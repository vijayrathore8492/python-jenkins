from jenkinsapi.jenkins import Jenkins
import sys
import sqlite3
import time
from requests import exceptions

def get_server_instance(args):
    """
    Connect to give jenkins status.
    """
    try:
        jenkins_url = args[1]
        username = args[2]
        password = args[3]
    except IndexError:
        sys.exit("Run with correct parameters. eg.`python3 manage.py http://instance username paswword`")
    try:
        server = Jenkins(jenkins_url, username=username, password=password)
    except exceptions.HTTPError:
        sys.exit("Unable to connect to given jenkins instance.")
    except exceptions.MissingSchema:
        sys.exit("Invalid jenkins instance given.Please correct")
    except exceptions.ConnectionError:
        sys.exit("Unable to connect to given jenkins instance.")
    return server

def get_job_details(args):
    """
    Get details of all jobs and call function to store in database
    """
    # Get jenkins instance
    server = get_server_instance(args)
    
    # Get status of all jobs
    jobs = []
    for job_name, job_instance in server.get_jobs():
        params = {}
        params['name'] = job_instance.name
        params['description'] = job_instance.get_description()
        params['is_running'] = 1 if job_instance.is_running() else 0
        params['is_enabled'] = 1 if job_instance.is_enabled() else 0
        params['is_queued'] = 1 if job_instance.is_queued() else 0
        jobs.append(params)
    
    #if jobs got saved in db or not
    if save_in_database(jobs):
        print("Job status added in database successfully.")
        sys.exit(0)
    else:
        sys.exit("Failed to save jobs in database")

def save_in_database(jobs):
    #connect db
    conn = sqlite3.connect('jenkins_job.db')

    # Insert data
    try:
        for params in jobs:
            args = (params['name'], params['is_running'], params['is_queued'], params['is_enabled'], int(time.time()))
            conn.execute("INSERT INTO jobs (name,is_running,is_queued,is_enabled,timestamp) VALUES (?,?,?,?,?)",args)
        # Save (commit) the changes
        conn.commit()
    except:
        #Roll back if error
        conn.rollback()
        return False
    else:
        #close connection
        conn.close()
    return True
        

if __name__ == '__main__':
    get_job_details(sys.argv)