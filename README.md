# AWS-Lambda-pingdom-ec2-reboot
A simple Lambda written in Python that reboots a specified EC2 instance when a "down" alert is received by the site monitoring tool Pingdom.

## Usage
The Lambda requires a function URL to act as a trigger and endpoint for the relevant site alert in pingdom. It also needs the following environment variables: 
-Pingdom:pingdom-bot
-InstanceID:<INSERT INSTANCE ID HERE>

## Requirements
- boto3
