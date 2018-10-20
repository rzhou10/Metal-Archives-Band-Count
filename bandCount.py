import json
import re
import csv
from requests_html import HTMLSession

with open("codes.json") as f:
    data = json.load(f)

count = {}

session = HTMLSession()

#find specific text to extract.
for i in range(len(data)):
    page = session.get("https://www.metal-archives.com/lists/" + data[i]["code"])
    page.html.render()

    contentStr = page.html.search("{} entries")[0]
    noComma = contentStr.replace(",", "")
    numArr = re.findall(r"\d+", noComma)
    count[data[i]["name"]] = numArr[len(numArr) - 1]

print("Finished all countries.")

countParsed = json.loads(count)
countData = countParsed[0]
countedData = open("/bandCount/bandCount.csv", "w")
csvWriter = csv.writer(countedData)

header = countData[0].keys()
csvWriter.writerow(header)

for cnt in countData:
    csvWriter.writerow(cnt.values())

countData.close()