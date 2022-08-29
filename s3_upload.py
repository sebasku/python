import csv
from path import Path

import boto3
from ec2_metadata import ec2_metadata

import pwd

def get_operating_system():
    with open(Path('/etc/os-release')) as csvfile:
        os_dict = dict(csv.reader(csvfile, delimiter='='))

        return f"{os_dict['NAME']} {os_dict['VERSION']}"


instance_metadata = f"""Instance ID: {ec2_metadata.instance_id}
Public IP: {ec2_metadata.public_ipv4}
Private IP: {ec2_metadata.private_ipv4}
Security Groups: {ec2_metadata.security_groups}
Operating System: {get_operating_system()}
Users: {[p[0] for p in pwd.getpwall() if any(x in p[6] for x in ['/sh', '/bash'])]}
"""

# Save data to s3 text file, expect credentials in .aws folder
file_path = Path('instance_file')
file_path.touch()
file_path.write_text(instance_metadata)

s3 = boto3.resource('s3')

#                   set here s3 bucket and prefix     
s3_object = s3.Object('s3_bucket', f'PREFIX/InstanceData_{ec2_metadata.instance_id}.txt')
s3_object.upload_file(str(file_path))

print(instance_metadata)