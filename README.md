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
$ sudo apt-get update -y
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

### Installing

A step by step series of examples that tell you how to get a development env running

Move into the the Prize-Generator directory
```
$ cd Prize-Generator
$ sudo apt-get install python3 -y
$ sudo apt-get install python3-pip -y
$ sudo apt-get install python-virtualenv
$ python3 -m venv venv
$ . venv/bin/activate
$ pip3 install -r requirements.txt

```

End with an example of getting some data out of the system or using it for a little demo

## Deploying the application

Run the following command to build the application

```
$ cd ..
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
$ flask run
```
### Viewing the application

Navigate to http://localhost:5000/

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
