import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask import request, render_template
import redis
import etcd

client = etcd.Client(host='127.0.0.1', port=2793)
redisconn = redis.StrictRedis(host='localhost', port=6000, db=0)
#r = redis.StrictRedis(host='localhost', port=6379, db=0)



app = Flask(__name__, static_url_path='/home/markus/PycharmProjects/untitled/message-rest-api/template/')

@app.route("/")
def hello():app.logger.warning('A warning occurred (%d apples)', 42)
        app.logger.error('An error occurred again and again')
        app.logger.info('Info')
        return app.send_static_file('index.html')

@app.route("/send")
def send():
	return app.send_static_file('send.html')

#/post?user=<username>&message=<message>
@app.route('/post',methods=['GET','POST'])
def post():
	if request.method == 'GET':
		return "GET request"
	elif request.method == 'POST':
		user = request.form['user']
		message = request.form['message']
		redisconn.lpush (user,message)
		return 'POST request %s' % message
def rag():
        if request.method == 'GET':
                return "Status"

@app.route('/read',methods=['GET'])
def read():
	if request.method == 'GET':
		user = request.args.get('user')
		n = redisconn.llen(user)
		nu = n
		messages=[]
		while (n > 0):
			messages.append(redisconn.lpop(user))
			n = n - 1

		return render_template('gam.html', data=messages, anzahl=nu)
	else:
		return "415 not supported"
if __name__ == "__main__":
    formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()