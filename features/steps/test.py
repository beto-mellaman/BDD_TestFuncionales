from behave import given,when,then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Scenario Outline: visit "<browser page>" and check "<browser title>"
@when(u'we visit "{browser_page}"')
def step(context, browser_page):
   context.browser.get(f"{browser_page}")

@then('it should have a title "{browser_title}"')
def step(context, browser_title ):
    assert context.browser.title == f"{browser_title}"

# Scenario Outline: search "<product>" and count "<total>"
@when(u'we search "{product}"')
def step_impl(context, product):
   a=context.browser.find_element(By.ID, 'mainsearch-input') # busca la barra de busqueda
   a.send_keys(f'{product}' + Keys.ENTER) # escribe en la barra de busqueda y simula el "enter"

@then(u'it should be "{total}"')
def step_impl(context, total):
   productos = context.browser.find_elements(By.CLASS_NAME, 'product-grid-box-tile') # almacena los productos
   cuenta = len(productos) # cuenta la cantidad de productos
   assert cuenta == int(total)

# Scenario Outline: after search "wifi" check web "<title>"
@then('web should have a title "{title}"')
def step(context, title ):
   assert context.browser.title == f"{title}"

# Scenario Outline: after search "wifi" check search "<searchTitle>"
@then('search title should be a title "{searchTitle}"')
def step(context, searchTitle ):
   assert context.browser.find_element(By.CLASS_NAME, 'result_count').text == f"{searchTitle}"

# Scenario Outline: add "product" to "shoping cart" and chek "<message>"
@when('add product')
def step_impl(context):
   context.browser.find_element(By.CLASS_NAME, 'product-grid-box-tile').click()
   context.browser.find_element(By.ID, 'add-to-cart').click()

@then(u'check "{message}"')
def step_impl(context, message):
   assert context.browser.find_element(By.CLASS_NAME, 'basket-overlay__title').text == f"{message}"