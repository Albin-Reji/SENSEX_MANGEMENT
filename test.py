import requests
from bs4 import BeautifulSoup


# URL of the Sensex page
url = "https://www.msn.com/en-in/money/watchlist?id=ahkucw&tab=Markets&ocid=winp2fptaskbarhover&cvid=58bf0751d3204858a9531cb31c53c94b&ei=9"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

current_percent_value=soup.find('div', class_=" color_red-DS-EntryPoint1-1 price_display-DS-EntryPoint1-1")
print(current_percent_value)

