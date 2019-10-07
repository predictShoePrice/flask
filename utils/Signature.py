import hashlib
from urllib.parse import urlparse

PublicKey = 'MwJpto3h7ppPD1hauZHMA_7Jdre1LRRnpkvqOsX2'


def _verfy_ac(params):
    items = params.items()
    print(items)
    # 请求参数串
    items.sort()
    # 将参数串排序
    params_data = ""
    private_key = 'ct49QLfm8_Ntn_Zixn-IFpBHrELZZ1lT6D07fj32_FvkDvzLl-wtMyE6_Pwg9HrC'
    for key, value in items:
        params_data = params_data + str(key) + str(value)
        params_data = params_data + private_key
    sign = hashlib.sha1()
    sign.update(params_data)
    signature = sign.hexdigest()
    # 生成的Signature值
    return signature


params = {
    "Action": "CreateUHostInstance",
    "Region": "cn-bj2",
    "Zone": "cn-bj2-04",
    "ImageId": "f43736e1-65a5-4bea-ad2e-8a46e18883c2",
    "CPU": 2,
    "Memory": 2048,
    "DiskSpace": 10,
    "LoginMode": "Password",
    "Password": "VUNsb3VkLmNu",
    "Name": "Host01",
    "ChargeType": "Month",
    "Quantity": 1,
    "PublicKey": "MwJpto3h7ppPD1hauZHMA_7Jdre1LRRnpkvqOsX2"
}

print(_verfy_ac(params))