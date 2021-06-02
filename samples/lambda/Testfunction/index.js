exports.handler = async (event) => {
    
    var start = Date.now() / 1000;
    var end = start + 1;
    var test = {
     "returncode": 0,
     "stdout": "lambda stdout",
     "stderr": "lambda stderr",
     "start_time": start,
     "end_time": end,
     "message": "Command message from lambda",
     "unit": "ms",
     "value": Math.floor(Math.random() * (1000 - 50 + 1) + 50);,
     "javascript": true,
     "args": event,
    }

    return test;
};
