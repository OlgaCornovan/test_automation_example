from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

#
from selenium.webdriver.support.wait import WebDriverWait

CLICK_AD_FEEDBACK = (By.CSS_SELECTOR, "span#ad-feedback-text-right-2")
# VERIFY_POPUP_WINDOW = (By.CSS_SELECTOR, "div.a-popover-wrapper")
VERIFY_POPUP_WINDOW = (By.CSS_SELECTOR, "h4#a-popover-header-4")


@given('Open Amazon1 page')
def open_amazon1(context):
    context.driver.get('https://www.amazon.com')


@when('Click on Ad feedback link')
def click_ad_feedback(context):
    context.driver.wait = WebDriverWait(context.driver, 4)
    context.driver.find_element(*CLICK_AD_FEEDBACK).click()


@then('Verify popup window is opened')
def popup_window(context):
    context.driver.wait = WebDriverWait(context.driver, 4)
    # context.driver.wait.until(EC.presence_of_element_located)
    popup_window_check = context.driver.find_element(*VERIFY_POPUP_WINDOW)
    print(popup_window_check)
    assert context.driver.find_element(*VERIFY_POPUP_WINDOW).text == "Share your feedback"

