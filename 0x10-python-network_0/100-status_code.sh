#!/bin/bash
#bash script send a request to an URL to displays only the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
