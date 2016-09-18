#!/usr/bin/env python
import logging
import random
import requests
import sys
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


SERVERS = [
    '127.0.0.1:8081',
    '127.0.0.2:8082',
    '127.0.0.3:8083',
]


class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        logging.warning(self.server.server_address)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        if self.path == '/':
            choices = make_a_choice(self)
        if self.path == '/node':
            choices = random.choice(['yes', 'no'])
        self.wfile.write(choices)
        return


def make_a_choice(host_self):
    choices = {'yes': 0, 'no': 0}
    choices[random.choice(['yes', 'no'])] += 1
    for each_server in SERVERS:
        if each_server != ':'.join(str(ea_item) for ea_item
                                   in host_self.server.server_address):
            logging.warning('requesting {}'.format(each_server))
            choices1 = requests.get('http://{}/node'.format(each_server))
            choices[choices1.text] += 1
        else:
            logging.warning('samve server!')
            logging.warning(host_self.server.server_address)
    return 'yes' if choices['yes'] > choices['no'] else 'no'


def setup_server(host, port):
    server = HTTPServer(('{}'.format(host), int(port)), myHandler)
    logging.warning('Started httpserver on \
        server {} and port {}'.format(host, port))
    server.serve_forever()


if __name__ == '__main__':
    setup_server(sys.argv[1], sys.argv[2])
