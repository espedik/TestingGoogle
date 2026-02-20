import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
# --- NUEVAS IMPORTACIONES PARA LA ESPERA ---
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginFallido(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://practicetestautomation.com/practice-test-login/"

    def test_error_contrasena_incorrecta(self):
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("12345_Error")
        driver.find_element(By.ID, "submit").click()

        # --- CAMBIO AQUÍ: ESPERA EXPLÍCITA ---
        # Le decimos que espere hasta 10 segundos a que el ID 'error' sea VISIBLE
        wait = WebDriverWait(driver, 10)
        error_msj = wait.until(EC.visibility_of_element_located((By.ID, "error")))
        
        # Ahora que sabemos que es visible, la validación pasará
        self.assertTrue(error_msj.is_displayed(), "El mensaje de error no se mostró")
        self.assertIn("Your password is invalid!", error_msj.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()