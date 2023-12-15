import boto3, json

aws_access_key_id = ''
aws_secret_access_key = ''

aws_session = boto3.Session(region_name="ap-south-1",
                            aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key)

ec2 = aws_session.resource('ec2')


def get_all_instances():
    instances = ec2.instances.all()
    instance_list = []
    for instance in instances:
        instance_dict = {
            'id': instance.id,
            'state': instance.state['Name'],
            'instance_type': instance.instance_type,
            'availability_zone': instance.placement['AvailabilityZone'],
            'security_groups': instance.security_groups,
            'private_ip': instance.private_ip_address,
            'public_ip': instance.public_ip_address,
            'launch_time': instance.launch_time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        instance_list.append(instance_dict)
    return json.dumps(instance_list)


def create_instance():
    instance = ec2.create_instances(
        ImageId='ami-0287a05f0ef0e9d9a',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro')
    print(instance[0].id)


def start_all_instances():
    instances = ec2.instances.all()
    instance_ids = [instance.id for instance in instances]
    ec2.instances.filter(InstanceIds=instance_ids).start()
    return json.dumps({'message': 'EC2 instances are starting...'})


def stop_all_instances():
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    instance_ids = [instance.id for instance in instances]
    ec2.instances.filter(InstanceIds=instance_ids).stop()
    return json.dumps({'message': 'Running EC2 instances are stopping...'})


def delete_instance(instance_id):
    instance = ec2.Instance(instance_id)
    response = instance.terminate()
    return json.dumps({'message': f'EC2 instance {instance_id} is being terminated.'})


# print(stop_all_instances())

#delete_instance('i-016a446f303b6ff02')
# create_instance()


# response = ec2.create_key_pair(KeyName='Tutorial')
# ec2_client = aws_session.client('ec2')
# print(ec2_client.describe_key_pairs())

print(json.loads(get_all_instances()))
