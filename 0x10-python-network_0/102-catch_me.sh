#!/bin/bash
# bash script that makes a request to show custom response
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin:You got me!"
