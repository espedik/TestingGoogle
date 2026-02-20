import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestFormulario(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        # Login rápido para llegar al formulario
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        # Ir a la zona de pago
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

    def test_errores_formulario(self):
        driver = self.driver
        # DATOS DINÁMICOS: (Nombre, Apellido, Zip, Error esperado)
        casos = [
            ("", "Perez", "12345", "Error: First Name is required"),
            ("Karla", "", "12345", "Error: Last Name is required"),
            ("Karla", "Civil", "", "Error: Postal Code is required")
        ]

        for nom, ape, zip_code, error_esperado in casos:
            driver.refresh() # Limpiar todo
            driver.find_element(By.ID, "first-name").send_keys(nom)
            driver.find_element(By.ID, "last-name").send_keys(ape)
            driver.find_element(By.ID, "postal-code").send_keys(zip_code)
            driver.find_element(By.ID, "continue").click()

            # Validar mensaje
            error_web = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
            self.assertEqual(error_web, error_esperado)
            print(f"✅ Validación '{error_esperado}': PASADA")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()