from http import client
from turtle import color, tilt
from urllib import request
from tilt import*
import requests
from pymongo import*

class tiltData():
    
    def consumirApi(self):
        
        url="https://api.brewfather.app/v1/batches/tBk0UOiUNrzxepWDduHKSodPVnn37H/readings"
        
        username='AA8NmS7aMyQEYUnV9jtxpKxaQ3z1'
        password='io5x5drLPL3JmHdZPaJJLf7wMSubNhBfD3LpwmDjHRuZak4cPK7sOqFpEkqqMy8u'
        
        resp=requests.get(url,auth=(username,password))
        
        if resp.status_code==200:
            resp_json=resp.json()
            for i in resp_json:
                color=i['id']
                sg=i['sg']
                time=i['time']
                
                dict={"color":color,"sg":sg,"time":time}
                
                mongo_url="mongodb+srv://admin:12345@miprimercluster.ityon.mongodb.net/?retryWrites=true&w=majority"
        
                client=MongoClient(mongo_url)
        
                db=client['tiltData']
                collection=db['tilts']
                   
                collection.insert_one(dict)
                print(dict)
                        
               
                
                
                    
        else:
            print(resp.content)
            
        
if __name__=='__main__':
    ip=tiltData()
    ip.consumirApi()
    
        
    