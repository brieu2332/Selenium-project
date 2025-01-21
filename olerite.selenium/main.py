from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar o serviço do ChromeDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Acessar o site
driver.get("https://egov.santos.sp.gov.br/contador/")

# Esperar um pouco para o site carregar
time.sleep(2)

# Localizar o campo de login e inserir o valor
login_field = driver.find_element(By.ID, "login")
login_field.send_keys("v0016813")

# Localizar o campo de senha e inserir o valor
password_field = driver.find_element(By.ID, "pass")
password_field.send_keys("casa6042")

# Esperar para inserir o CAPTCHA (ou anti-robô manualmente)
time.sleep(20)

# Localizar o botão de acesso e clicar
access_button = driver.find_element(By.ID, "submit")
access_button.click()

# Aguardar o carregamento da página pós-login
time.sleep(10)


 # Selecionar o ano (ID: "ano-button")
year_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "ano-button"))
)
year_button.click()

# Esperar os itens da lista ficarem visíveis
year_option = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//ul[@id='ano-menu']//li[contains(text(),'2024')]"))
)

year_option.click()

# # Selecionar o mês (ID: "mes-button")
# month_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, "mes-button"))
# )
# month_button.click()

# Localizar o botão "Consultar" e clicar (ID: "consultar-previdencia-dinamica")
consult_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "consultar-holerite"))
)
consult_button.click()

# Aguardar o carregamento dos resultados (tempo ajustável)
time.sleep(2)

# Localizar o botão "Imprimir" e clicar (ID: "imprimir")
print_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "imprimir"))
)
print_button.click()

time.sleep(5)

imprimir_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='sidebar'']//print-preview-button-strip//div/cr-button[2]"))
)
imprimir_button.click()

# # Localizar o botão pelo XPath e clicar 
# imprimir_button = driver.find_element(By.XPATH, "/html/body/print-preview-app//print-preview-sidebar//print-preview-button-strip//div/cr-button[1]")
#     imprimir_button.click()



# Esperar um tempo para observar o resultado antes de fechar o navegador
time.sleep(10)

# Fechar o navegador
driver.quit()
