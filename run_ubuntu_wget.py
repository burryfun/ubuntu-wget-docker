#!/usr/bin/python

import sys
import subprocess
import threading


def docker_build(num):
    subprocess.call(['sudo', 'docker', 'build', '-t', 'ubuntu-{}'.format(num), '.'])

def docker_run(num, server_ip, number_of_requests):
    subprocess.call(['sudo', 'docker', 'run', '-d', 'ubuntu-{}'.format(num),
                     './nginx_wget.sh', server_ip, number_of_requests])

if __name__ == "__main__":

    # count of ubuntu images
    count = int(sys.argv[1])
    server_ip = sys.argv[2]
    number_of_requests = sys.argv[3]

    for i in range(count):
        th = threading.Thread(target=docker_build, args=(i,))
        th.start()

    for i in range(count):
        th = threading.Thread(target=docker_run, args=(i, server_ip, number_of_requests))
        th.start()