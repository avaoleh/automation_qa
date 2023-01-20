from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    @allure.step('Open a browser')
    def open(self):
        self.browser.get(self.url)

    @allure.step('Find a visible element')
    def element_is_visible(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Find visible elements')
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Find a present element')
    def element_is_present(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Find present elements')
    def elements_are_present(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step('Find a not visible element')
    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Find clickable elements')
    def element_is_clickable(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Go to specified element')
    def go_to_element(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Double click')
    def action_double_click(self, element):
        action = ActionChains(self.browser)
        action.double_click(element)
        action.perform()

    @allure.step('Right click')
    def action_right_click(self, element):
        action = ActionChains(self.browser)
        action.context_click(element)
        action.perform()

    @allure.step('Drag and drop by offset')
    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.browser)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    @allure.step('Drag and drop element to element')
    def action_drag_and_drop_to_element(self, what, where):
        action = ActionChains(self.browser)
        action.drag_and_drop(what, where)
        action.perform()

    @allure.step('Move cursor to element')
    def action_move_to_element(self, element):
        action = ActionChains(self.browser)
        action.move_to_element(element)
        action.perform()

    @allure.step('Remove footer')
    def remove_footer(self):
        self.browser.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.browser.execute_script("document.getElementById('close-fixedban').remove();")
