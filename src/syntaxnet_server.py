#!/usr/bin/python3
import json, os
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from syntaxnet_parser import SyntaxnetParser
from conll2tree import conll2tree, buildNodeList

ENV_MODEL_DIR = os.environ.get('MODEL_DIR')
MODEL_DIR = ENV_MODEL_DIR if ENV_MODEL_DIR else "/models/Spanish-AnCora"

parser = SyntaxnetParser(MODEL_DIR)

app = Flask(__name__)
api = Api(app)


class ParseTree(Resource):
    def get(self):
        response = {}
        return response
    
    def post(self):
        text = json.loads(request.get_data())['text']
        tree = parser.parse(text)      
        return conll2tree(tree)


class ParseConll(Resource):
    def get(self):
        response = {}
        return response
    
    def post(self):
        text = json.loads(request.get_data())['text']
        tree = parser.parse(text)
        conll = buildNodeList(tree)      
        return {'conll': conll}

    
class ParseTree_Name(Resource):
    def get(self, employee_id):      
        return {}


api.add_resource(ParseTree, '/tree') # Route_1
api.add_resource(ParseConll, '/conll') # Route_2
api.add_resource(ParseTree_Name, '/tree/<employee_id>') # Route_3


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')