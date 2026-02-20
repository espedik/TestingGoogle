import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRegistro(unittest.TestCase):

    def setUp(self):
        # Configuración inicial: Abrir el navegador
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/login") # Usamos una página de prueba real

    def test_campos_vacios(self):
        driver = self.driver
        # 1. Localizar el botón de submit y darle clic sin llenar nada
        boton_login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        boton_login.click()

        # 2. Capturar el mensaje de error que aparece en la página
        mensaje_error = driver.find_element(By.ID, "flash").text

        # 3. EL ASSERT: Verificamos que el mensaje contenga la palabra 'invalid'
        # Si el mensaje no contiene eso, la prueba fallará automáticamente
        self.assertIn("invalid", mensaje_error)

    def test_registro_exitoso(self):
        driver = self.driver
        
        # Llenar datos válidos (Usando credenciales de esa página de prueba)
        driver.find_element(By.NAME, "username").send_keys("tomsmith")
        driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")
        
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Validar que entramos a la zona segura
        mensaje_exito = driver.find_element(By.ID, "flash").text
        self.assertIn("You logged into a secure area!", mensaje_exito)

    def tearDown(self):
        # Cerrar el navegador al terminar cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()