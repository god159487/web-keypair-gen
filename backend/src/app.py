import os
import json
import datetime
import flask
from flask import Flask, render_template, request, send_from_directory, redirect
# from flask_cors import CORS, cross_origin
import urllib
import requests
import google.auth.transport.requests
import google.oauth2.id_token
import pyrebase
import firebase_admin
from firebase_admin import credentials, auth
from functools import wraps
from env import FLASK_ENV
from constants import LASI_VM_SERVICE_URL, KEYPAIR_GENERATOR_URL


CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "*",
    "Access-Control-Allow-Headers": "*",
    "Access-Control-Max-Age": "3600",
}


def check_token(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if not request.headers.get('Authorization'):
            return {'message': 'No token provided'},400
        try:
            user = auth.verify_id_token(request.headers['Authorization'].split(" ")[1])
            request.user = user
        except:
            return {'message':'Invalid token provided.'},400
        return f(*args, **kwargs)
    return wrap


def create_app(test_config=None):

    app = Flask(__name__, static_url_path="/static")
    app.config['CORS_HEADERS'] = 'Content-Type'
    # CORS(app)

    #Connect to firebase
    cred = credentials.Certificate('fbAdminConfig.json')
    firebase = firebase_admin.initialize_app(cred)
    pb = pyrebase.initialize_app(json.load(open('fbconfig.json')))

    @app.route("/sa-decoder")
    @app.route("/keypair")
    @app.route("/login")
    @app.route("/annoation")
    @app.route("/lasivm")
    @app.route("/")
    def get_index():
        
        response = send_from_directory("static", "index.html")
        # response.headers["Cache-Control"] = "no-store"
        return response

    @app.route("/sample-flask-healthcheck")
    @check_token
    def health_check():
        try:
            url = 'https://sampleflaskapi-grccdfiqlq-as.a.run.app'
            req = urllib.request.Request(url)

            auth_req = google.auth.transport.requests.Request()
            id_token = google.oauth2.id_token.fetch_id_token(auth_req, url)
            req.add_header("Authorization", f"Bearer {id_token}")

            response = urllib.request.urlopen(req)

            return response.read()

        except Exception as e:
            app.logger.error(e)


    @app.route("/get-keypair")
    @check_token
    def keypair_generator():
        try:

            node_id = request.args.get('node_id')
            url = f'{KEYPAIR_GENERATOR_URL}/api/v1/get-keypair?node_id={node_id}'
            req = urllib.request.Request(url)

            auth_req = google.auth.transport.requests.Request()
            id_token = google.oauth2.id_token.fetch_id_token(auth_req, url)
            req.add_header("Authorization", f"Bearer {id_token}")

            response = urllib.request.urlopen(req)
            return response.read()

        except Exception as e:
            app.logger.error(e)


    @app.route("/create-instance")
    @check_token
    def create_instance():
        try:
            pc_num = request.args.get('pc_num')
            url = f'{LASI_VM_SERVICE_URL}/api/v1/create-instance?pc_num={pc_num}'
            req = urllib.request.Request(url)

            auth_req = google.auth.transport.requests.Request()
            id_token = google.oauth2.id_token.fetch_id_token(auth_req, url)
            req.add_header("Authorization", f"Bearer {id_token}")

            response = urllib.request.urlopen(req)

            return response.read()

        except Exception as e:
            app.logger.error(e)


    @app.route("/create-multi-instance")
    @check_token
    def create_multi_instance():
        try:
            pc_quantity = request.args.get('pc_quantity')
            url = f'{LASI_VM_SERVICE_URL}/api/v1/create-multi-instance?pc_quantity={pc_quantity}'
            req = urllib.request.Request(url)

            auth_req = google.auth.transport.requests.Request()
            id_token = google.oauth2.id_token.fetch_id_token(auth_req, url)
            req.add_header("Authorization", f"Bearer {id_token}")

            response = urllib.request.urlopen(req)

            return response.read()

        except Exception as e:
            app.logger.error(e)


    @app.route("/delete-instance")
    @check_token
    def delete_instance():
        try:
            pc_num = request.args.get('pc_num')
            url = f'{LASI_VM_SERVICE_URL}/api/v1/delete-instance?pc_num={pc_num}'
            req = urllib.request.Request(url)

            auth_req = google.auth.transport.requests.Request()
            id_token = google.oauth2.id_token.fetch_id_token(auth_req, url)
            req.add_header("Authorization", f"Bearer {id_token}")

            response = urllib.request.urlopen(req)

            return response.read()

        except Exception as e:
            app.logger.error(e)


    @app.route("/delete-all-instance")
    @check_token
    def delete_all_instance():
        try:
            url = f'{LASI_VM_SERVICE_URL}/api/v1/delete-all-instance'
            req = urllib.request.Request(url)

            auth_req = google.auth.transport.requests.Request()
            id_token = google.oauth2.id_token.fetch_id_token(auth_req, url)
            req.add_header("Authorization", f"Bearer {id_token}")

            response = urllib.request.urlopen(req)

            return response.read()

        except Exception as e:
            app.logger.error(e)


    @app.route("/get-vm-status")
    @check_token
    def get_vm_status():
        try:
            url = f'{LASI_VM_SERVICE_URL}/api/v1/get-vm-status'
            req = urllib.request.Request(url)

            auth_req = google.auth.transport.requests.Request()
            id_token = google.oauth2.id_token.fetch_id_token(auth_req, url)
            req.add_header("Authorization", f"Bearer {id_token}")

            response = urllib.request.urlopen(req)

            return response.read()

        except Exception as e:
            app.logger.error(e)

    return app
