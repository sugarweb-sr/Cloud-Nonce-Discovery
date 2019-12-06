# use for comsm0010_CW

import boto3
import time

def creat_instances(num):
    ec2 = boto3.client('ec2')
    ec2.run_instances(
        ImageId='ami-04b9e92b5572fa0d1',
        InstanceType='t2.micro',
        MinCount=num,
        MaxCount=num,
        KeyName='cnd',
        Monitoring={'Enabled': False},
        SecurityGroupIds=['sg-0753cdb8ce7cd2fc4'],
    )


def terminate_instances():
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    instancesnum = len(instances['Reservations'])
    ids = [None] * instancesnum
    for i in range(instancesnum):
        result = instances['Reservations'][i]['Instances'][0]['InstanceId']
        ids[i] = result
    ec2.terminate_instances(InstanceIds=ids)


if __name__ == '__main__':

# the number of VMs
    num = 2

    creat_instances(num)
#set the time that all works have been done needed, it should be long enough
    time.sleep(1000000000)

    terminate_instances()

