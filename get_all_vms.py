import requests
import time
import json
import sys
# import global_variable as gfile

uim_credentials = ("brcmltd\\tk029975", "9347845356aA******")
base_url = r"https://cloudportal.broadcom.net/api/vms"
headers = {"Authorization": "Bearer 38377c9bc6612337cc48d55928548488"}
host_ids = {}
def test_get_vms():
    payload = \
        {
            'expand': 'resources',
            'attributes': 'name'
        }
    #response = requests.get("{}?".format(base_url), params=payload, headers=headers)
    response = requests.get("{}?".format(base_url), params=payload, auth = uim_credentials)
    print("\nResponse URL is :", response.url)
    print("\nResponse Code is : ", response.status_code)
    assert response.status_code == 200
    res_dict = response.json() # response dictionary with all vm details
    #print(res_dict)
    for key, value in res_dict.items():
        if key == 'resources':
            for key1 in value:
                #print(key1)
                for key2, value2 in key1.items():
                    if key2.startswith("href"):
                        continue
                    # print(key2, '-->', value2)
                    if key2.startswith("name"):
                        host = value2
                        # print(value2)
                    if key2.startswith("id"):
                        id = value2
                        # print(value2)
                    host_ids[host] = value2

def take_vm_snapshot():
    data = \
        {

            "action": "take snapshot",
            "snap_name": "CleanImage"
        }
    headers = {'Accept': '*/*','Content-Type' : 'text/plain', 'Content-Type': 'application/json'}
    host = (input("enter host name to take snapshot : ")).strip()
    vm_id = host_ids[host]
    print("Snapshot vm id is : ",vm_id, "for host : ",host)

    response = requests.post("{}/{}".format(base_url,vm_id), json=data, auth = uim_credentials,headers = headers)


    print("\nResponse URL is :", response.url)
    print("\nResponse Code is : ", response.status_code)
    assert response.status_code == 200
    res = response.json()
    print(res)

def revert_vm_snapshot():
    time.sleep(5)
    data = \
        {
            "action": "revert snapshot",
            "snapshot_uuid": "CleanImage"
        }
    headers = {'Accept': '*/*','Content-Type' : 'text/plain', 'Content-Type': 'application/json'}
    host = (input("enter host name to revert snapshot : ")).strip()
    print(host)
    vm_id = host_ids[host]
    print("Snapshot vm id is : ",vm_id, "for host : ",host)

    response = requests.post("{}/{}".format(base_url,vm_id), json=data, auth = uim_credentials,headers = headers)


    print("\nResponse URL is :", response.url)
    print("\nResponse Code is : ", response.status_code)
    assert response.status_code == 200
    res = response.json()
    print(res)

test_get_vms()
print(host_ids)
#take_vm_snapshot()
revert_vm_snapshot()
