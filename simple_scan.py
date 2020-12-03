#!/usr/bin/env python
# -*- coding:utf-8 -*-

import optparse
import socket
import re
import threading

screenLock = threading.Semaphore(value=1)

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)

        screenLock.acquire() # 加锁

        print '[+]%d/tcp open' % tgtPort
        print '[+] ' + str(results)
    except:
        screenLock.acquire()
        print '[-]%d/tcp closed' % tgtPort
    finally:
        screenLock.release()
        connSkt.close()


def portScan(tgtHost, tgtPorts):
    pattern = '%d\.%d\.%d\.%d'
    #print pattern
    match = re.match(pattern, tgtHost)
    if match:
        tgtIP = tgtHost
    else:
        try:
            tgtIP = socket.gethostbyname(tgtHost)
        except:
            print '[-] Cannot resolve %s: Unknown host' % tgtHost

    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print '\n[+] Scan Results for: ' + tgtName
    except:
        print '\n[+] Scan Results for: ' + tgtIP
    socket.setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        print 'Scanning port ' + str(tgtPort)
        t = threading.Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()



def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
    parser.add_option('-H', '--host', dest='tgtHost', type='string', help='specity target host')
    parser.add_option('-p', '--port',dest='tgtPort', type='int', help='specity target port')
    options, args = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort
    args.append(tgtPort)
    if tgtHost == None or tgtPort == None:
        print '[-] You must specify a target host and port[s]!'
        exit(0)
    portScan(tgtHost, args)

if __name__ == '__main__':
    main()
