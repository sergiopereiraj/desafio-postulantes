from lib2to3.pgen2 import driver
from selenium import webdriver
from bs4 import BeautifulSoup
import json

url = 'https://www.sii.cl/servicios_online/1047-nomina_inst_financieras-1714.html'

driver = webdriver.Chrome(executable_path='C:\dchrome\chromedriver.exe')

driver.get(url)

driver.maximize_window()

ides = driver.find_elements_by_xpath('//tbody/tr/td[1]')
razonSociales = driver.find_elements_by_xpath('//tbody/tr/td[2]')
paises = driver.find_elements_by_xpath('//tbody/tr/td[3]')
datos = driver.find_elements_by_xpath('//tbody/tr/td[4]')
vigencias = driver.find_elements_by_xpath('//tbody/tr/td[5]')
actualizaciones = driver.find_elements_by_xpath('//tbody/tr/td[6]')
estados = driver.find_elements_by_xpath('//tbody/tr/td[7]')

lista = []
for i in range(156):
    temporaly_data = {"No": ides[i].text, "RAZON SOCIAL": razonSociales[i].text, "PAIS": paises[i].text, "DATOS INSCRIPCION": datos[i].text, "VIGENCIA HASTA": vigencias[i].text, "DATOS ULTIMA ACTUALIZACION":actualizaciones[i].text, "ESTADO": estados[i].text}
    lista.append(temporaly_data)



data_json = json.dumps(lista)

print(data_json)
