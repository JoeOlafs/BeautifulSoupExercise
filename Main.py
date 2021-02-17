from bs4 import BeautifulSoup

with open('index.html','r') as html_file:
     content  = html_file.read()
     
     soup = BeautifulSoup(content, 'lxml')
     navBar = soup.find_all('div', class_='Buttons')
     for button in navBar:
          button_name = button.a.text
          print(button_name)