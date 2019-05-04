from flask import Flask,render_template
try:

	from twilio.rest import Client
except ImportError:
	print("Error in twilio")
import requests
app=Flask(__name__)

@app.route('/')
def index():
	city='Patna'
	country='IN'
	appid='20d01cb3e42aec48af6097a37756381b'
	url = 'http://api.openweathermap.org/data/2.5/weather?q={},country={}&appid={}'
	res = requests.get(url.format(city,country,appid)).json()	
	 

	weather = {
			'city' : city,

			'temperature' : res['main']['temp'] ,
			'description' : res['weather'][0]['description'],
			'icon': res['weather'][0]['icon']


	}
	print(weather)



	return render_template('weather.html',weather=weather)


@app.route('/makeCalls')
def makeCalls():



# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+14155551212',
                        from_='+15017122661'
                    )

print(call.sid)

if __name__ == '__main__':
	app.run() 