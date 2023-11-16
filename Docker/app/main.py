from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def say_hello():
	return 'HELLO this is from Docker container'

@app.route('/name')
def return_name():
	return 'My name is HARSHA'

@app.route('/hostname')
def return_hostname():
	hostname = socket.gethostname()
	return hostname

@app.route('/ip')
def return_ip():
	hostname = socket.gethostname()
	get_ip = socket.gethostbyname(hostname)
	return get_ip

if __name__ == '__main__':
	app.run(host="0.0.0.0", port="8080")

