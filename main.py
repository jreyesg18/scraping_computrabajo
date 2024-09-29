import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Solicitar al usuario que ingrese la palabra clave
keyword = input("Ingrese la palabra clave para buscar en los títulos de trabajo: ")

# Abrir la página
url = "https://cl.computrabajo.com/empleos-en-rmetropolitana"
driver = webdriver.Chrome()

driver.get(url)

# Lista para almacenar los resultados
job_results = []

try:
    while True:
        # Esperar a que los trabajos estén cargados
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.js-o-link.fc_base"))
        )

        # Encontrar todos los elementos <a> con la clase js-o-link fc_base
        job_elements = driver.find_elements(By.CSS_SELECTOR, "a.js-o-link.fc_base")

        # Extraer el título y el enlace de cada trabajo
        for job_element in job_elements:
            title = job_element.text  # Texto del título del trabajo
            link = job_element.get_attribute("href")  # Enlace de la oferta

            # Filtrar por palabra clave en el título
            if keyword.lower() in title.lower():  # Comparación insensible a mayúsculas
                # Crear un diccionario con los datos del trabajo
                job_data = {
                    "title": title,
                    "link": link
                }

                # Agregar el diccionario a la lista
                job_results.append(job_data)

        # Hacer scroll hacia abajo para asegurarnos de que el botón "Siguiente" sea visible
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Pausa breve para asegurarnos de que la página se cargue completamente

        # Intentar ir a la siguiente página
        try:
            # Usar un XPATH para seleccionar el botón por su atributo title y data-path
            next_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@title='Siguiente' and contains(@data-path, 'p=')]"))
            )
            next_button.click()  # Hacer clic en el botón de "Siguiente"
            time.sleep(3)  # Esperar a que se carguen los nuevos trabajos

        except Exception as e:
            print("No se pudo encontrar el botón de 'Siguiente' o no hay más páginas.")
            break  # Si no hay más páginas, salir del ciclo

except Exception as e:
    print(f"Error: {e}")

finally:
    # Cerrar el navegador
    driver.quit()

# Guardar los resultados en un archivo JSON
with open("job_offers.json", "w", encoding="utf-8") as f:
    json.dump(job_results, f, ensure_ascii=False, indent=4)

print("Datos guardados en job_offers.json")

