import ftplib
import os.path

def returnDefault(ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        print('[-] Could not list directory contens.')
        print('[-] Skipping To Next Target.')
        return

    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.' in fn or '.html' in fn or '.asp' in fn:
            print('[+] Found default page: ' + fileName)
            retList.append(fileName)

    return retList


if __name__ == '__main__':
    host = '192.168.1.108'
    userName = 'msfadmin'
    password = 'msfadmin'
    ftp = ftplib.FTP(host)
    ftp.login(userName, password)
    returnDefault(ftp)