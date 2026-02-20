import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. DICCIONARIO DE TEST CASES (Datos Dinámicos)
test_cases_registro = {
    "TC-01": {
        "nombre": "Campos Vacíos",
        "datos": {"user": "", "pass": ""},
        "esperado": "invalid", # Palabra clave que debe aparecer en el error
    },
    "TC-02": {
        "nombre": "Login Exitoso",
        "datos": {"user": "tomsmith", "pass": "SuperSecretPassword!"},
        "esperado": "You logged into a secure area!",
    }
}

class TestFormularioCompleto(unittest.TestCase):

    def setUp(self):
        """Preparamos el entorno antes de cada prueba"""
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.driver.implicitly_wait(5) # Espera técnica para que carguen los elementos

    def test_ejecutar_matriz_pruebas(self):
        """Corremos todos los casos del diccionario dinámicamente"""
        driver = self.driver

        for tc_id, info in test_cases_registro.items():
            # Usamos subTest para que si un caso falla, el robot siga con el siguiente
            with self.subTest(msg=f"Ejecutando {tc_id}: {info['nombre']}"):
                
                # Acciones del Robot
                user_input = driver.find_element(By.ID, "username")
                pass_input = driver.find_element(By.ID, "password")
                btn_login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

                # Limpiar campos antes de escribir (por si quedó algo de la iteración anterior)
                user_input.clear()
                pass_input.clear()

                # Enviar datos
                user_input.send_keys(info['datos']['user'])
                pass_input.send_keys(info['datos']['pass'])
                btn_login.click()

                # VALIDACIÓN (Asserts y Mensajes de error)
                # Buscamos el elemento que contiene el mensaje (en este sitio es id="flash")
                mensaje_real = driver.find_element(By.ID, "flash").text
                
                print(f"Verificando {tc_id}: Se esperaba '{info['esperado']}'")
                
                # Comprobamos que el texto esperado esté contenido en el mensaje real
                self.assertIn(info['esperado'], mensaje_real)

    def tearDown(self):
        """Limpiamos el entorno cerrando el navegador"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()