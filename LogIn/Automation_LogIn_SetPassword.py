from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

# Localizar elementos y realizar acciones
# Buscamos por ID porque es el más seguro
driver.find_element(By.ID, "username").send_keys("studentt")
driver.find_element(By.ID, "password").send_keys("Password123")

# Hacemos clic en el botón de login
driver.find_element(By.ID, "submit").click()

input("¿Se movió a la siguiente página? Presiona Enter...")
driver.quit()