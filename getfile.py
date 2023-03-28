import requests


def getfile():
    url = "https://raw.githubusercontent.com/VahagnOhanyan/SpringJavaFxApplication/main/META-INF/MANIFEST.MF"

    payload = ""
    headers = {
        'Authorization': '',
        'Cookie': ''
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text
    return data
