from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=15)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f"Expected {expected_text} but got {actual_text}"

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f"Expected {expected_text} but got {actual_text}"

    def presence_of_element_located(self, *locator):
        self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Couldn't find the presence of element at '{locator}'"
        )

    def wait_element_locator_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by '{locator}' is not clickable."
        )

    def wait_element_clickable(self, element):
        self.wait.until(
            EC.element_to_be_clickable(element),
            message=f"Element '{element}' is not clickable."
        )

    def wait_locator_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by '{locator}' is not clickable."
        ).click()

    def wait_element_clickable_click(self, element):
        self.wait.until(
            EC.element_to_be_clickable(element),
            message=f"Element by '{element}' is not clickable."
        ).click()

    def verify_partial_url(self, expected_partial_url):
        self.wait.until(
            EC.url_contains(expected_partial_url),
            message=f'Expected {expected_partial_url} not in url'
        )

    def verify_url(self, url):
        self.wait.until(
            EC.url_to_be(url),
            message=f'Expected {url} is not present.'
        )

    def hover_over(self, web_element):
        actions = ActionChains(self.driver)
        actions.move_to_element(web_element)
        actions.pause(2)
        actions.perform()


