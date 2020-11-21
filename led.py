#import RP1.GPIO as GPIO
from EmulatorGUI import GPIO
import time
import requests
import json
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(3, GPIO.IN)

while True:
    if GPIO.input(3):
        GPIO.output(7,True)
        headers = {"Content-Type":"application/json","access_token":"access_token_f3d9461c68fd208dae3385184d4fbff20ce4ed61"}
       
       
       
       
       
       
       
       
        payload = {"name": "6",
         "horaInicio": "07:15",
         "horaFin": "06:00",
         "horasXsemana": "48",
         "descripcion": "Prueba con el profe carlos "}
        datajson = json.dumps(payload)
        url= "https://3d5ad842360a.ngrok.io/api/controlemployees.horario"
        response = requests.request("POST",url,data=datajson, headers=headers)
        if response.status_code == 200:
           print('si entro ') 
           pass
        
    else:
        GPIO.output(7,False)


     

       
        
        
 
   