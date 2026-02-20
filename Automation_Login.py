#Creating new document for python scripts

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Esto descarga el driver automáticamente y abre el navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))