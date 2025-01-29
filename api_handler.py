import requests
import json
import logging
from requests.exceptions import RequestException, Timeout, ConnectionError, HTTPError

# تنظیمات logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ApiHandler:
    def __init__(self, api_url, timeout=60, max_retries=3):
        self.api_url = api_url
        self.timeout = timeout
        self.max_retries = max_retries

    def fetch_data(self):
        retries = 0
        while retries < self.max_retries:
            try:
                response = requests.get(self.api_url, timeout=self.timeout)
                response.raise_for_status()
                data = response.json()
                return data
            except Timeout:
                logging.warning(f"Timeout error for URL: {self.api_url}. Retrying...")
                retries += 1
            except ConnectionError:
                logging.warning(f"Connection error for URL: {self.api_url}. Retrying...")
                retries += 1
            except HTTPError as e:
                logging.error(f"HTTP error for URL: {self.api_url}: {e}")
                return None
            except json.JSONDecodeError as e:
                logging.error(f"Error decoding JSON from URL: {self.api_url}: {e}")
                return None
            except RequestException as e:
                logging.error(f"A general request error occurred: {e}")
                return None
        logging.error(f"Max retries exceeded for URL: {self.api_url}")
        return None