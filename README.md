# Project Title
QA Group Project 
Aim of the project is to generate a web-based application which generates a unique User ID from a set of random generated numbers & letters, additionally the user is presented with a prize after they enter their full name.

## Getting Started
These instructions will get you a copy of the project up and running and deployed on a live AWS system.

## Creating a AWS Account
If you haven't got a AWS Account already, follow the link on how to create one.
[How to create AWS Account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)


## IAM Roles
This section will instruct you on how to setup the IAM roles
[Create an IAM Role](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)

**Create role** Select type of trusted entity: AWS service
**Create role** Choose the service that will use this role: EC2
**Attach permissions policies** Search for "AmazonRDSDataFullAccess", "AmazonRDSFullAccess", "AWSLambdaFullAccess", and make sure the checkbox is highlighted before moving on to next page
**Add tags** Key: Name, Value: EC2-Access
**Review** Role name: EC2-Permissions
**Review** Role description: *Specify a description of your choice*

Ensure these parameters are the same:

## Lambda Function
Section will instruct you on how to create the lambda functions
[Create a Lambda Function](https://docs.aws.amazon.com/lex/latest/dg/gs-bp-create-lambda-function.html)


## EC2 Instance
This section will instruct you on how to create an EC2 instance.
[Create an EC2 Instance](https://docs.aws.amazon.com/efs/latest/ug/gs-step-one-create-ec2-resources.html)

Ensure these parameters are the same:

Amazon Machine Image (AMI): Select the first option
Instance type: t2.micro
**Configure Instance Details** Auto-assign public IP: Enable
**Configure Instance Details** IAM role: EC2-Permissions
**Add Tags** Key: Name Value: First or any name of your liking
**Configure Security Group** Add new rules, Type: HTTP, MYSQL/Aurora. Source for both: 0.0.0.0/0 

# AWS
### Prerequisites
Software needed & installation process.

System Update
```
$ sudo yum update -y
```
Git clone the project repository onto the EC2 Instance & move into the the Prize-Generator directory
```
$ git clone -b https://github.com/lidnelson/Prize-Generator
$ cd Prize-Generator
```
Run mysql.sh which consists of all required process needed to be installed
```
$ sh mysql.sh
```
After the shell script file has been launched, reboot the EC2 instance to ensure docker commands can be ran without 'Sudo' command.

## Creating Database
This section will guide you on how to create a database and link to it
[Create an RDS DB Instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateDBInstance.html)

Ensure these parameters are the same:

Engine type: MySQL
Version: MySQL 5.7.26
Templates: Free tier
Settings, DB instance identifier // Master username // Master password: mysqldatabase or your own choice, ensure to note down these values.
Virtual Private Cloud (VPC): Default VPC
Additional connectivity configration, Publicly accessible: No
VPC security group: Choose existing, select the pre made VPC group you created earlier "EC2-CONNECT-APP"

Parameters that are not listed should be kept at the default value

Create a database called Prizes
```
$ mysql -h [mysql endpoint] -P 3306 -u [sql database name] -p
$ MySQL [(none)]> CREATE database Prizes;
$ MySQL [(none)]> exit;
```
Create a database called Prizes
```
$ MySQL [(none)]> CREATE database Prizes;
```
Exit out of MySQL
```
$ MySQL [(none)]> exit;
```
Import prize table into the newly created Prizes Database
```
$ mysql -h [mysql endpoint] -P 3306 -u [sql database name] -p Prize < prizes.sql
```

### Edit Files

Edit config file and specify a random 18 character secret key
import the database uri in a similar fashion to ..

### Deploying the application

Run the following command to build the application using docker compose
```
$ docker-compose up -d --build
```
Check that the application has been successfully built without any erorrs
```
$ docker-compose logs app
```
View the application container and the the corresponding details
```
$ docker ps
```
### Viewing the application

Obtain the EC2 IPv4 Public IP, copy & paste into your web browser.

### Viewing the database

To view your database, enter the following command into your CLI & enter your password upon request
```
$ mysql -h [mysql endpoint] -P 3306 -u [sql database name] -p
```
Show databases
```
$ MySQL [(none)]> show databases;
```
Use database
```
$ MySQL [(none)]> Use Prizes;
```
View entries in database
```
$ MySQL [(none)]> SELECT * FROM prizes;
```


## Built With

* [VirtualBox](https://www.virtualbox.org/wiki/Downloads) - VirtualBox used
* [Amazon Web Service](https://aws.amazon.com/) - Cloud computing platform used
* [Sublime](https://www.sublimetext.com/3) - Text editor

## Authors

* **Solomon Bada**
* **Lydia Nelson**
