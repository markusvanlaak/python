import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask import request, render_template
import redis
import etcd

etcdconn = etcd.Client(host='127.0.0.1', port=2379)
r = redis.StrictRedis(host='localhost', port=6000, db=0)
#r = redis.StrictRedis(host='localhost', port=6379, db=0)


app = Flask(__name__, static_url_path='/home/markus/template/')

@app.route("/")
def hello():
    timestart = datetime.now()
    etcdconn.write('/nodes/n1', 1)
    timedone = datetime.now()
    timedelta = timedone - timestart
    logging.info(' writing to etcd took %s' % timedelta)
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
        r.lpush (user,message)
        return 'POST request %s' % message
def rag():
        if request.method == 'GET':
                return "Status"

@app.route('/read',methods=['GET'])
def read():
    if request.method == 'GET':
        user = request.args.get('user')
        n = r.llen(user)
        nu = n
        messages=[]
        while (n > 0):
            messages.append(r.lpop(user))
            n = n - 1

        return render_template('gam.html', data=messages, anzahl=nu)
    else:
        logging.warning(' 415 not supported')
        return "415 not supported"
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='myapp.log', level=logging.INFO)
    app.run()