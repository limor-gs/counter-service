from redis import StrictRedis
from flask import Flask, request

app = Flask(__name__)
app.config.from_object('config.AppConfig')


class Counter():
	def __init__(self):
		self.app_id = app.config.get('APP_ID')	
		connection = {
			'host': app.config.get('REDIS_HOST'),
			'password': app.config.get('REDIS_PASS'),
			'port': app.config.get('REDIS_PORT'),
			'db': 0
		}
		self.redis = StrictRedis(**connection)		

	def increase(self):				
		return self.redis.incr(self.app_id)

	def value(self):				
		return self.redis.get(self.app_id) or '0'


@app.route('/', methods=['GET', 'POST'])
def hello():
	if request.method == 'POST':
		response = f"Increasing counter. new value: {Counter().increase()} "		
	else:
		response = f"Counter value: {int(Counter().value())}"
	return response

if __name__ == '__main__':    	
	app.run(host='0.0.0.0', port=5000)
