"""
Tool for interacting with NEO's cloudx API.

Usage: neo.py <create|delete> <NEO IP> <NEO password> </path/to/port.json>

The JSON file is the data normally sent from the neutron plugin to NEO, a dump
of the port state. There is an example in example-port.json.
"""

import json
import requests
import sys


def login(session, ip, password):
    login_url = 'http://{}/neo/login'.format(ip)
    data = 'username=admin&password={}'.format(password)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'} 
    r = session.post(login_url, data=data, headers=headers)
    print r.text
    r.raise_for_status()


def show_port(session, ip, id):
    # Doesn't seem to work.
    url = 'http://{}/neo/cloudx/Ports'.format(ip, id)
    r = session.get(url)
    print r.text
    r.raise_for_status()


def create_port(session, ip, data):
    url = 'http://{}/neo/cloudx/Port'.format(ip)
    r = session.post(url, data=data)
    print r.text
    r.raise_for_status()


def delete_port(session, ip, data):
    id = json.loads(data)['id']
    url = 'http://{}/neo/cloudx/Port/{}'.format(ip, id)
    r = session.delete(url, data=data)
    print r.text
    r.raise_for_status()


def main():
    session = requests.session()
    if len(sys.argv) != 5:
        raise Exception("Usage: %s <create|delete> <NEO IP> <NEO password> </path/to/port.json>" % sys.argv[0])
    op = sys.argv[1]
    ip = sys.argv[2]
    password = sys.argv[3]
    with open(sys.argv[4], 'r') as f:
        data = f.read()
    login(session, ip, password)
    if op == 'create':
        create_port(session, ip, data)
    elif op == 'delete':
        delete_port(session, ip, data)
    else:
        raise Exception("Unknown operation %s" % op)


if __name__ == "__main__":
    main()
