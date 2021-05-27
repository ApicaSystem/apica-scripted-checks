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

# Important Fields
## Start time and end time
start_time and end_time are important fields as they define when your check started and stopped it's run. These must be set to unix epoch in **seconds**. If you do not set this value your check will be sent back in time to 1970. If you set this to a value in the future your check result will be discarded by our system.

## Return Code
returncode controls wether your script succeeded or failed. If you return a value other than 0 it indicates your script failed.

## Value
value is an important field, it should be parseable as an integer, it will be displayed in ASM as the main return value of your script.

## Metrics Object
The metrics object can contain any number of entries, all values should be positive integers, these metrics will be aggregated in the ASM backend and saved in our metric storage collection.

## Expandable JSON
You may add any new fields to your JSON, these fields can be simple or as complex as new objects. This data will be saved into your final result in the "custom_fields" JSON object.
