import requests
from bs4 import BeautifulSoup as bs
import pprint as pprint

ls = []
ls2 = []
ls3 = []


def get_citations_needed_count(link):
    """this function will return the number of citations needed"""
    citation_counter = []
    # find all the p tags in the div class mw-parser-output
    for index in soup.find("div", class_="mw-parser-output").find_all("p"):
        # find all the links with title "Wikipedia:Citation needed" and store them in counter list
        for all_hrefs in index.find_all('a', title="Wikipedia:Citation needed"):
            a_href = all_hrefs  # store the link in a_href

            citation_counter.append(a_href)
    print("Count of the citations = ", len(citation_counter))
    return len(citation_counter)


def get_citations_needed_report(link):
    """this function will return the report of citations needed"""
    for index in soup.find("div", class_="mw-parser-output").find_all("p"):  # find all the p tags in the div class mw-parser-output
        # find all the links with title "Wikipedia:Citation needed" and store them in counter list
        for all_hrefs in index.find_all('a', title="Wikipedia:Citation needed"):
            # print(all_hrefs.text)
            # store the text in report variable and strip the white spaces
            report = all_hrefs.parent.parent.parent.text.strip()
            # print("Report of the Citations =", report)
            pprint.pprint(report)
    return report


def get_citations_needed_by_section(links):
    """ This function takes in a list of links and subtext and returns a list of dictionaries with the title, votes, and comments """
    for index in soup.find("div", class_="mw-parser-output").find_all("p"):
        for all_hrefs in index.find_all('a', title="Wikipedia:Citation needed"):
            report = all_hrefs.parent.parent.parent.text.strip()
            ls.append(report)
            # find all the toctext tags and store them in ls2 list
            for i in soup.select('.toctext'):
                x = i.text.strip()
                ls2.append(x)
            ls3 = zip(ls, ls2)
            print(ls3)

    return ls3


url = "https://en.wikipedia.org/wiki/History_of_Mexico"
res = requests.get(url)
soup = bs(res.content, 'html.parser')

if __name__ == "__main__":
    get_citations_needed_count(url)
    get_citations_needed_report(url)
    get_citations_needed_by_section(url)
