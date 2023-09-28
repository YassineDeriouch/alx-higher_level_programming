#!/bin/bash
# bash script that makes a request to show custom response
curl -sLX GET -H "Host: 0.0.0.0:5000" -H "User-Agent: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
