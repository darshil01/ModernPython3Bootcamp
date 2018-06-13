from bs4 import BeautifulSoup
import requests
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_data.csv", "w", newline='') as f:
    writer = writer(f)
    writer.writerow(["Title", "Link", "Date"])

    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag['href']
        date = article.find("time")['datetime']

        writer.writerow([title, url, date.strip("\n")])
        # print(title, url, date)