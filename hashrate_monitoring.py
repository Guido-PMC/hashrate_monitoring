import requests
import json
import os
class miner:
    def __init__(self, id, wallet, miner, hash):
        self.id = id
        self.wallet = wallet
        self.miner = miner
        self.hash = hash

list_miners=[]
i=0
with open('/hive-config/wallet.conf') as f:
  for line in f:
    if "0x" in line:
        if i>0:
            f2 = open('/run/hive/last_stat.json','r')
            data = json.load(f2)
            word = "total_khs"+str((i+1))
            list_miners.append(miner(i,line.split('"')[1].split(".")[0],line.split("_")[0],data["params"][word]))
            i=i+1
        if i == 0:
            f2 = open('/run/hive/last_stat.json','r')
            data = json.load(f2)
            list_miners.append(miner(i,line.split('"')[1].split(".")[0],line.split("_")[0],data["params"]["total_khs"]))
            i=i+1
hostname_stream = os.popen("hostname")
hostname = hostname_stream.read()
for x in list_miners:
    print ("Minero_ID: "+str(x.id))
    print ("Wallet: "+str(x.wallet))
    print ("Minero: "+str(x.miner))
    print ("Hashrate: "+str(x.hash))
    print("Hostname: "+str(hostname))
    url = "http://45.239.131.173:5000/wallet/"+x.wallet
    payload="{\""+str(hostname)+"\" : \""+str(x.hash)+"\"}"
    headers = {
        'Content-Type': 'application/json'
        }

    response = requests.request("POST", url, headers=headers, data=payload)
    date = os.popen("date")
    output_date = date.read()
    print("Fecha: "+str(output_date))
    print("URL a enviar data: "str(url))
    print("Payload enviado al server: "str(payload))
    print("Respuesta del server: "str(response.text))
    print("-------")
