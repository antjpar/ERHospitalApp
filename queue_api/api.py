#!/usr/bin/python

import cherrypy
import json


class Server(object):
    def __init__(self):
        self.apt_queue = []
        self.call_queue = []

    @cherrypy.expose
    def get_hospitals(self):
        return json.dumps([
            {
                'name': 'St. Josefskrankenhaus'
            },
            {
                'name': 'Universitätsklinikum'
            }
        ])

    @cherrypy.expose
    def all_appointments(self):
        return json.dumps(self.apt_queue)

    @cherrypy.expose
    def expected_apt_wait(self):
        return 132

    @cherrypy.expose
    def create_apt(self):
        pass

    @cherrypy.expose
    def apt_status(self, apt_id=None):
        if apt_id is not None:
            return json.dumps({
                'wait_time': 123,
                'before_you': 4
            })
        else:
            return None

    @cherrypy.expose
    def start_apt(self, apt_id=None):
        pass

    @cherrypy.expose
    def end_apt(self, apt_id=None):
        pass

    @cherrypy.expose
    def all_calls(self):
        return json.dumps(self.call_queue)

    @cherrypy.expose
    def expected_call_wait(self):
        pass

    @cherrypy.expose
    def request_call(self):
        pass

    @cherrypy.expose
    def call_status(self):
        pass

    @cherrypy.expose
    def answer_call(self):
        pass

    @cherrypy.expose
    def call_finished(self):
        pass


def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"


cherrypy.config.update({
    'cors.expose.on': True,
})
cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
cherrypy.quickstart(
    Server(),
    config={
        '/': {
            # 'request.dispatch':
            #     cherrypy.dispatch.MethodDispatcher(),
            'tools.CORS.on': True}}
)
