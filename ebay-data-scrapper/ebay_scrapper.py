from selenium import webdriver
from selenium.webdriver.edge.options import Options


class EbayScrapper:

    def __init__(self):
        pass

    def open_page(self, url: str):
        edge_options = Options()
        edge_options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=edge_options)
        driver.get(url)
