from bs4 import BeautifulSoup


def get_html(file):
    with open(file, "rt") as f:
        html = f.read()
        return html


def make_soup(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup


if __name__ == "__main__":
    FILE = "website.html"
    html_content = get_html(FILE)
    soup = make_soup(html_content)
    print(f"Site title tag is named: {soup.title.name}")
    print(f"The title tag text: {soup.title.string}")
    print(f"The tag with enclosed text: {soup.title}")
# Uncomment below lines to print out the raw html
# or a prettified version of the html we just parsed with BS4
# print(soup)
# print(soup.prettify())
