from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Diretório de download desejado
download_dir = r"C:\Users\gabri\Desktop\olerite"

# Garantir que o diretório exista
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Configurar as opções do Chrome para download
chrome_options = webdriver.ChromeOptions()
prefs = {
    "printing.print_preview_sticky_settings.appState": '{"recentDestinations":[{"id":"Save as PDF","origin":"local","account":""}],"selectedDestinationId":"Save as PDF","version":2}',
    "savefile.default_directory": download_dir,  # Define o diretório de download
    "download.default_directory": download_dir,  # Certifique-se de que este também esteja configurado
    "download.prompt_for_download": False,  # Impede a exibição de prompts para salvar
    "download.directory_upgrade": True,  # Garante que as alterações de diretório sejam aplicadas
}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--kiosk-printing")  # Habilita a impressão automática

# Configurar o serviço do ChromeDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Acessar o site
driver.get("https://egov.santos.sp.gov.br/contador/")

# Esperar um pouco para o site carregar
time.sleep(1)

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

# IDs dos meses como variáveis separadas
mes4 = "//ul[@id='mes-menu']/li[1]"
mes5 = "//ul[@id='mes-menu']/li[2]"
mes6 = "//ul[@id='mes-menu']/li[3]"
mes7 = "//ul[@id='mes-menu']/li[4]"
mes8 = "//ul[@id='mes-menu']/li[5]"
mes9 = "//ul[@id='mes-menu']/li[6]"
mes10 =" //ul[@id='mes-menu']/li[7]"
mes11 =" //ul[@id='mes-menu']/li[8]"
mes12 =" //ul[@id='mes-menu']/li[9]"
mes13 =" //ul[@id='mes-menu']/li[10]"
mes14 =" //ul[@id='mes-menu']/li[11]"
mes15 =" //ul[@id='mes-menu']/li[12]"
mes16 =" //ul[@id='mes-menu']/li[13]"
mes17 =" //ul[@id='mes-menu']/li[14]"
mes18 =" //ul[@id='mes-menu']/li[15]"

# Função para realizar o processo para um mês específico
def processar_mes(mes_id):
    # Selecionar o ano
    time.sleep(1)
    year_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ano-button"))
    )
    year_button.click()

    time.sleep(1)

    # Selecionar o ano de 2024
    year_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//ul[@id='ano-menu']//li[contains(text(),'2024')]"))
    )
    year_option.click()

    time.sleep(1)

    # Abrir o menu de seleção do mês
    mes_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "mes-button"))
    )
    mes_button.click()

    time.sleep(1)

    # Selecionar o mês correspondente
    mes_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, mes_id))
    )
    mes_option.click()

    time.sleep(1)

    # Localizar o botão "Consultar" e clicar
    consult_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "consultar-holerite"))
    )
    consult_button.click()

    # Aguardar o carregamento dos resultados
    time.sleep(1)

    try:
        # Tentar localizar e clicar no botão "Imprimir"
        print_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "imprimir"))
        )
        print_button.click()

        # Aguardar o processo de impressão
        time.sleep(2)

        print("Impressão realizada com sucesso.")

    except Exception as e:
        # Caso o botão "Imprimir" não seja encontrado ou clique falhar
        print(f"Erro ao tentar imprimir!!!!!!!{mes_id}: {e}")

    finally:
        # Clicar no botão "Voltar" independente do sucesso ou falha
        try:
            voltarDoImprimir = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "voltar"))
            )
            voltarDoImprimir.click()
            print("Retornando para a página anterior.")
        except Exception as e:
            print(f"Erro ao tentar voltar: {e}")
    print("{}\n".format(mes_id))


# Repetir o processo para cada mês
processar_mes(mes4)
print('mes concluido')

processar_mes(mes5)
print('mes concluido')

processar_mes(mes6)
print('mes concluido')

processar_mes(mes7)
print('mes concluido')

processar_mes(mes8)
print('mes concluido')

processar_mes(mes9)
print('mes concluido')

processar_mes(mes10)
print('mes concluido')

processar_mes(mes11)
print('mes concluido')

processar_mes(mes12)
print('mes concluido')

processar_mes(mes13)
print('mes concluido')

processar_mes(mes14)
print('mes concluido')

processar_mes(mes15)
print('mes concluido')

processar_mes(mes16)
print('mes concluido')

processar_mes(mes17)
print('mes concluido')

processar_mes(mes18)
print('mes concluido')

# Função para realizar o processo para um mês específico
def processar_mes2023(mes_id):
    # Selecionar o ano
    time.sleep(1)
    year_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ano-button"))
    )
    year_button.click()

    time.sleep(1)

    # Selecionar o ano de 2024
    year_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//ul[@id='ano-menu']//li[contains(text(),'2023')]"))
    )
    year_option.click()

    time.sleep(1)

    # Abrir o menu de seleção do mês
    mes_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "mes-button"))
    )
    mes_button.click()

    time.sleep(1)

    # Selecionar o mês correspondente
    mes_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, mes_id))
    )
    mes_option.click()

    time.sleep(1)

    # Localizar o botão "Consultar" e clicar
    consult_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "consultar-holerite"))
    )
    consult_button.click()

    # Aguardar o carregamento dos resultados
    time.sleep(1)

    try:
        # Tentar localizar e clicar no botão "Imprimir"
        print_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "imprimir"))
        )
        print_button.click()

        # Aguardar o processo de impressão
        time.sleep(2)

        print("Impressão realizada com sucesso.")

    except Exception as e:
        # Caso o botão "Imprimir" não seja encontrado ou clique falhar
        print(f"Erro ao tentar imprimir!!!!!!!{mes_id}: {e}")

    finally:
        # Clicar no botão "Voltar" independente do sucesso ou falha
        try:
            voltarDoImprimir = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "voltar"))
            )
            voltarDoImprimir.click()
            print("Retornando para a página anterior.")
        except Exception as e:
            print(f"Erro ao tentar voltar: {e}")
    print("{}\n".format(mes_id))


# Repetir o processo para cada mês
processar_mes2023(mes4)
print('mes concluido')

processar_mes2023(mes5)
print('mes concluido')

processar_mes2023(mes6)
print('mes concluido')

processar_mes2023(mes7)
print('mes concluido')

processar_mes2023(mes8)
print('mes concluido')

processar_mes2023(mes9)
print('mes concluido')

processar_mes2023(mes10)
print('mes concluido')

processar_mes2023(mes11)
print('mes concluido')

processar_mes2023(mes12)
print('mes concluido')

processar_mes2023(mes13)
print('mes concluido')

processar_mes2023(mes14)
print('mes concluido')

processar_mes2023(mes15)
print('mes concluido')

processar_mes2023(mes16)
print('mes concluido')

processar_mes2023(mes17)
print('mes concluido')

processar_mes2023(mes18)
print('mes concluido')

# Função para realizar o processo para um mês específico
def processar_mes2022(mes_id):
    # Selecionar o ano
    time.sleep(1)
    year_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ano-button"))
    )
    year_button.click()

    time.sleep(1)

    # Selecionar o ano de 2024
    year_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//ul[@id='ano-menu']//li[contains(text(),'2022')]"))
    )
    year_option.click()

    time.sleep(1)

    # Abrir o menu de seleção do mês
    mes_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "mes-button"))
    )
    mes_button.click()

    time.sleep(1)

    # Selecionar o mês correspondente
    mes_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, mes_id))
    )
    mes_option.click()

    time.sleep(1)

    # Localizar o botão "Consultar" e clicar
    consult_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "consultar-holerite"))
    )
    consult_button.click()

    # Aguardar o carregamento dos resultados
    time.sleep(1)

    try:
        # Tentar localizar e clicar no botão "Imprimir"
        print_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "imprimir"))
        )
        print_button.click()

        # Aguardar o processo de impressão
        time.sleep(2)

        print("Impressão realizada com sucesso.")

    except Exception as e:
        # Caso o botão "Imprimir" não seja encontrado ou clique falhar
        print(f"Erro ao tentar imprimir!!!!!!!{mes_id}: {e}")

    finally:
        # Clicar no botão "Voltar" independente do sucesso ou falha
        try:
            voltarDoImprimir = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "voltar"))
            )
            voltarDoImprimir.click()
            print("Retornando para a página anterior.")
        except Exception as e:
            print(f"Erro ao tentar voltar: {e}")
    print("{}\n".format(mes_id))


# Repetir o processo para cada mês
processar_mes2022(mes4)
print('mes concluido')

processar_mes2022(mes5)
print('mes concluido')

processar_mes2022(mes6)
print('mes concluido')

processar_mes2022(mes7)
print('mes concluido')

processar_mes2022(mes8)
print('mes concluido')

processar_mes2022(mes9)
print('mes concluido')

processar_mes2022(mes10)
print('mes concluido')

processar_mes2022(mes11)
print('mes concluido')

processar_mes2022(mes12)
print('mes concluido')

processar_mes2022(mes13)
print('mes concluido')

processar_mes2022(mes14)
print('mes concluido')

processar_mes2022(mes15)
print('mes concluido')

processar_mes2022(mes16)
print('mes concluido')

processar_mes2022(mes17)
print('mes concluido')

processar_mes2022(mes18)
print('mes concluido')

# Função para realizar o processo para um mês específico
def processar_mes2021(mes_id):
    # Selecionar o ano
    time.sleep(1)
    year_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ano-button"))
    )
    year_button.click()

    time.sleep(1)

    # Selecionar o ano de 2024
    year_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//ul[@id='ano-menu']//li[contains(text(),'2021')]"))
    )
    year_option.click()

    time.sleep(1)

    # Abrir o menu de seleção do mês
    mes_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "mes-button"))
    )
    mes_button.click()

    time.sleep(1)

    # Selecionar o mês correspondente
    mes_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, mes_id))
    )
    mes_option.click()

    time.sleep(1)

    # Localizar o botão "Consultar" e clicar
    consult_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "consultar-holerite"))
    )
    consult_button.click()

    # Aguardar o carregamento dos resultados
    time.sleep(1)

    try:
        # Tentar localizar e clicar no botão "Imprimir"
        print_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "imprimir"))
        )
        print_button.click()

        # Aguardar o processo de impressão
        time.sleep(2)

        print("Impressão realizada com sucesso.")

    except Exception as e:
        # Caso o botão "Imprimir" não seja encontrado ou clique falhar
        print(f"Erro ao tentar imprimir!!!!!!!{mes_id}: {e}")

    finally:
        # Clicar no botão "Voltar" independente do sucesso ou falha
        try:
            voltarDoImprimir = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "voltar"))
            )
            voltarDoImprimir.click()
            print("Retornando para a página anterior.")
        except Exception as e:
            print(f"Erro ao tentar voltar: {e}")
    print("{}\n".format(mes_id))


# Repetir o processo para cada mês
processar_mes2021(mes4)
print('mes concluido')

processar_mes2021(mes5)
print('mes concluido')

processar_mes2021(mes6)
print('mes concluido')

processar_mes2021(mes7)
print('mes concluido')

processar_mes2021(mes8)
print('mes concluido')

processar_mes2021(mes9)
print('mes concluido')

processar_mes2021(mes10)
print('mes concluido')

processar_mes2021(mes11)
print('mes concluido')

processar_mes2021(mes12)
print('mes concluido')

processar_mes2021(mes13)
print('mes concluido')

processar_mes2021(mes14)
print('mes concluido')

processar_mes2021(mes15)
print('mes concluido')

processar_mes2021(mes16)
print('mes concluido')

processar_mes2021(mes17)
print('mes concluido')

processar_mes2021(mes18)
print('mes concluido')

# Função para realizar o processo para um mês específico
def processar_mes2020(mes_id):
    # Selecionar o ano
    time.sleep(1)
    year_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ano-button"))
    )
    year_button.click()

    time.sleep(1)

    # Selecionar o ano de 2024
    year_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//ul[@id='ano-menu']//li[contains(text(),'2020')]"))
    )
    year_option.click()

    time.sleep(1)

    # Abrir o menu de seleção do mês
    mes_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "mes-button"))
    )
    mes_button.click()

    time.sleep(1)

    # Selecionar o mês correspondente
    mes_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, mes_id))
    )
    mes_option.click()

    time.sleep(1)

    # Localizar o botão "Consultar" e clicar
    consult_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "consultar-holerite"))
    )
    consult_button.click()

    # Aguardar o carregamento dos resultados
    time.sleep(1)

    try:
        # Tentar localizar e clicar no botão "Imprimir"
        print_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "imprimir"))
        )
        print_button.click()

        # Aguardar o processo de impressão
        time.sleep(2)

        print("Impressão realizada com sucesso.")

    except Exception as e:
        # Caso o botão "Imprimir" não seja encontrado ou clique falhar
        print(f"Erro ao tentar imprimir!!!!!!!{mes_id}: {e}")

    finally:
        # Clicar no botão "Voltar" independente do sucesso ou falha
        try:
            voltarDoImprimir = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "voltar"))
            )
            voltarDoImprimir.click()
            print("Retornando para a página anterior.")
        except Exception as e:
            print(f"Erro ao tentar voltar: {e}")
    
    print("{}\n".format(mes_id))


# Repetir o processo para cada mês
processar_mes2020(mes4)
print('mes concluido')

processar_mes2020(mes5)
print('mes concluido')

processar_mes2020(mes6)
print('mes concluido')

processar_mes2020(mes7)
print('mes concluido')

processar_mes2020(mes8)
print('mes concluido')

processar_mes2020(mes9)
print('mes concluido')

processar_mes2020(mes10)
print('mes concluido')

processar_mes2020(mes11)
print('mes concluido')

processar_mes2020(mes12)
print('mes concluido')

processar_mes2020(mes13)
print('mes concluido')

processar_mes2020(mes14)
print('mes concluido')

processar_mes2020(mes15)
print('mes concluido')

processar_mes2020(mes16)
print('mes concluido')

processar_mes2020(mes17)
print('mes concluido')

processar_mes2020(mes18)
print('mes concluido')


# O arquivo será salvo automaticamente no diretório configurado
time.sleep(10)

# Fechar o navegador
driver.quit()
