# python
Python script which uses Instance metadata, gathers the required information about an instance, then saves all collected data to a file and place the file in S3 bucket.

Stores info like:
- Instance ID: 
- Public IP: 
- Private IP: 
- Security Groups: (list)
- Operating System: (name and version from /etc/os-release file)
- Users: (list of users with permissions to bash or sh shells)
