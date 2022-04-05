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


class Logic:

    def __init__(self, db, user, password):
        self.url = f'https://{db}'
        self.db = db
        self.user = user
        self.password = password
        self.server = xmlrpc.client.ServerProxy(
            '{}/xmlrpc/2/common'.format(self.url))
        self.uid = self.server.authenticate(db, user, password, {})
        self.models = xmlrpc.client.ServerProxy(
            '{}/xmlrpc/2/object'.format(self.url))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def invoke(self, model, method, *args):
        reponse = self.models.execute_kw(
            self.db, self.uid, self.password, model, method, [args])
        return reponse

    # MEMBER
    def create_lead(self, lead_details):
        try:
            # if 'tag' in lead_details:
            #     self.invoke('crm.tag', 'search', [[['is_company', '=', True]]], {
            #                 'offset': 10, 'limit': 5})
            #     tag_id = self.invoke('crm.tag', 'create', {
            #                          "name": lead_details['tag']})
            #     del lead_details['tag']
            #     lead_details['tag_ids'] = tag_id

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
