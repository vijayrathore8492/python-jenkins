# Python-Jenkins

Command line script, that uses Jenkins' API to get a list of jobs and their status from a given Jenkins instance.

  - Built on Python3

## Pre-requisities
  - python3
  - virtualenv

## Install pre-requisities [on ubuntu 16.04]
 - sudo apt-get install python3
 - sudo apt-get install python3-pip python3-dev
 - sudo pip3 install virtualenv

## Execution
Once all Pre-requisites are done, Follow below steps to execute

### Clone the repo
 - git clone https://github.com/vijayrathore8492/python-jenkins.git

### Execute script
 - cd python-jenkins
 - virtualenv appenv
 - source appenv/bin/activate
 - pip3 install -r requirements.txt
 - python3 manage.py <jenkins_instance> <username> <password>
  - eg:- python3 manage.py http://localhost:8080 admin admin

## DB tables
### jobs [job status table]
 - id INT PRIMARY KEY
 - instance CHAR(200) NOT NULL
 - name CHAR(100) NOT NULL
 - is_running INT NOT NULL
 - is_queued INT NOT NULL
 - is_enabled INT NOT NULL
 - timestamp INTEGER NOT NULL

## DIR structure
```
 - manage.py                        #Main application logic
 - README.md                        #this
 - jenkins_job.db                   #sqlite DB

```

## PS
  - This is my first script Python. I have tried my best to keep standards but may have missed some.