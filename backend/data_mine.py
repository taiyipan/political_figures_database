import requests
import json
# get json from url, output as json file
def data_mine_api(url: str, api_key: dict, fname: str) -> bool:
    # make requests, obtain response
    print('Requesting from', url)
    response = requests.get(url, headers = api_key)
    # normal flow, download data, output to json file
    if response.status_code == 200:
        print('Success', response.status_code)
        data = response.json()
        if data['status'] == 'ERROR':
            print('Data source exhausted, ending data mining')
            return False
        try:
            with open(fname, 'w', encoding = 'utf-8') as f:
                json.dump(data, f, ensure_ascii = False, indent = 4)
        except IOError:
            print(fname, "couldn't be created.")
        finally:
            return True
    # errors
    elif response.status_code == 400:
        print('Bad Request', response.status_code)
    elif response.status_code == 403:
        print('Forbidden', response.status_code)
    elif response.status_code == 404:
        print('Not Found', response.status_code)
    elif response.status_code == 406:
        print('Not Acceptable', response.status_code)
    elif response.status_code == 500:
        print('Internal Server Error', response.status_code)
    elif response.status_code == 503:
        print('Service Unavailable', response.status_code)
    return False
