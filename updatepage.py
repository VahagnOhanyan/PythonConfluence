import requests
from requests.auth import HTTPBasicAuth


def updatepage(value, version):
    payload = {
        "version": {
            "number": version
        },
        "title": "My new title",
        "type": "page",
        "body": {
            "storage": {
                "value": value,
                "representation": "storage"
            }
        }
    }

    requests.put(
        'https://vahagn2908.atlassian.net/wiki/rest/api/content/65630?expand=body.storage,version',
        auth=HTTPBasicAuth('ohanyanvahagn7@gmail.com', 'ATATT3xFfGF0KLdqlPepMywnMYK8-'
                                                       'ctKdo6gm1xgDo_ESMK7XAeX2GAHYuV_atE9ec6eDlzNrYPJ8Z9Vw_'
                                                       'Kv08rt0UU9W3IF7ETXwmsaTD7gJyYJsw08hSW4WnQGs-'
                                                       'EFDldRpui1aDl7tOfyrE4xrUa_3Sg7XX21uqNcW9Dcs9LNaINRgaZ-'
                                                       'bc0=641B217C'),
        json=payload)
