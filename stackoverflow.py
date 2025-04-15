import requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}


url = 'https://stackoverflow.com/questions'
respuesta = requests.get(url, headers=headers)
soup = BeautifulSoup(respuesta.text)


preguntas = soup.find(id="questions") 
lista_de_preguntas = preguntas.find_all('div', class_="s-post-summary") 

for pregunta in lista_de_preguntas:
  t_pregunta = pregunta.find('h3').text 
  descripcion_pregunta = pregunta.find(class_= 's-post-summary--content-excerpt').text 
  des_pregunta = descripcion_pregunta.replace('\n', '').replace('\r', '') 
  print (t_pregunta)
  print (des_pregunta)
#print ()

