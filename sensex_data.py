import requests
from bs4 import BeautifulSoup
from datetime import datetime


date_object = datetime.now()
current_date = date_object.strftime("%A, %B %d, %Y")


# URL of the Sensex page
url = "https://g.co/finance/SENSEX:INDEXBOM"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'lxml')

# Find the element containing the Sensex value
sensex_value = soup.find("div", class_="YMlKec fxKbKc")

# Extract the text containing the Sensex value
sensex_value_text = sensex_value.text.strip()

div_element = soup.find("div", class_="ln0Gqe")
current_Sensex_value=div_element.text
# print(f'SENSEX: {current_Sensex_value}')

current_percent=soup.find('div', class_='JwB6zf').text
current_percent_value=float(current_percent.split(sep='%')[0])

print(current_percent_value)


