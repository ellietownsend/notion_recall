from bs4 import BeautifulSoup
import html.parser


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    section = {}
    headers = soup.find_all("h2")
    for header in headers:
        title = header.get_text(" ", strip=True)
        content = []

        for sibiling in header.find_next_siblings():
            if sibiling.name == "h2":
                break

            text = sibiling.get_text("", strip = True)
            if text:
                content.append(text)

        section[title] = content
        

    return section

    
