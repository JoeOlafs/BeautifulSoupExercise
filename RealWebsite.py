from bs4 import BeautifulSoup
import requests
import datetime

html_text = requests.get('https://github.com/JoeOlafs').text
#content = html_text.read()
soup = BeautifulSoup(html_text, 'lxml')
days_contribution = soup.find_all('rect', class_='ContributionCalendar-day')
for date in days_contribution:
     print(date)

###########################
#got a bit ahead of myself, part of Twitter bot challenge to finish this
###########################