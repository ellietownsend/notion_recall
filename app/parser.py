from bs4 import BeautifulSoup
import html.parser


def parse_html(html):
    print(html)
    filehandle = open(html)
    print(filehandle)
    # soup = BeautifulSoup(html, "html.parser")
    # print(soup.prettify())