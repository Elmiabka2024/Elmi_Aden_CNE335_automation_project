## EC2 instance ping final automation project for CNE335
# project overview
This is the final project for CNE335 and focuses on python scripts that pings an EC2 instance to check its availability
# Task
ping an Ec2 server and run SSH commands using paramiko library for SSH communication and os for pinging
# problems you my encounter 
paramiko library does not support .ppk file. convert it to .pem using the following steps

open Puttygen and load the .ppk file
from the conversion menu, choose Export OpenSSH key and save it as a .pem file.
you will also need to update your file path to reflect to the correct path of .pem.

Troubleshoot the EC2 security group settings to ensure the EC2 instance's security group allows inbound traffic on port 22 for ssh.
![image alt](https://github.com/Elmiabka2024/Elmi_Aden_CNE335_automation_project/blob/f97dce8d2bcf92643d989003dca8df4cf03e07a8/final_project_ec2-connection.jpg)


![image alt](https://github.com/Elmiabka2024/Elmi_Aden_CNE335_automation_project/blob/fcfe043765f156fe9f282d50a4340b80673f5eff/ec2_ping.jpg)
