import getfile
import getpage
import updatepage
import json

if __name__ == "__main__":
    fileContent = getfile.getfile()
    pageContent = getpage.getpage()

with open('resources/file.txt', "w", encoding="utf8") as file:
    file.truncate(0)
    file.write(fileContent)
    file.close()
with open('resources/page.json', "w") as page:
    content = json.dumps(pageContent)
    page.truncate(0)
    page.write(content)
    page.close()
with open('resources/file.txt', "r", encoding="utf8") as file:
    f = file.readlines()
    value = ""
    for x in f:
        value = value + x
with open('resources/page.json', "r", encoding="utf8") as page:
    p = json.load(page)
    version = p["version"]
    versionNum = version['number']
    versionNum = versionNum + 1
    versionStr = str(versionNum)
updatepage.updatepage(value, versionStr)
