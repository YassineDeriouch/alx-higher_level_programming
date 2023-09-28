#!/bin/bash
# bash script that makes a request to show custom response
curl -sLX PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
