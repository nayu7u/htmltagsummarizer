from urllib import request
from bs4 import BeautifulSoup
from time import sleep
import json

url = "https://reference.hyper-text.org/html5/"

response = request.urlopen(url)
soup = BeautifulSoup(response, features="html.parser")
response.close

dl = soup.find("dl", class_="element-alphabet-list")
li_elms = dl.find_all("li")

elems_d = {}
for li in li_elms:
    elem_name = li.a.text.split()[0]
    elems_d[elem_name] = "https://reference.hyper-text.org" + li.a.get("href")

elems_desc_d = {}
for elem_name, elem_url in elems_d.items():
    sleep(0.5)

    print(elem_url)
    res = request.urlopen(elem_url)
    soup = BeautifulSoup(res, features="html.parser")
    res.close

    # <div class="module-element-description module-reference-section">
    # <div class="module-element-text module-reference-section" id="detail">
    description = soup.select(".module-element-description.module-reference-section")
    detail_text = soup.find("div", id="detail")

    descrp = []
    for x in description[0].find_all("p"):
        try:
            if x.attrs["class"] == ["module-angle-down-btn"]:
                continue
        except:
            descrp.append(x.text)

    if detail_text is not None:
        detail = [x.text for x in detail_text.find_all("p")]
    else:
        detail = []

    elems_desc_d[elem_name] = descrp + detail

with open("./data.json", "w") as f:
    json.dump(elems_desc_d, f, indent=4)
