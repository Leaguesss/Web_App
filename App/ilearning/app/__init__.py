
from bottle import Bottle

app = Bottle(__name__)

from app import controller

