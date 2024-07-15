from selenium.webdriver.remote.webelement import WebElement


class Command:
    def execute(self, element: WebElement):
        raise NotImplementedError("You should implement this method")


class ClickCommand(Command):
    def execute(self, element: WebElement):
        element.click()


class SendKeys(Command):
    def __init__(self, keys: str):
        self.keys = keys

    def execute(self, element: WebElement):
        element.send_keys(self.keys)

# /html/body/div[2]/div[2]/section/section[4]/ul/li[1]/div/div/div[1]/a
# /html/body/div[2]/div[2]/section/section[4]/ul/li[2]/div/div/div[1]/a