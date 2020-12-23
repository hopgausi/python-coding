import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'user-agent': 'hopgausi/1.0'
}
r = requests.get('https://lvngd.com/', headers=headers)

data = r.content
soup = BeautifulSoup(data, "html.parser")

data_sections = soup.findAll(class_='section-lg')

service_heading = []
blog_links = []
blog_titles = []
for data_section in data_sections[:-1]:
    service_heading.append(data_section.find_all(class_='services-heading'))
    blog_links.append(data_section.find_all('a', class_='related-blog-link'))
    blog_titles.append(data_section.find_all('a', class_='related-blog-link'))

links_to_blog = []
titles_to_blog = []
services = []
for i in range(len(service_heading)):
    services_provided = [service[0].text for service in service_heading][i]
    blog_service_links = ['https://lvngd.com/' + link[i]['href'] for link in blog_links]
    blog_service_titles = [title[i].text for title in blog_titles]
    links_to_blog.append(blog_service_links)
    titles_to_blog.append(blog_service_titles)
    services.append(services_provided)

df = pd.DataFrame({
    "Services": services,
    "Blog Links": links_to_blog,
    "Blog Titles": titles_to_blog,
}, )
df.to_csv('lvngd.csv',index=False)
