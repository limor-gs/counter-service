# Counter service

## Content
### Dockerfile - 
Based on python:3.6
Installs flask
Installs redis
Runs the command - python counter-service.py

### counter-service.py, config.py - 
Runs the service using flask
Writes the counter to redis database 
Writes the redis app id to file named ‘app_id_<branch_name>’
In order to save the counter between upgrades, the file is mounted to the host vm located in /tmp/app 

### Jenkinsfile - 
Gets branch name as parameter
Removes the counter container if exists 
Builds the counter image
Creates the counter container based on counter image, container name is ‘counter-<branch_name>’
Prints the container ip
Prints examples of POST and GET commands using the container ip.

## Instructions
Access Jenkins by the following url - https://34.255.57.138/
User: admin
Password: admin

'counter-service-Multibranch' job creates a container for each 
branch that runs the web server. The jos is run on every push to 
every branch.

There are two options to send the requests

#### Increase counter using:
curl -X POST http://<container_ip>:5000/ 
**or** . 
curl -X POST "http://<host_public_ip>/<branch_name>"
#### Display counter using:
curl http://<container_ip>:5000/ . 
**or** using the browser . 
http://<host_public_ip>/<branch_name> . 
http://34.255.57.138/dev








