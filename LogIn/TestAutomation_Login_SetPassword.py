import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginExitoso(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(7)
        self.url = "https://practicetestautomation.com/practice-test-login/"

    def test_valida_acceso_correcto(self):
        driver = self.driver
        driver.get(self.url)

        # 1. Ingresar credenciales válidas
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()

        # 2. Validaciones de Dashboard
        self.assertIn("logged-in-successfully", driver.current_url)
        
        mensaje = driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(mensaje, "Logged In Successfully")
        
        boton_logout = driver.find_element(By.LINK_TEXT, "Log out")
        self.assertTrue(boton_logout.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()