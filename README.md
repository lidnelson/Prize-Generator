# Project Title
QA Group Project 
Aim of the project is to generate a web-based application which generates a unique User ID from a set of random generated numbers & letters, additionally the user is presented with a prize after they enter their full name.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system (AWS).

# Local Machine
### Prerequisites
Software needed & installation process.
### Automatic Process
System Update
```
$ sudo yum update -y
```
Git clone the project repository onto the EC2 Instance & move into the the Prize-Generator directory
```
$ git clone -b solomon https://github.com/lidnelson/Prize-Generator
$ cd Prize-Generator
```
Run mysql.sh which consists of all required process needed to be installed
```
$ sh mysql.sh
```
### Manual Process
System Update
```
$ sudo yum update -y
```
Git
```
$ sudo yum install git
```
MySQL Server
```
$ sudo yum install mysql -y
```
Docker
```
$ sudo amazon-linux-extas install docker
$ sudo service docker start
$ sudo usermod -aG docker ec2-user
```
Docker Compose
```
$ sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null
$ sudo chmod +x /usr/local/bin/docker-compose
```


### Installing

A step by step series of examples that tell you how to get a development env running

Git clone the project repository onto the EC2 Instance & move into the the Prize-Generator directory

```
$ git clone -b solomon https://github.com/lidnelson/Prize-Generator
$ cd Prize-Generator
```

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Deploying the application

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

Navigate to http://{{ External IP address }}/


## Running the application

Add additional notes about how to deploy this on a live system

### Viewing the application

Explain what these tests test and why

```
Give an example
```

# AWS
### Prerequisites
Software needed & installation process.
### Automatic Process
System Update
```
$ sudo yum update -y
```
Git clone the project repository onto the EC2 Instance & move into the the Prize-Generator directory
```
$ git clone -b solomon https://github.com/lidnelson/Prize-Generator
$ cd Prize-Generator
```
Run mysql.sh which consists of all required process needed to be installed
```
$ sh mysql.sh
```
### Manual Process
System Update
```
$ sudo yum update -y
```
Git
```
$ sudo yum install git
```
MySQL Server
```
$ sudo yum install mysql -y
```
Docker
```
$ sudo amazon-linux-extas install docker
$ sudo service docker start
$ sudo usermod -aG docker ec2-user
```
Docker Compose
```
$ sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null
$ sudo chmod +x /usr/local/bin/docker-compose
```


### Installing

A step by step series of examples that tell you how to get a development env running

Git clone the project repository onto the EC2 Instance & move into the the Prize-Generator directory

```
$ git clone -b solomon https://github.com/lidnelson/Prize-Generator
$ cd Prize-Generator
```

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Deploying the application

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

Navigate to http://{{ External IP address }}/

## Built With

* [VirtualBox](https://www.virtualbox.org/wiki/Downloads) - VirtualBox used
* [Amazon Web Service](https://aws.amazon.com/) - Cloud computing platform used
* [Sublime](https://www.sublimetext.com/3) - Text editor

## Authors

* **Solomon Bada**
* **Lydia Nelson**
