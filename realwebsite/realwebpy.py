from bs4 import BeautifulSoup
import requests

unfamiliarskill=input("Enter unfamilar skills separated by a single space: ").casefold().split()
print(unfamiliarskill)

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup=BeautifulSoup(html_text, 'lxml')
jobs=soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    posted=job.find('span', class_='sim-posted').span.text
    if 'few' in posted:
        compname=job.find('h3', class_='joblist-comp-name').text.replace('  ','')
        skills=job.find('span', class_='srp-skills').text.replace('  ','')
        more_info=job.header.h2.a['href']
        flag=0
        for i in unfamiliarskill:
            if i in skills.casefold():
                flag=1
                break
        if flag==0: 
            print(f"Company Name: {compname.strip()}")
            print(f"Skills Req: {skills.strip()}")
            print(f"{posted.strip()}")
            print(f"More Info: {more_info}")
            
            print('-------------------------------------------------')