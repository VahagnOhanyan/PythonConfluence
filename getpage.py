import json
import requests


def getpage():
    response = requests.get(
        'https://vahagn2908.atlassian.net/wiki/rest/api/content/65630?expand=body.storage,version',
        auth=('ohanyanvahagn7@gmail.com',
              'ATATT3xFfGF0KLdqlPepMywnMYK8'
              '-ctKdo6gm1xgDo_ESMK7XAeX2GAHYuV_atE9ec6eDlzNrYPJ8Z9Vw_Kv08rt0UU9W3IF7ETXwmsaTD7gJyYJsw08hSW4WnQGs'
              '-EFDldRpui1aDl7tOfyrE4xrUa_3Sg7XX21uqNcW9Dcs9LNaINRgaZ-bc0=641B217C'), )

    data = json.loads(response.text)
    return data
