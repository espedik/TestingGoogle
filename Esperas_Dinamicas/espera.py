import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestEsperasDinamicas(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() # Asegúrate de tener el driver instalado
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    def test_espera_boton_dinamico(self):
        driver = self.driver
        
        # Localizar el botón de inicio y hacer clic
        boton_start = driver.find_element(By.CSS_SELECTOR, "#start button")
        boton_start.click()

        # IMPLEMENTACIÓN DE EXPLICIT WAIT
        # Esperamos hasta 10 segundos a que el elemento con texto "Hello World!" sea visible
        espera = WebDriverWait(driver, 10)
        elemento_final = espera.until(
            EC.visibility_of_element_element_located((By.ID, "finish"))
        )

        # Validación
        self.assertTrue(elemento_final.is_displayed())
        self.assertEqual(elemento_final.text, "Hello World!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()