from abc import ABC, abstractmethod


class BaseExtractor(ABC):
    """Abstract base class for all data source extractors.

    Defines the interface that every extractor must implement,
    ensuring consistent behavior across different data sources.
    """

    def __init__(self, data_source_name, data_source_address, access_key=None):
        self.name = data_source_name
        self.address = data_source_address
        self.access_key = access_key

    @abstractmethod
    def extract(self, series: str) -> dict:
        """Receives data series to extract and returns fetched data in dict format"""
        pass

    @abstractmethod
    def validate(self, raw_data):
        """Receives extracted data and validates it against the desired format."""
        pass

    def get_metadata(self):
        """Returns metadata about the data source: its name, URL,
        and whether or not it has access_key"""
        return {
            "source_name": self.name,
            "base_url": self.address,
            "has_api_key": self.access_key is not None,
        }
