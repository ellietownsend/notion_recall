from bs4 import BeautifulSoup


def parse_html(html: str):
    soup = BeautifulSoup(html, "html.parser")

    sections = []
    current = None

    for element in soup.body.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        if current:
            sections.append(current)

        current = {
            "title": element.get_text(strip=True),
            "level": int(element.name[1]),
            "content": [],
        }

        for sibling in element.find_next_siblings():
            if sibling.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
                break

            current["content"].append(str(sibling))

    if current:
        sections.append(current)

    return sections