# Beautiful soup is using to scarp details from naukari website
import bs4
# beautiful-soup imported
import requests
# requests imported
title = []
summary = []
location = []
company = []
experienceList = []

res = requests.get('https://www.indeed.co.in/jobs?q=data+science&l=India')
# print(res.text)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(soup)
for t in soup.select(".jobtitle.turnstileLink"):
    title.append(t.text.lstrip())
for s in soup.select(".summary"):
    summary.append(s.text.lstrip())
for l in soup.select(".location"):
    location.append(l.text.lstrip())
for c in soup.select(".company"):
    company.append(c.text.lstrip())
# for e in soup.select(".experienceList"):
#     experienceList.append(e.text.lstrip())
print(title[3])
print(summary[3])
print(location[3])
print(company[3])
# print(experienceList[3])

