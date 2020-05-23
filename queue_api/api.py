#!/usr/bin/python

import cherrypy
import json
import uuid

MINUTES_PER_PATIENT = 5


class PrioQueue(object):
    def __init__(self):
        self.data = []
        for c in range(0, 10):
            self.data.append([])

    def push(self, item, prio):
        if (prio >= 0) and (prio < 10):
            self.data[prio].append(item)

    def pop(self):
        for i in range(9, -1, -1):
            list = self.data[i]
            if len(list) > 0:
                return list.pop()
        return None

    def count_inner(self):
        return sum([len(l) for l in self.data])

    def before(self, item):
        counter = 0
        for i in range(9, -1, -1):
            print('prio: ', i)
            lili = self.data[i]
            if item in lili:
                counter += lili.index(item)
                break
            else:
                counter += len(lili)
        return counter

    def find(self, id):
        for list in self.data:
            for item in list:
                if item['id'] == id:
                    return item
        return None

    def remove(self, item):
        for list in self.data:
            if item in list:
                list.remove(item)

    def all_with_prio(self):
        items = []
        for prio, list in enumerate(self.data):
            for item in list:
                items.append({
                    'item': item,
                    'prio': prio
                })
        return items


class Server(object):
    def __init__(self):
        self.apt_queue = PrioQueue()
        self.call_queue = []
        self.apt_ongoing = []

    def find_apt(self, apt_id):
        return self.apt_queue.find(apt_id)

    def find_ongoing_apt(self, apt_id):
        for apt in self.apt_ongoing:
            if apt['id'] == apt_id:
                return apt
        return None

    def create_id(self):
        return uuid.uuid4().hex

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
        return json.dumps(self.apt_queue.all_with_prio())

    @cherrypy.expose
    def expected_apt_wait(self):
        return json.dumps(self.apt_queue.count_inner() * MINUTES_PER_PATIENT)

    @cherrypy.expose
    def create_apt(self, prio):
        id = self.create_id()
        self.apt_queue.push({
            'id': id
        }, int(prio))
        return id

    @cherrypy.expose
    def apt_status(self, apt_id=None):
        found = self.find_apt(apt_id)
        if found:
            index = self.apt_queue.before(found)
            return json.dumps({
                'wait_time': index * MINUTES_PER_PATIENT,
                'before_you': index
            })
        else:
            return 'Not found'

    @cherrypy.expose
    def start_apt(self, apt_id=None):
        found = self.find_apt(apt_id)
        if found:
            self.apt_queue.remove(found)
            self.apt_ongoing.append(found)
        else:
            return 'Not found'

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
cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(
    Server(),
    config={
        '/': {
            'tools.CORS.on': True}
    }
)
