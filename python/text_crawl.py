from os import link
from re import L
from bs4 import BeautifulSoup
import requests



def get_link(i):
    url = f"https://news.daum.net/breakingnews/society?page={i}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser').find("ul",{"class" : "list_news2 list_allnews"}).find_all("li")
    links = []
    for a in soup:
        try:
            links.append(a.find("a",{"class" : "link_thumb"})['href'])
        except:
            pass
    return links



def get_links(i):
    links = []
    for i in range(1,i):
        link = get_link(i)
        for l in link:
            links.append(l)
    return links


def get_info(html):
    content = html.find("div",{"id":"cMain"}).select("#harmonyContainer > section > p:nth-child(2)")
    title = html.find("div",{"id":"cSub"}).find("h3",{"class" : "tit_view"}).text
    date = html.find("div",{"id":"cSub"}).find("span",{"class" : "num_date"}).text
    section = html.find("ul",{"class" : "gnb_comm"}).get_attribute_list('data-category').text
    return {
        "title" : title,
        "section" : section,
        "date" : date,
        "content" : content
        }

def get_news(link):
    news = []
    for url in link:
        res = requests.get(url)
        htmls = BeautifulSoup(res.text,'html.parser')
        for html in htmls:
            job = get_info(html)
            news.append(job)
    return news



# link = get_links(3)
# print(get_news(link))

def get_text(i):
    content = []
    link = get_links(i)
    for url in link:
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser').find("div",{"id":"cMain"}).select("#harmonyContainer > section > p:nth-child(2)")
        for c in soup:
            content.append(c.text)
    return content

print(get_text(10))

            
# def get_title(i):
#     title = []
#     link = get_links(i)
#     for url in link:
#         res = requests.get(url)
#         soup = BeautifulSoup(res.text,'html.parser').find("div",{"id":"cSub"}).find("h3",{"class" : "tit_view"})
#         for t in soup:
#             title.append(t.text)
#     return title

# def get_date(i):
#     dates = []
#     link = get_links(i)
#     for url in link:
#         res = requests.get(url)
#         soup = BeautifulSoup(res.text,'html.parser').find("div",{"id":"cSub"}).find("span",{"class" : "num_date"})
#         for d in soup:
#             dates.append(d.text)          
#     return dates


# def get_section(i):
#     sec = []
#     link = get_links(i)
#     for url in link:
#         res = requests.get(url)
#         soup = BeautifulSoup(res.text,'html.parser').find("ul",{"class" : "gnb_comm"}).get_attribute_list('data-category')
#         for s in soup:
#             sec.append(s)
#     return sec


# def get_dic(i):
#     text = {}
#     dates = get_date(i); title = get_title(i); content = get_text(i); section = get_section(i)

#     return text

# get_dic(5)