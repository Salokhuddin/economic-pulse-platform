import requests

from extractors.base import BaseExtractor


class FREDExtractor(BaseExtractor):
    """Extractor for FRED data.
    Extracts data and validates it"""

    def __init__(self, access_key):
        super().__init__("FRED", "https://api.stlouisfed.org/fred/series/observations", access_key)

    def extract(self, series_id):
        """Extracts data for the requested series_id (ex.: GDP)"""
        try:
            params = {"series_id": series_id, "api_key": self.access_key, "file_type": "json"}
            response = requests.get(self.address, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"FRED Extraction failed for {series_id}: {e}")
            raise

    def validate(self, extracted_data):
        """Checks for observation existence; replaces empty value with None"""
        if "observations" not in extracted_data:
            raise KeyError("Response missing 'observations' key")
        if not extracted_data["observations"]:
            raise ValueError("Response missing observations")
        for observation in extracted_data["observations"]:
            if observation["value"] == ".":
                observation["value"] = None
        return extracted_data
