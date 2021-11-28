from bs4 import BeautifulSoup

with open(r'C:\Users\User\Desktop\Untitled-1.html', 'r') as hfile:
    content= hfile.read()
    
    soup=BeautifulSoup(content, 'lxml')
    course_cards=soup.find_all('div', class_='card')
    for crs in course_cards:
        name=crs.h5.text
        price=crs.a.text.split()[-1]

        print(f'{name} costs {price}')
