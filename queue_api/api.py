#!/usr/bin/python

import cherrypy
import json
import uuid

MINUTES_PER_CALL = 2
MINUTES_PER_PATIENT = 5
JITSI_BASE_URL = 'https://call.parsons.group/'


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
        self.call_queue = PrioQueue()
        self.apt_ongoing = []
        self.call_ongoing = []

    def find_apt(self, apt_id):
        return self.apt_queue.find(apt_id)

    def find_ongoing_apt(self, apt_id):
        for apt in self.apt_ongoing:
            if apt['id'] == apt_id:
                return apt
        return None

    def find_call(self, call_id):
        return self.call_queue.find(call_id)

    def find_ongoing_call(self, call_id):
        for call in self.call_ongoing:
            if call['id'] == call_id:
                return call
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
        prioritized = {}
        for i in range(0, 10):
            prioritized[str(i)] = []
        for apt in self.apt_queue.all_with_prio():
            apt = apt['item']
            prioritized[str(apt['prio'])].append([apt['id'], 'waiting'])
        for apt in self.apt_ongoing:
            prioritized[str(apt['prio'])].append([apt['id'], 'ongoing'])
        return json.dumps(prioritized)

    @cherrypy.expose
    def expected_apt_wait(self):
        n = self.apt_queue.count_inner()
        return json.dumps([
            n,
            n * MINUTES_PER_PATIENT
        ])

    @cherrypy.expose
    def create_apt(self, priority=0):
        id = self.create_id()
        self.apt_queue.push({
            'id': id,
            'prio': int(priority)
        }, int(priority))
        return id

    @cherrypy.expose
    def apt_status(self, id=None):
        found = self.find_apt(id)
        if found:
            index = self.apt_queue.before(found)
            return json.dumps([
                index + 1,
                index * MINUTES_PER_PATIENT
            ])
        else:
            raise cherrypy.HTTPError(404)

    @cherrypy.expose
    def start_apt(self, id=None):
        found = self.find_apt(id)
        if found:
            self.apt_queue.remove(found)
            self.apt_ongoing.append(found)
            return 'true'
        else:
            raise cherrypy.HTTPError(404)

    @cherrypy.expose
    def end_apt(self, apt_id):
        found = self.find_ongoing_apt(apt_id)
        if found:
            self.apt_ongoing.remove(found)
            return 'true'
        else:
            raise cherrypy.HTTPError(404)

    @cherrypy.expose
    def all_calls(self):
        prioritized = {}
        for i in range(0, 10):
            prioritized[str(i)] = []
        for call in self.call_queue.all_with_prio():
            call = call['item']
            prioritized[str(call['prio'])].append([call['id'], 'waiting'])
        for call in self.call_ongoing:
            prioritized[str(call['prio'])].append([call['id'], 'ongoing'])
        return json.dumps(prioritized)

    @cherrypy.expose
    def expected_call_wait(self):
        n = self.call_queue.count_inner()
        return json.dumps([
            n,
            n * MINUTES_PER_CALL
        ])

    @cherrypy.expose
    def request_call(self, priority=0):
        id = self.create_id()
        self.call_queue.push({
            'id': id,
            'prio': int(priority)
        }, int(priority))
        return id

    @cherrypy.expose
    def call_status(self, call_id):
        found = self.find_call(call_id)
        if found:
            index = self.call_queue.before(found)
            return json.dumps([
                index + 1,
                index * MINUTES_PER_CALL
            ])
        else:
            raise cherrypy.HTTPError(404)

    @cherrypy.expose
    def start_call(self, id):
        found = self.find_call(id)
        if found:
            self.call_queue.remove(found)
            self.call_ongoing.append(found)
            return 'true'
        else:
            raise cherrypy.HTTPError(404)

    @cherrypy.expose
    def call_finished(self, id):
        found = self.find_ongoing_call(id)
        if found:
            self.call_ongoing.remove(found)
            return 'true'
        else:
            raise cherrypy.HTTPError(404)

    @cherrypy.expose
    def call_url(self, id):
        found = self.find_ongoing_call(id)
        if found:
            return JITSI_BASE_URL + id
        else:
            raise cherrypy.HTTPError(404)


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
