from bs4 import BeautifulSoup
import html.parser


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    headers = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    for header in headers:
        print (header.get_text(strip=True))
