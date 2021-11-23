import requests
from argparse import ArgumentParser
import json
import time

parse = ArgumentParser()
parse.add_argument('-t', '--tags', default='')
parse.add_argument('-ct', '--critical-tags', default='', required=False)
parse.add_argument('-a', '--auth-ticket')
args = parse.parse_args()

tags = str(args.tags).split(',')
crit_tags = []

json_payload = {
    "check_tags": {
        "include_tag": tags
    },
    "stale_timeout_ms": 3600000
}

if args.critical_tags:
    crit_tags = str(args.critical_tags).split(',')
    critical_tags_dict = {
        'critical_check_tags': {
            'include_tag': crit_tags
        }
    }
    json_payload.update(critical_tags_dict)


url = 'https://api-wpm1.apicasystem.com/v3/checks/composite_result'
params = {'auth_ticket': args.auth_ticket}
headers = {'Accept': 'application/json', 'Content-type': 'application/json'}

start = time.time()
response = requests.post(url, params=params, headers=headers, json=json_payload).json()
end = time.time()

uptime_ratio = int(response.get('uptime_ratio'))
return_code = 0

if uptime_ratio < 60:
    return_code = 1

print(json.dumps({
    'start_time': start,
    'end_time': end,
    'value': int(uptime_ratio),
    'message': 'Business composite check has result: ' + str(uptime_ratio),
    'returncode': return_code,
    'included_tags': tags + crit_tags,
    'response': response,
    'metrics': {
        'uptime_score': int(response.get('uptime_score')),
        'downtime_score': int(response.get('downtime_score')),
        'stale_checks': response.get('checks_stale')
    }
}))
