import requests
import os.path as path

url = "http://127.0.0.1:7999/change_data"
files = {}
data = {    
                "number": 1,
                "login": "user",
                "password": "password",
                "manufacturer": "Ilya",
                "equipment": "",
                "analog": "",
                "type": "",
                "name": "Ilya",
                "SAP_number": "",
                "serial_number": "",
                "storage": "",
                "unit": "",
                "delivery_time": 0,
                "using_time": 0,
                "downtime": 0,
                "delivery_time_and_coefficient": 0,
                "using_in_workshop": 0,
                "price_in_rubles": 0,
                "count": 0,
                "ordered": 0,
                "min_fact": 0,
                "max_fact": 0}

request = requests.post(url=url, data=data, files=files)
print("Status:", request.headers["status"])