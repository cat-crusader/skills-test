from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from typing import Tuple

from element_commands import Command, ClickCommand, SendKeys


class EbayScrapper:

    def __init__(self):
        edge_options = Options()
        edge_options.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(options=edge_options)
        self.wait_time = 5

    def close(self):
        self.driver.close()

    def open_page(self, url: str):
        self.driver.get(url)

    def get_element(self, locator: Tuple[str, str]):
        by, path = locator
        wait = WebDriverWait(self.driver, self.wait_time)
        return wait.until(EC.presence_of_element_located((by, path)))

    def perform_action(self, element: WebElement, command: Command):
        if element:
            command.execute(element)
