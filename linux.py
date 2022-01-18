import subprocess

stdout = ''' PING S15SERVER1 (10.17.165.125) 56(84) bytes of data.
64 bytes from S15SERVER1 (10.17.165.125): icmp_seq=1 ttl=64 time=1.42 ms

--- S15SERVER1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 1.425/1.425/1.425/0.000 ms

'''
def linux_ip():
    for line in stdout.splitlines():

        if line.strip().startswith('PING'):
            print ((line.split(' ')[3]).strip('()'))


linux_ip()