import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/History_of_Mexico"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


def get_citations_needed_count(link):
    """this function will return the number of citations needed"""
    counter = []
    for index in soup.find("div", class_="mw-parser-output").find_all("p"):
        for wrapper in index.find_all('a', title="Wikipedia:Citation needed"):
            a_href = wrapper
            counter.append(a_href)

    print("How many count citations? \nCount of the Citations =", len(counter))
    return len(counter)


def get_citations_needed_report(link):
    """this function will return the report of citations needed"""
    for index in soup.find("div", class_="mw-parser-output").find_all("p"):
        for wrapper in index.find_all('a', title="Wikipedia:Citation needed"):
            report = wrapper.parent.parent.parent.text.strip()
            print("\n", "*"*100, "\n", report, "\n", "*"*100, "\n")
    return report


if __name__ == "__main__":
    get_citations_needed_count(url)
    get_citations_needed_report(url)
