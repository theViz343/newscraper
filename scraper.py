import requests
from bs4 import BeautifulSoup
def protected_get(URL):
    resp=requests.get(URL,timeout=2)
    if resp.status_code==404:
        return None
    return resp
def fetch_indiatoday():
    resp = protected_get("https://www.indiatoday.in/news.html")
    newslist=[]
    # print("YES")
    # print(resp.headers['Content-Type'])
    raw_html = resp.content
    html = BeautifulSoup(raw_html, 'html.parser')
    for hl in html.find_all('h3', class_='news-page-feature'):
        newslist.append(hl.a.text)
    return newslist
def fetch_ndtv():
    resp=protected_get('https://www.ndtv.com/latest?pfrom=home-mainnavgation')
    newslist=[]
    raw_html=resp.content
    html=BeautifulSoup(raw_html,'html.parser')
    for div in html.find_all('div',class_='nstory_header'):
        for tag in div.children:
            newslist.append(tag.text.strip())
    return newslist
print(fetch_indiatoday())
print(fetch_ndtv())
