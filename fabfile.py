# use for comsm0010_CW

from json import loads
from fabric.api import *
import boto3
import hashlib
import time


ec2 = boto3.client('ec2')
instances = ec2.describe_instances(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
instancesnum = len(instances['Reservations'])
print(instancesnum)
if instancesnum > 0:
    hosts = [None] * instancesnum
    for i in range(instancesnum):
        host = instances['Reservations'][i]['Instances'][0]['PublicDnsName']
        hosts[i] = host

env.hosts = hosts
env.user = 'ubuntu'
env.key_filename = 'D:/advanced computing/cloud computing/.ssh/cnd.pem'


def compute1():
    put('D:/advanced computing/cloud computing/PycharmProjects/untitled/cloud computing/work1.py',
        '/home/ubuntu/work1.py')
    run('python3 work1.py')

def compute2(difnum):
    pow(difnum)

@parallel
def cnd1():
    put('D:/advanced computing/cloud computing/PycharmProjects/untitled/cloud computing/work1.py',
        '/home/ubuntu/work1.py')
    run('python3 work1.py')



@parallel
def cnd2(difnum,N):
    r = run('curl ipinfo.io/json')
    returned = loads(r)
    h = returned['hostname']
    print(h)
    for i in range(0, N):
        if env.hosts[i]==h:
            pown(difnum,N,i)


def pow(difnum):
    num=int(difnum)
    max_nonce = 2 ** 32
    header = 'COMSM0010cloud'
    print("Starting search...")
    start_time = time.time()
    for nonce in range(0, max_nonce):
        block_nonce = header + str(nonce)
        hashresult = hashlib.sha256(block_nonce.encode('utf-8')).hexdigest()
        if hashresult[0:num] == str(0).zfill(num):
            print("Success with nonce %d" % nonce)
            print("Hash is %s" % hashresult)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Elapsed time: %f seconds" % elapsed_time)
            if elapsed_time > 0:
                hash_power = float(int(nonce) / elapsed_time)
                print("Hashing power: %ld hashes per second" % hash_power)
            return (hashresult, nonce)
    print("Failed after %d (max_nonce) tries" % nonce)
    return nonce





def pown(difnum, N, m):
    num=int(difnum)
    max_nonce = 2 ** 32
    header = 'COMSM0010cloud'
    print("Starting search...")
    start_time = time.time()
    for nonce in range(m-1, max_nonce, N):
        block_nonce = header + str(nonce)
        hashresult = hashlib.sha256(block_nonce.encode('utf-8')).hexdigest()
        if hashresult[0:num] == str(0).zfill(num):
            print("Success with nonce %d" % nonce)
            print("Hash is %s" % hashresult)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Elapsed time: %f seconds" % elapsed_time)
            if elapsed_time > 0:
                hash_power = float(int(nonce) / elapsed_time)
                print("Hashing power: %ld hashes per second" % hash_power)
            return (hashresult, nonce)
    print("Failed after %d (max_nonce) tries" % nonce)
    return nonce



