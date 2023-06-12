# Scan service simulator

1. Get session token:

Method

POST

URL

http://localhost/api/v1/authn

Data

{"username":"sampleUsername", "password":"somepass"}

Response:
{
    "sessionToken": "DummyTOKEN",
    "status": "Success"
}

Test By

curl -X POST http://localhost/api/v1/authn -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"username\": \"sampleUsername\",\"password\":\"samplePassword\"}" -o sessiontoken.json


2. Get access token:

Method

POST

URL

http://localhost/token

Data

{"sessionToken": "<<session token>>"}

Response:

{
    "access_token": "DummyTOKEN",
    "success": true
}

{
    "error": "the request failed",
    "success": false
}

Test By

curl -X POST http://localhost/token -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"sessionToken\": \"13456666666666ffghhhhhh\"}" -o accesstoken.json

 
3. scan repo

Method

POST

URL

http://localhost/api/v1/scans/repo

HEADER

'Authorization: <<access token>>'

Data

{"repoURL": "https://github.com/kumvijaya/ansible-samples.git", "scanBranch": "master", "tag": "static", "patUserId":"kumvijaya", "paToken": "ghp_awfawfwfwefewfwegfew123", }

Response

{
    "jobID": "1234",
    "success": true
}

{
    "jobID": "",
    "success": false
}


Test By

curl -X POST http://localhost/api/v1/scans/repo -H  "accept: application/json" -H  'Authorization: eygsdgsdgdfgdfgdfgdfgdf' -H  "Content-Type: application/json" -d "{\"repoURL\": \"https://github/repo.git\",\"scanBranch\":\"master\",\"tag\":\"secret\",\"patUserId\":\"uer123444\",\"paToken\":\"ghp_reterertt44\"}" -o scan.json

4. scan status

Method

POST

URL

http://localhost/api/v1/scans/status

HEADER:

'Authorization: <<access token>>'

Data:

{"jobID": "<<job id>>"}

Response
{
    "status": "Submitted"
}

OR

{
    "status": "Finished"
}

curl -X POST http://localhost/api/v1/scans/status -H  "accept: application/json" -H  'Authorization: eyeseegegrgdgdff' -H  "Content-Type: application/json" -d "{\"jobID\": \"1234\"}" -o scanstatus.json

5. scan report

Method

POST

URL

http://localhost/api/v1/scans/report

HEADER

'Authorization: <<access token>>'

Data

{"jobID": "<<job id>>"}

Response

[	
    {
          "jobID":"1234",
	   "summary.count":123
    }
]

Test By

curl -X POST http://localhost/api/v1/scans/report -H  "accept: application/json" -H  'Authorization: eyedrhdfdfhdfdgdh' -H  "Content-Type: application/json" -d "{\"jobID\": \"1234\"}" -o scanresult.json