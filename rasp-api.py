from flask import request
from flask_api import FlaskAPI
from EmulatorGUI import GPIO

GPIO.setmode(GPIO.BCM)
LEDS = {"green":16,"red":18}
GPIO.setup(LEDS["green"],GPIO.OUT)
GPIO.setup(LEDS["red"],GPIO.OUT)
#Se inicializa el framework FlaskAPI el cual permite generar interfaz web para consumir los metodos
app = FlaskAPI(__name__)


#Ruta principal del api
@app.route('/',methods = ["GET"])
def api_root():
    return {"led_url":request.url+"led/(green|red)","led_url_POST":{"state":"(0|1)"},"Levis":"Tabares"}

@app.route('/led/<color>/', methods=["GET", "POST"])
def api_leds_control(color):
    if request.method == "POST":
        if color in LEDS:
            #GPIO.output(18,True)
            GPIO.output(LEDS[color], int(request.data.get("state")))      
   
    return {color: GPIO.getStatePinOut(LEDS[color])}
if __name__== "__main__":
    app.run()