import os
import uuid


with open('/etc/hostname', 'r') as myfile:
	data = myfile.read().strip()
APP_ID_PATH = f"/tmp/app/app_id_{data}"
if os.path.exists(APP_ID_PATH):
	with open(APP_ID_PATH) as app_id_file:
		app_id = app_id_file.read()
else:
	with open(APP_ID_PATH, 'w') as app_id_file:
		app_id = uuid.uuid4().hex
		app_id_file.write(app_id)


class Config(object):	
	REDIS_HOST = 'redis-15816.c1.eu-west-1-3.ec2.cloud.redislabs.com'
	REDIS_PORT = 15816
	REDIS_PASS = 'fY6X71N8zpTGYyAsAkqU9t46NBr2cfFr'    


class AppConfig(Config):	
	APP_ID = app_id
