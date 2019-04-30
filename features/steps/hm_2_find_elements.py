from selenium.webdriver.common.by import By
from behave import given, when, then

CLICK_TRY_PRIME = (By.CSS_SELECTOR, "a.nav-sprite.nav-logo-tagline.nav-prime-try")
BENEFIT_CARDS = (By.CSS_SELECTOR, 'div#prime-benefit-cards div.card-title')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Try Prime navigation link')
def click_try_prime(context):
    context.driver.find_element(*CLICK_TRY_PRIME).click()


@then('Verify 4 prime benefits cards are displayed')
def verify_on_try_prime_page(context):
    cards = context.driver.find_elements(*BENEFIT_CARDS)
    print(cards)
    assert len(cards) == 4, 'Expected cards amount is 4, but get {}'.format(len(cards))
