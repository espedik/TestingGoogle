from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.amazon.com.mx")
driver.title
print(driver.title)
driver.maximize_window()
# El código se detendrá aquí y el navegador se quedará abierto
input("Presiona Enter en la terminal para cerrar el navegador...")

driver.quit()