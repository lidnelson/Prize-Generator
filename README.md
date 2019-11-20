# QA Group Project
Aim of the project is to generate a web-based application which generates a unique User ID from a set of random generated numbers & letters, additionally the user is presented with a prize after they enter their full name.

## Getting Started
This README will guide you on how to get a copy of the project up, running and deployed on a live AWS system.

## Creating a AWS Account
[If you haven't got a AWS Account already, follow this link on how to create one.](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)

## IAM Roles
[Link to instructions on how to create an IAM Role](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)

Ensure the following parameters are the same:

**Page - (Create role)** Select type of trusted entity: AWS service

**Page - (Create role)** Choose the service that will use this role: EC2

**Page - (Attach permissions policies)** Search for "AmazonRDSDataFullAccess", "AmazonRDSFullAccess", "AWSLambdaFullAccess", and make sure the checkbox is highlighted before moving on to next page

**Page - (Add tags)** Key: Name, Value: EC2-Access

**Page - (Review)** Role name: EC2-Permissions

**Page - (Review)** Role description: *Specify a description of your choice*

*Parameters that are not listed here should be kept at the default value*

## EC2 Instance
[Link to instructions on how to create an EC2 Instance](https://docs.aws.amazon.com/efs/latest/ug/gs-step-one-create-ec2-resources.html)

Ensure the following parameters are the same:

**Page - (Amazon Machine Image (AMI))**: Select the first option

**Page - (Instance type)**: t2.micro

**Page - (Configure Instance Details)** Auto-assign public IP: Enable

**Page - (Configure Instance Details)** IAM role: EC2-Permissions

**Page - (Add Tags)** Key: Name Value: EC2-Instance, *or any name of your liking*

**Configure Security Group** Assign a security group: create a **new** security group, **Security group name:** EC2-CONNECT-APP,   **Security group name:** EC2-CONNECT-APP 

**Configure Security Group** Add new rules, Type: HTTP, MYSQL/Aurora. Source for both: 0.0.0.0/0 

*Parameters that are not listed here should be kept at the default value*

## Creating Database
[Link to instructions on how to create an RDS DB Instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateDBInstance.html)

Ensure these parameters are the same:

**Engine type:** MySQL

**Version:** MySQL 5.7.26

**Templates:** Free tier

**Settings, DB instance identifier // Master username // Master password:** sqldatabase *or your own choice, ensure to note down 
these values.*

**Virtual Private Cloud (VPC):** Default VPC

**Additional connectivity configration, Publicly accessible:** No

**VPC security group: Choose existing,** select the pre-made VPC group you created earlier "EC2-CONNECT-APP"

*Parameters that are not listed here should be kept at the default value*

## Lambda Function
[Link to instructions on how to create a Lambda Function](https://docs.aws.amazon.com/lex/latest/dg/gs-bp-create-lambda-function.html)

You will need to create 3 lambda functions for this application to work

**Lambda Function 1**

**Basic information** Function name: randomprize

**Basic information** Runtime: Python 3.7

Copy and paste the code from the randomprize_lambda.py file into the function code

**Lambda Function 2**

**Basic information** Function name: randomletter

**Basic information** Runtime: Python 3.7

Copy and paste the code from the randomprize_letter.py file into the function code

**Lambda Function 3**

**Basic information** Function name: randomnumber

**Basic information** Runtime: Python 3.7

Copy and paste the code from the randomprize_number.py file into the function code

*Parameters that are not listed here should be kept at the default value*

## Edit Files
Rename the config file and remove the *"_sample"* from the file name

Within the config file specify a SECRET KEY which is a string of length 30 that has both numbers and letters

Edit the config file and specify the Database URI: 'mysql+pymysql://[master username]:[master password]@[database endpoint]/[database name]

# EC2 Console
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

.
.
.

Create a database called Prizes
```
$ mysql -h [database endpoint] -P 3306 -u [database name] -p
$ MySQL [(none)]> CREATE database Prizes;
$ MySQL [(none)]> exit;
```
Import prize table into the newly created Prizes Database
```
$ mysql -h [database endpoint] -P 3306 -u [database name] -p Prize < prizes.sql
```

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
$ mysql -h [database endpoint] -P 3306 -u [database name] -p
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
$ MySQL [(Prizes)]> SELECT * FROM prizes;
```

## Built With

* [VirtualBox](https://www.virtualbox.org/wiki/Downloads) - VirtualBox used
* [Amazon Web Service](https://aws.amazon.com/) - Cloud computing platform used
* [Sublime](https://www.sublimetext.com/3) - Text editor

## Authors

* **Solomon Bada**
