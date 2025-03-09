from selenium import webdriver
from PIL import Image

# Configurar el navegador sin interfaz gráfica
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=6920,6080")  # Resolución alta

driver = webdriver.Chrome(options=options)
driver.get("C:\Users\diego\Downloads\Hoja1.html")  # Ruta del HTML local

# Capturar la pantalla completa
screenshot = "tabla.png"
driver.save_screenshot(screenshot)
driver.quit()

# Recortar la imagen para enfocarse en la tabla
img = Image.open(screenshot)
img.show()  # Ver la imagen antes de guardar
img.save("tabla_alta_calidad.png", dpi=(300, 300))  # Guardar en alta calidad
