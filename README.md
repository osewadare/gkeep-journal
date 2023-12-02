# Description
Lambda that synchronizes Google keep notes with Github pages.  

# Deployment 
Setup your AWS credentials:
`aws configure`  

Build the SAM project 
`sam build`    

Deploy the SAM application
`sam deploy`    

# Dependencies 
Set SSM parameters in AWS all in text/string - https://console.aws.amazon.com/systems-manager/parameters

- gkeep-journal/gmail (Email Address used to login to Google Keep)
- gkeep-journal/gpassword (This is the password created for this app for authentication performed on the Google Account) - Create one here 
- gkeep-journal/github-pat (Personal access token that grants access to Gihub repos)


# Configuration 
- github repo posts url
- github commit name 
- github email 

Learn more - https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#create-or-update-file-contents