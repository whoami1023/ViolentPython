#!/usr/bin/env python3

import pexpect

PROMPT = ['#', '>>>', '>', '\$']

def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)


def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continux connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret == 0:
        print('[-] Error Connection')
        return

    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P\p]assword:'])

    if ret == 0:
        print('[-] Error Connection')
        return

    child.sendline(password)
    child.expect(PROMPT)
    return child


if __name__ == '__main__':
    ssh = connect('ubuntu', '192.168.1.110', 'whoami1023')
    send_command(ssh, 'ls -al')
