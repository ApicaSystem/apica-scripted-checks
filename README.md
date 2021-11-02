# cbt-demo-run-anything

See samples directory for java, javascript, and python samples.


All Run Anything scripts should produce JSON that corresponds to the following example:

```json
{
  "returncode":0,
  "stdout":"Stdout from java",
  "start_time":1622120634,
  "value":"0",
  "end_time":1622120638,
  "stderr":"Stderr from java",
  "message":"HTTP Call completed with status OK",
  "metrics":{
    "duration":0,
    "content_size":1256,
    "header_count":11,
    "http_status":200
  }
}
```

# JSON Restrictions
## Keys with dots (.) or dollar signs ($)
Keys with these characters are not currently allowed. Results with these keys will be discarded by our system. We may implement a replacement system where these are replaced with another character.


# Important Fields
## Start time and end time
start_time and end_time are important fields as they define when your check started and stopped it's run. These must be set to unix epoch in **seconds**. If you do not set this value your check will be sent back in time to 1970. If you set this to a value in the future your check result will be discarded by our system.

As an alternative to this field you may use the start_timestamp_ms and end_timestamp_ms fields. If you use these fields your values should be in milliseconds rather than seconds. 

**No matter which fields you use your values should be whole numbers**

## Return Code
returncode controls whether your script succeeded or failed. If you return a value other than 0 it indicates your script failed.

## Value
value is an important field, it should be parseable as an integer, it will be displayed in ASM as the main return value of your script.

## Metrics Object
The metrics object can contain any number of entries, all values should be positive integers, these metrics will be aggregated in the ASM backend and saved in our metric storage collection.

## Expandable JSON
You may add any new fields to your JSON, these fields can be simple or as complex as new objects. This data will be saved into your final result in the "custom_fields" JSON object.
