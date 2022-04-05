from flask import jsonify, request, json, g
from flask_httpauth import HTTPTokenAuth, HTTPBasicAuth
from . import mod
from gateway.odoo_methods.logic import Logic
from gateway.utilities.util import Util
import datetime
import requests


@mod.route('/create-lead', methods=['POST'])
def create_lead():
    """ Add a members bio data into the systeme """
    headers = request.headers
    db = headers.get("db")
    user = headers.get("user")
    password = headers.get("password")
    with Logic(db=db, user=user, password=password) as logic:

        data = request.json
        response = logic.create_lead(data)
    return response
