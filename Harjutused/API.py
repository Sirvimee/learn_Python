import requests
"""
Loo funktsioon authenticated_get(url: str, username: str, password: str), mis võtab parameetrina URL-i (url),
kasutajanime (username) ja parooli (password). Funktsioon peaks tegema autentseeritud GET päringu määratud URL-ile,
kasutades antud kasutajanime ja parooli. Funktsioon tagastab päringu vastuse objekti.
"""
def authenticated_get(url: str, username: str, password: str):
    response = requests.get(url, auth=(username, password))
    return response

print(authenticated_get("https://cs.taltech.ee/services/ex14/httpbin-org/basic-auth/user/pass", "user", "pass"))


"""
Loo funktsioon send_options_request(url: str), mis võtab parameetrina URL-i (url). See funktsioon teeb OPTIONS 
päringu määratud URL-ile ja hangib teabe, millised meetodid ja omadused on sellel URL-il lubatud. 
Funktsioon tagastab päringu vastuse headeri.
"""
def send_options_request(url: str):
    response = requests.options(url)
    return response.headers

print(send_options_request("https://cs.taltech.ee/services/ex14/httpbin-org/get")['Access-Control-Allow-Methods'])
print(send_options_request("https://cs.taltech.ee/services/ex14/httpbin-org/get")['Content-Type'])


"""
Loo funktsioon update_data(url: str, new_data: dict), mis võtab parameetriteks URL-i ja sõnastiku new_data. 
See funktsioon peaks tegema PATCH päringu määratud URL-ile new_data-ga, et uuendada konkreetset andmete kirjet. 
Funktsioon tagastab päringu vastuse objekti.
"""
import requests
import json


def update_data(url: str, new_data: dict):
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(new_data)
    response = requests.patch(url, data=json_data, headers=headers)
    return response

print(update_data("https://cs.taltech.ee/services/ex14/httpbin-org/patch", {"name": "Toomas", "age": 100}))


"""
Loo funktsioon get_and_parse_json(url: str), mis võtab parameetrina URL-i (url) ja teeb GET päringu määratud URL-ile. 
Funktsioon peaks pärast päringu tegemist parsima vastuse JSON-objektiks ja tagastama selle.
"""
import requests

def get_and_parse_json(url: str):
    response = requests.get(url)
    json_response = response.json()
    return json_response

print(get_and_parse_json("https://cs.taltech.ee/services/ex14/httpbin-org/get")['headers']['Accept-Encoding'])


"""
Loo funktsioon fetch_xml(url: str), mis võtab parameetrina URL-i (url). See funktsioon teeb GET päringu määratud URL-ile, 
et hankida XML-dokument. Funktsioon peaks tagastama päringu vastuse XML-dokumendina tekst formaadis.
"""
import requests

def fetch_xml(url: str):
    response = requests.get(url)
    response = response.text
    return response

print(fetch_xml("https://cs.taltech.ee/services/ex14/httpbin-org/xml"))


"""
Loo funktsioon delete_data(url: str), mis võtab parameetriteks URL-i. See funktsioon peaks tegema DELETE päringu 
määratud URL-ile, et kustutada konkreetne andmete kirje. Funktsioon tagastab päringu vastuse staatus koodi.
"""
import requests

def delete_data(url: str):
    response = requests.delete(url)
    return response.status_code

print(delete_data("https://cs.taltech.ee/services/ex14/httpbin-org/delete"))


"""
Loo funktsioon send_data(api_url: str, data: dict), mis võtab parameetriteks API url ja sõnastiku data. Funktsioon 
peaks tegema POST päringu API URL-ile antud andmetega ja tagastama json vastuse.
"""
import requests
import json

def send_data(url: str, data: dict):
    json_data = json.dumps(data)
    response = requests.post(url, data=json_data)
    return response.json()

response = send_data("https://cs.taltech.ee/services/ex14/httpbin-org/post", {"name": "Toomas", "age": 100})

user_agent = response['json']
print(user_agent)


"""
Loo funktsioon safe_fetch(url: str), mis võtab parameetriks URL-i. See funktsioon peaks tegema GET päringu määratud 
URL-ile. Erinevalt lihtsast GET päringust, sisaldab see funktsioon veatöötlust, et käsitleda erinevaid võimalikke vigu, 
nagu HTTP veakoodid, ühenduse probleemid või ajaületus. Funktsioon tagastab päringu vastuse staatus koodi või veateate.
"""
import requests

def safe_fetch(url: str):
    try:
        response = requests.get(url, timeout=10)  # Määratud ajaületus (timeout)
        response.raise_for_status()  # Tõstab erandi, kui päring ebaõnnestub (nt veakoodiga)
        return response.status_code  # Tagastame päringu vastuse staatuse koodi
    except requests.exceptions.Timeout as e:
        print(f"Aeg ületatud: {e}")
        return "Timeout Error"
    except requests.exceptions.RequestException as e:
        print(f"Viga päringu tegemisel: {e}")
        return "Request Error"

print(safe_fetch("https://cs.taltech.ee/services/ex14/httpbin-org/status/200"))


"""
Loo funktsioon put_data(url: str, data: dict), mis võtab parameetrina URL-i (url) ja sõnastiku data. See funktsioon 
teeb PUT päringu määratud URL-ile, saates kaasa antud andmed. Funktsioon peaks pärast päringu tegemist parsima vastuse 
JSON-objektiks ja tagastama selle.
"""
import requests
import json

def put_data(url: str, data: dict):
    json_data = json.dumps(data)
    response = requests.put(url, data=json_data)
    return response.json()

print(put_data("https://cs.taltech.ee/services/ex14/httpbin-org/put", {"Nimi": "Ago"})['data'])