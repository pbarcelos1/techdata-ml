import os

from abc import ABC, abstractmethod
from typing import List, Dict, Any

from pathlib import Path

from tqdm import tqdm
from utils.constants import espera, get_soup, build_session, load_existing_urls, append_on_jsonl

class FetchResult:
    url: str
    status_code: int
    text: str
    headers: Dict[str, str]


class Scraper(ABC):
    def __init__(self, base_url : str = None, out_dir : Path = None, site : str = None, max_pages : int = 1, starting_page : int = 1):
        if not base_url or not isinstance(base_url, str):
            raise ValueError("base_url must be a non-empty string")
        if not isinstance(out_dir, Path):
            raise ValueError("out_dir must be a non-empty Path object")
        if not site or not isinstance(site, str):
            raise ValueError("site must be a non-empty string")
        if not max_pages or not isinstance(max_pages, int) or max_pages < 1:
            raise ValueError("max_pages must be a non-empty integer")
        if not isinstance(starting_page, int) or starting_page < 1:
            raise ValueError("starting_page must be a non-empty integer")
        if not isinstance(starting_page, int) or starting_page < 1:
            raise ValueError("starting_page must be a non-empty integer")
        
        self.base_url = base_url
        self.out_dir = out_dir
        self.site = site
        self.max_pages = max_pages
        self.jsonl_file = self.out_dir / (self.site + ".jsonl")
        self.session = build_session()
        os.makedirs(self.out_dir, exist_ok=True)

    @abstractmethod
    def parse_listing_page(self, page: int) -> set[str]:
        """
        Parse the listing page and yield the URLs of the articles to be scraped.
        Args:
            page: Page number.
        Returns:
            Set[str]: Set of URLs of the articles to be scraped.
        """
        pass
    
    @abstractmethod
    def extract_data(self, soup) -> Dict:
        """
        Extract the data from the article page and return a dictionary with the data.
        """
        pass

    def iter_listing_urls(self) -> List[str]:
        """
        Iterate over the listing pages and yield the URLs of the articles to be scraped.
        Args:
            **kwargs: Arguments for the listing page (e.g. page number, max pages, etc.).
        Returns:
            List[str]: List of URLs of the articles to be scraped.
        """
        new_urls = list()
        for i in tqdm(range(self.max_pages), desc="Pages"):
            urls = self.parse_listing_page(page=i + 1)
            # adiciona apenas as URLs que ainda não existiam
            fresh_urls = urls.difference(self.existing_urls)
            new_urls.extend(fresh_urls)
        return new_urls

    def parse_article_page(self, url: str) -> Dict[str, Any]:
        """
        Parse the article page and return a dictionary with the data.
        Args:
            url: URL of the article page.
        Returns:
            Dict[str, Any]: Dictionary with the data of the article.
        """
        soup = get_soup(url, self.session)
        if not soup:
            raise ValueError(f"Failed to parse article page: {url}")
        return self.extract_data(soup)

    def run(self):
        print(f"Scraping site: {self.site}, max pages: {self.max_pages}")
        print(f"Output directory: {self.out_dir}")
        self.existing_urls = load_existing_urls(self.jsonl_file)
        print(f"Found {len(self.existing_urls)} existing URLs in {self.jsonl_file}")
        new_urls = self.iter_listing_urls()
        print(f"Found {len(new_urls)} new URLs to scrape")

        written_urls = 0
        for url in tqdm(new_urls, desc="Articles"):
            try:
                data = self.parse_article_page(url)
                if data:
                    append_on_jsonl(data, self.jsonl_file)
                    written_urls += 1
            except Exception as e:
                print(f"Error processing article: {url} -> {e}")
            espera()

        print(f"Finished scraping site: {self.site}")
        print(f"Wrote {written_urls} new items to {self.jsonl_file}")