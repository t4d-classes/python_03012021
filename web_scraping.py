
import requests
import re

web_sites = [
    "https://www.microsoft.com",
    "https://www.yahoo.com",
    "https://www.intuit.com",
    "https://www.oracle.com",
    "https://www.amazon.com"
]

# web_sites = [
#     "https://finance.yahoo.com/quote/GME?p=GME&.tsrc=fin-srch"
# ]

# data-reactid="50">132.35</span>
# r = re.compile(r'data-reactid="50">(.*?)</span>', re.MULTILINE)
r = re.compile(r'href=["\'](.*?)["\']', re.MULTILINE)

for web_site in web_sites:
    response = requests.get(web_site)
    content = response.text
    matches = r.findall(content)
    print(matches)

    # with open("gme_price.txt", "a") as price_file:
    #     price_file.write(gme_price + "\n")