# Description
Serverless function that publishes journals from Google keep to Github pages.  Can essentially be used as a private journal without having to create posts/files or write markdown. 

# Deploy Serveless Resources
Setup your AWS credentials:
`aws configure`  

Build the SAM project 
`sam build`    

Deploy the SAM application
`sam deploy`    

# Configure Google Keep Access 
Set SSM parameters - https://console.aws.amazon.com/systems-manager/parameters

- gkeep-journal/gmail (Email Address used to login to Google Keep)
- gkeep-journal/gpassword (This is the password created for this app for authentication performed on the Google Account) - Create one here 
- gkeep-journal/github-pat (Personal access token that grants access to Gihub repos)


# Configure Github settings
Create a github page 
https://github.com/skills/github-pages

Set commit configuration 
- github_commit_name
- github_commit_email
- github_commit_url
- github_commit_message

Learn more about creating files via Github API here - https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#create-or-update-file-contents

# How to use
Create a keep note with the Journal prefix and just write 
Note gets published to your github pages journal