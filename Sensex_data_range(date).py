import requests
from bs4 import BeautifulSoup
import lxml


# URL of the Sensex page
url = "https://www.google.com/finance/quote/SENSEX:INDEXBOM?hl=en&window=1M"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')
span_tag = soup.find('span', class_='NydbP')

# Extract the percentage value from the span tag

print("Percentage Value:", span_tag.text)

