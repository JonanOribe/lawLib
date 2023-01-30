import configparser

config = configparser.ConfigParser()
config.read("config.ini")

class DataScrapper:
    def __init__(self, source) -> None:
        self.source:str = {section: dict(config.items(section)) for section in config.sections()}['URLS'][source.lower()]

    def get_scrapper_sources(self):
        return {section: dict(config.items(section)) for section in config.sections()}['URLS']