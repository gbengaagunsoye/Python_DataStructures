#!/usr/bin/env python
import pexpect

devices = {'Arista1': {'prompt': 'Arista1#', 'ip': '10.10.10.2'},
            {'Arista2': {'prompt': 'Arista2#', 'ip': '10.10.10.3'}}

username = 'admin'
password = 'Python'

for device in devices.keys():
    device_prompt = devices[device]['prompt']
    child = pexpect.spawn('telnet' + devices[device]['ip'])
    child.expect('Username:')
    child.sendline(username)
    child.expect('Password:')
    child.sendline(password)
    child.expect(device_prompt)
    child.sendline('show version | include V')
    child.expect(device_prompt)
    print(child.before)
    child.sendline('exit')