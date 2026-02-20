from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# El código se detendrá aquí y el navegador se quedará abierto
input("Presiona Enter en la terminal para cerrar el navegador...")

driver.quit()