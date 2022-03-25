import json
import xmlrpc.client
import logging
from flask import g, jsonify, url_for, render_template
import sys
import requests
import random
import base64
from gateway.utilities.util import Util
import itertools

logging.basicConfig()
var = sys.version

URL = 'https://erp.jengaschool.com'
DB = 'erp.jengaschool.com'
USER = 'admin'
PASS = 'admin'


class Logic:

    def __init__(self):

        self.server = xmlrpc.client.ServerProxy(
            '{}/xmlrpc/2/common'.format(URL))
        self.uid = self.server.authenticate(DB, USER, PASS, {})
        self.models = xmlrpc.client.ServerProxy(
            '{}/xmlrpc/2/object'.format(URL))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def invoke(self, model, method, *args):
        reponse = self.models.execute_kw(
            DB, self.uid, PASS, model, method, [args])
        return reponse

    # MEMBER
    def create_lead(self, lead_details):
        try:
            self.invoke(
                'crm.lead', 'create', lead_details)

            resp = jsonify({"message": "new lead created"})
            resp.status_code = 201
            return resp

        except Exception as e:
            resp = jsonify({
                "error": str(e),

            })
            resp.status_code = 404
            return resp
