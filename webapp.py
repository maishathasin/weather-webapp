import requests
import json
from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def weather():
    response = requests.get('https://www.metaweather.com/api/location/4118/')
    x = response.json()

    y = x["consolidated_weather"]
    current_state = y[0]
    state = current_state['weather_state_name']
    temp = current_state['the_temp']
    l = 'l'
    if (state == 'snow'):
        l = '🌨' 
    elif(state== 'Thunderstorm'):
        l = '🌩' 
    elif(state == 'Showers'):
        l = '⛈'
    elif(state == 'Clear'):
        l = '☀️'
    elif(state == 'Heavy Cloud'):
        l = '☁️'
    elif(state == 'Light Cloud'):
        l = '🌥'
    return render_template('weather.html', state=state,temp=temp,emoji=l)












