"""
Scrape curated MLS soccer knowledge pages from multiple sources via Firecrawl
and write one Markdown file per URL into knowledge/raw/, each with a YAML
front-matter block capturing provenance (source URL, scrape time, source domain).

Run:
    .venv/bin/python3 extract/extract_knowledge_sources.py

Required env var (.env):
    FIRECRAWL_API_KEY    API key from firecrawl.dev

Output:
    knowledge/raw/<slug>.md   one file per URL in TARGETS

Targets currently span fbref.com, mlssoccer.com, and americansocceranalysis.com.
The script logs and skips any individual failure (404, network error, empty
markdown) rather than aborting — partial scrapes are normal.

SDK: firecrawl-py 4.23.0 (v2 client: `from firecrawl import Firecrawl`)
"""
import logging
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from dotenv import load_dotenv
from firecrawl import Firecrawl

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
)
log = logging.getLogger(__name__)

OUTPUT_DIR = Path('knowledge/raw')
SLEEP_SECONDS = 2

TARGETS = [
    # fbref.com — MLS competition stats pages (7)
    'https://fbref.com/en/comps/22/Major-League-Soccer-Stats',
    'https://fbref.com/en/comps/22/stats/Major-League-Soccer-Stats',
    'https://fbref.com/en/comps/22/shooting/Major-League-Soccer-Stats',
    'https://fbref.com/en/comps/22/passing/Major-League-Soccer-Stats',
    'https://fbref.com/en/comps/22/defense/Major-League-Soccer-Stats',
    'https://fbref.com/en/comps/22/possession/Major-League-Soccer-Stats',
    'https://fbref.com/en/comps/22/misc/Major-League-Soccer-Stats',

    # fbref.com — illustrative MLS-relevant player profiles (3)
    'https://fbref.com/en/players/d70ce98e/Lionel-Messi',
    'https://fbref.com/en/players/00e7e57b/Sergio-Busquets',
    'https://fbref.com/en/players/8b04d6c1/Jordi-Alba',

    # mlssoccer.com — league context and current standings (4)
    'https://www.mlssoccer.com/about/',
    'https://www.mlssoccer.com/news/',
    'https://www.mlssoccer.com/standings/',
    'https://www.mlssoccer.com/competitions/mls-cup-playoffs',

    # americansocceranalysis.com — long-form MLS analytics articles (4)
    'https://www.americansocceranalysis.com/home/2024/8/27/state-of-the-mls-academy-system',
    'https://www.americansocceranalysis.com/home/2024/2/16/breaking-down-mls-roster-rules',
    'https://www.americansocceranalysis.com/home/2023/11/15/mls-expected-goals-leaders',
    'https://www.americansocceranalysis.com/home',
]


def url_to_slug(url):
    """Convert a URL path into a filesystem-safe slug.

    >>> url_to_slug('https://fbref.com/en/comps/22/Major-League-Soccer-Stats')
    'en_comps_22_Major-League-Soccer-Stats'
    """
    path = urlparse(url).path.strip('/')
    slug = path.replace('/', '_')
    slug = re.sub(r'[^A-Za-z0-9._-]', '_', slug)
    return slug or 'index'


def url_to_source(url):
    """Return the bare host (without leading 'www.') for the source: front-matter field."""
    host = urlparse(url).netloc.lower()
    if host.startswith('www.'):
        host = host[4:]
    return host


def write_markdown_file(out_dir, url, markdown):
    slug = url_to_slug(url)
    path = out_dir / f'{slug}.md'
    front_matter = (
        '---\n'
        f'source_url: {url}\n'
        f'scraped_at: {datetime.now(timezone.utc).isoformat()}\n'
        f'source: {url_to_source(url)}\n'
        '---\n\n'
    )
    path.write_text(front_matter + (markdown or ''), encoding='utf-8')
    return path


def main():
    api_key = os.environ['FIRECRAWL_API_KEY']
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    client = Firecrawl(api_key=api_key)

    successes = []
    failures = []

    for i, url in enumerate(TARGETS):
        log.info('[%d/%d] Scraping %s', i + 1, len(TARGETS), url)
        try:
            doc = client.scrape(url, formats=['markdown'], only_main_content=True)
            markdown = getattr(doc, 'markdown', None)
            if not markdown:
                log.error('No markdown returned for %s — skipping', url)
                failures.append(url)
            else:
                path = write_markdown_file(OUTPUT_DIR, url, markdown)
                log.info('Wrote %s (%d chars)', path, len(markdown))
                successes.append(url)
        except Exception as exc:
            log.error('Failed to scrape %s: %s', url, exc)
            failures.append(url)

        if i < len(TARGETS) - 1:
            time.sleep(SLEEP_SECONDS)

    print()
    print('Scrape summary:')
    print(f'  succeeded : {len(successes)}')
    print(f'  failed    : {len(failures)}')
    print(f'  output    : {OUTPUT_DIR.resolve()}')
    if failures:
        print('Failed URLs:')
        for u in failures:
            print(f'  - {u}')


if __name__ == '__main__':
    main()
