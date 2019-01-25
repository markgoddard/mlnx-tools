# Mellanox Tools

Tools for working with Mellanox products

## neo.py

Script for interacting with the Mellanox NEO Cloudx API, used for integration
between OpenStack and Mellanox NEO SDN controller. Supports manually creating
and deleting ports, which can be useful if things have got out of sync somehow.

Usage:

    neo.py <create|delete> <NEO IP> <NEO password> </path/to/port.json>

The JSON file is the data normally sent from the neutron plugin to NEO, a dump
of the port state. There is an example in example-port.json. A dump of the data
sent to NEO is available in the NEO logs file
/opt/neo/files/controller/log/web-info.log.
