from selenium import webdriver

# 1. Abrir el navegador (Chrome)
driver = webdriver.Chrome()

# 2. Ir a la URL
url = "https://practicetestautomation.com/practice-test-login/"
driver.get(url)

# 3. Verificar que cargó (opcional pero buena práctica)
print("Título de la página:", driver.title)

# Mantenemos abierto para ver el resultado
input("Presiona Enter para cerrar...")
driver.quit()