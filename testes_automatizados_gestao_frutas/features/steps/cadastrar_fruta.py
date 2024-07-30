from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('que estou na página de cadastro de frutas')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('http://localhost:3000/#/login')

    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).send_keys('gabriel')
    password_input = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
    password_input.send_keys('vCRz*z9QT!xj!4P')
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, 'loginButton'))).click()

    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.layout-menu-button"))).click()
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Cadastros']"))).click()
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Cadastrar Fruta']"))).click()
    
@when('eu preencho o formulário com dados válidos')
def step_impl(context):
    driver = context.driver
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'nome'))).send_keys('Maçã')
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'classificacao'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[text()='Extra']"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'fresca'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[text()='Sim']"))).click()
    
    quantity_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@id='quantidadeDisponivel']//input")))
    quantity_input.clear()
    quantity_input.send_keys('100')
    
    value_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@id='valorVenda']//input")))
    value_input.clear()
    value_input.send_keys('5.00')

@when('eu submeto o formulário')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, 'cadastrarFrutaBtn'))).click()

@then('a fruta deve ser cadastrada com sucesso')
def step_impl(context):
    success_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'p-toast-summary'))
    ).text
    assert 'Sucesso' in success_message
    context.driver.quit()
