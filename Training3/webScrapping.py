import requests
from bs4 import BeautifulSoup

# URL de la página web a scrapear
url = 'http://limpiezatotal.cc'

# Enviar una solicitud GET a la URL
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Analizar el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extraer los datos deseados (por ejemplo, todos los textos de citas)
    quotes = soup.find_all('span', class_='text')

    # Almacenar los datos en una lista
    extracted_data = [quote.get_text() for quote in quotes]

    # Imprimir los datos extraídos
    for data in extracted_data:
        print(data)
else:
    print(f"Error al acceder a la página: {response.status_code}")