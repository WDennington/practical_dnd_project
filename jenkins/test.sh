#!/bin/bash

# install app dependencies
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv y

#creat and source virtual enviroment
python3 -m venv venv
source venv/bin/activate

#install pip requirements
pip3 install -r jenkins/requirements.txt

#run pytest
python3 -m pytest 5000_templates --cov=5000_templates --cov-report=html --junitxml=junit/test-results1.xml --cov-report=xtml
python3 -m pytest 5001_name_class --cov=5001_name_class --cov-report=html --junitxml=junit/test-results2.xml --cov-report=xtml
python3 -m pytest 5002_stats --cov=5002_stats --cov-report=html --junitxml=junit/test-results3.xml --cov-report=xtml
python3 -m pytest 5003_character --cov=5003_character --cov-report=html --junitxml=junit/test-results4.xml --cov-report=xtml
