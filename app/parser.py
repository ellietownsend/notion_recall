from bs4 import BeautifulSoup
import html.parser


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    section = {}
    headers = soup.find_all("h2")
    for header in headers:
        next_siblings = header.find_next_siblings()
        section[header.get_text(" ", strip=True)] = next_siblings
        

    return section

    
