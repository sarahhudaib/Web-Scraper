import requests
from bs4 import BeautifulSoup
import pprint as pprint

url = "https://en.wikipedia.org/wiki/History_of_Mexico"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


def get_citations_needed_count(link):
    """this function will return the number of citations needed"""
    citation_counter = []
    for index in soup.find("div", class_="mw-parser-output").find_all("p"): # find all the p tags in the div class mw-parser-output
        for all_hrefs in index.find_all('a', title="Wikipedia:Citation needed"): # find all the links with title "Wikipedia:Citation needed" and store them in counter list 
            a_href = all_hrefs # store the link in a_href
            
            citation_counter.append(a_href)
    print ("Count of the citations = " , len(citation_counter))
    return len(citation_counter)


def get_citations_needed_report(link):
    """this function will return the report of citations needed"""
    for index in soup.find("div", class_="mw-parser-output").find_all("p"): # find all the p tags in the div class mw-parser-output
        for all_hrefs in index.find_all('a', title="Wikipedia:Citation needed"): # find all the links with title "Wikipedia:Citation needed" and store them in counter list
            # print(all_hrefs.text)
            report = all_hrefs.parent.parent.parent.text.strip()
            # print("Report of the Citations =", report)
            pprint.pprint(report)
    return report


if __name__ == "__main__":
    get_citations_needed_count(url)
    get_citations_needed_report(url)
