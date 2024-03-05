import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/finance/markets/most-active?hl=en"

# Fetch the webpage content
response = requests.get(url)
html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

activeCompany=soup.find("div", class_='Sy70mc')
activetopCompany=activeCompany.find_all("div", class_='ZvmM7')
topCompany=[]
for i in activetopCompany:
    topCompany.append(i.text)

topCompanyMargin=[]

activetopCompanyMargin=activeCompany.find_all("div", class_='JwB6zf')
for i in activetopCompanyMargin:
    topCompanyMargin.append(i.text)


currentValue=[]
currentval=activeCompany.find_all("div", class_='Bu4oXd')
for i in currentval:
    currentValue.append(i.text)

currentProgess=[]
currentprogg=activeCompany.find_all('div', class_='BAftM')
for i in currentprogg:
    currentProgess.append(i.text.split('₹'))

finalList=[]
finalList.append(f'{"Industry":<40}{'Current Value':<15}{'Progress':<15} Margin')
finalList.append('_'*80)
for i, j , k , l in zip(topCompany, currentValue,currentProgess, topCompanyMargin):
    if k[0]=='+':
        # print(f'{i} {j} {"".join(k)}, +{l}')
        finalList.append(f'{i:<50}{j:<20}{"".join(k):<20}+{l}')
    else:
        # print(f'{i} {j} {"".join(k)}, -{l}')
        finalList.append(f'{i:<50}{j:<20}{"".join(k):<20}-{l}')



def companyList(finalList):
    return finalList

company_data=companyList(finalList)
for i in company_data:
    print(i)

