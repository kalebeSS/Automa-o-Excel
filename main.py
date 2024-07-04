import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


sheet = openpyxl.load_workbook('numeros.xlsx')
pagina = sheet['Página1']

for linha in pagina.iter_cols(min_row=2, values_only=True, max_row=21):
	for valor in linha:
		driver = webdriver.Chrome()
		driver.get('https://www.google.com')
		time.sleep(5)
		driver.find_element(By.XPATH, '//*[@id="input"]').send_keys(valor)
