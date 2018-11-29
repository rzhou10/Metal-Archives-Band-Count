import json
import csv
from selenium import webdriver

#writes to csv
def writeToCSV(count, fileName):
    try:
        with open("csv/" + fileName + ".csv", "w+", newline='') as csv_file:
            write = csv.writer(csv_file)
            for key, value in count.items():
                write.writerow([key, value])
    except Exception as e:
        print(e)

#counts based on criteria from main
def countBands(fileName, tagId):
    with open("json/" + fileName + ".json") as f:
        data = json.load(f)

    count = {}

    #find specific text to extract.
    for i in range(len(data)):
        driver = webdriver.Chrome()
        driver.get("https://www.metal-archives.com/lists/" + data[i]["code"])
        content = driver.find_element_by_id(tagId).text

        #get the count
        bandCount = content.split(" ")
        if len(bandCount) > 1:
            count[data[i]["name"]] = bandCount[5]
            
        driver.close()

    print("Finished all items.")
    writeToCSV(count, fileName)