#!/usr/bin/env python3
# -*- coding:utf -*-

import optparse
from pexpect import pxssh

class Client(object):
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print(e)
            print('[-] Error Connectiing')

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


def botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print('[*] Output from {}'.format(client.host))
        print('[*] {}\n'.format(output))


def addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

botNet = []

addClient('192.168.1.110', 'ubuntu', 'whoami1023')
botnetCommand('uname -v')



