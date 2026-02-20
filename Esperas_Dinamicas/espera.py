"""
EJERCICIO 3: AUTOMATIZACIÓN DE ESPERAS DINÁMICAS
------------------------------------------------
ESCENARIO: 
Al cargar la página y presionar 'Start', aparece una barra de carga. 
El mensaje final ("Hello World!") no está presente en el DOM o no es visible 
al inicio, sino que tarda unos segundos en renderizarse.

OBJETIVO TÉCNICO:
1. Implementar 'Explicit Wait' (Esperas Explícitas) para sincronizar el script 
   con la velocidad de la aplicación.
2. Evitar el uso de 'time.sleep()', permitiendo que la prueba continúe 
   tan pronto como el elemento aparezca (optimización de tiempo).
3. Utilizar Expected Conditions (EC) para validar la visibilidad del elemento.
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestEsperasDinamicas(unittest.TestCase):

    def setUp(self):
        # Configuración del navegador
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    def test_espera_explicit_wait(self):
        driver = self.driver

        # Paso 1: Localizar el botón que inicia la carga dinámica
        boton_start = driver.find_element(By.CSS_SELECTOR, "#start button")
        boton_start.click()

        # Paso 2: Configurar la espera explícita
        # Le decimos al driver que tenga una paciencia máxima de 10 segundos
        wait = WebDriverWait(driver, 10)

        # Paso 3: Definir la condición esperada
        # El script se detiene aquí hasta que el ID 'finish' sea visible en pantalla
        elemento_oculto = wait.until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )

        # Paso 4: Validación final (Assert)
        # Una vez que la espera termina con éxito, verificamos el contenido del texto
        self.assertEqual(elemento_oculto.text, "Hello World!")
        print("Éxito: El elemento se detectó dinámicamente.")

    def tearDown(self):
        # Cierre de sesión y limpieza de recursos
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()