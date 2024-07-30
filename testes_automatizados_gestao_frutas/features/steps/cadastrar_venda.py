from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('Eu estou na página de cadastro de vendas')
def step_impl(context):   
    
    # Inicializar o WebDriver e acessar a página de login
    context.driver = webdriver.Chrome()
    context.driver.get('http://localhost:3000/#/login') # URL da página de login

    # Fazer login
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).send_keys('gabriel')
    password_input = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
    password_input.send_keys('vCRz*z9QT!xj!4P')
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, 'loginButton'))).click()


    # Navegar pelo menu "Cadastros" e clicar em "Cadastrar Fruta"
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.layout-menu-button"))).click()
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Cadastros']"))).click()
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Cadastrar Vendas']"))).click()

@when('Eu seleciono uma fruta e um vendedor, e preencho a quantidade e o desconto')
def step_impl(context):
    driver = context.driver
    
    # Selecionar uma fruta
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'fruta'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[text()='Banana']"))).click()
    
    # Preencher quantidade vendida
    quantity_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@id='quantidadeVendida']//input")))
    quantity_input.clear()
    quantity_input.send_keys('1')
    
    # Selecionar desconto
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'desconto'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[text()='5%']"))).click()
    
    # Selecionar vendedor
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'vendedor'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[text()='gabriel']"))).click()
    
@when('Eu clico no botão de cadastrar venda')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, 'cadastrarVendaBtn'))).click()

@then('A venda deve ser cadastrada com sucesso')
def step_impl(context):
    success_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'p-toast-summary'))
    ).text
    assert 'Sucesso' in success_message
    context.driver.quit()
