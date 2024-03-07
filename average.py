import requests
from bs4 import BeautifulSoup

finance_news_url = "https://finance.yahoo.com/"
# Fetch the webpage content
response = requests.get(finance_news_url)
news_List=[]
avg_List=[]

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')
# Find news headlines
headlines_tags = soup.find_all('h3')
for headline in headlines_tags:
    news_List.append(headline.text)
for i in range(5):
    avg_List.append(news_List[i])
# for i in news_List:
#     print(i)

print(avg_List)


