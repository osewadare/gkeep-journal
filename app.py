import json
import gkeepapi
from urllib.request import urlopen, Request
from base64 import b64encode, b64decode
from datetime import datetime
import boto3


#Set config
keep_journal_prefix = 'JotSync-Journal'
github_commit_name = 'Dare Osewa'
github_commit_email = 'osewa.dare@gmail.com'
github_commit_url = 'https://api.github.com/repos/osewadare/jotsync/contents/_posts'
github_commit_message = 'New journal post'



def lambda_handler(event, context):
    ssm = boto3.client('ssm')
    email_param_response = ssm.get_parameter(Name='gkeep-journal/gmail')
    email_parameter_value = email_param_response['Parameter']['Value']
    password_param_response = ssm.get_parameter(Name='gkeep-journal/gpassword')
    password_parameter_value = password_param_response['Parameter']['Value']
    keep = gkeepapi.Keep()
    success = keep.login(email_parameter_value, password_parameter_value)
    publish_journal(keep, ssm)


def publish_journal(keep, ssm):
    gnotes = keep.find(func=lambda x: x.title == keep_journal_prefix)
    date = datetime.now().strftime("%Y-%m-%d")
    try: 
        note = next(gnotes)
    except StopIteration:
        return {
            'statusCode': "304",
            }
    title = f'{note.title}-{note.timestamps.updated.strftime("%d-%h-%Y-%H:%M")}'
    post = f'''---
title: "{title}"
date: {date}
---
{note.text}
    '''
    github_pat_param_response = ssm.get_parameter(Name='gkeep-journal/github-pat')
    github_pat_parameter_value = github_pat_param_response['Parameter']['Value']
    headers = {
        'content-type':'application/json',
        'authorization': f"Basic {str(b64encode(bytes(github_pat_parameter_value, 'utf-8')), 'utf-8')}"
        }
    
    request = {'message':{github_commit_message},'committer':{'name': github_commit_name,'email':{github_commit_email}},'content':str(b64encode(bytes(post, 'utf-8')), 'utf-8')}

    resp = urlopen(Request(f'{github_commit_url}/{date}-{title}.md', 
                           headers=headers,
                           method='PUT',
                           data = bytes(json.dumps(request), 'utf-8')))
    if (resp.status == 201):
        {
            note.trash()
        }
    keep.sync()
    return {
        'statusCode': resp.status,
    }
    
