from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Abrir la página
url = "https://www.trabajando.cl/trabajo-empleo/?ubicacion=las+condes&comuna=324"
driver = webdriver.Chrome()

driver.get(url)

# Lista para almacenar los resultados
job_results = []

# Esperar a que el dropdown de "Fecha" esté presente y hacer clic para desplegarlo
dropdown_fecha = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.field_select_links.small.open"))
)
dropdown_fecha.click()

# Esperar a que las opciones del dropdown estén visibles y seleccionar "Últimos 3 días"
opcion_ultimos_3_dias = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@data-path='?pubdate=3']"))
)
opcion_ultimos_3_dias.click()

# Aquí puedes agregar la lógica para esperar los resultados y extraer información de las ofertas de trabajo

# Cerrar el navegador
driver.quit()
