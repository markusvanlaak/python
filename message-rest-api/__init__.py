import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask import request, render_template
from flask_testing import TestCase
from flask_testing import LiveServerTestCase
import redis
import etcd


app = Flask(__name__, static_url_path='/home/markus/template/')



