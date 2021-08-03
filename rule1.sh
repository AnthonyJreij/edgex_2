curl -X POST \
  http://172.17.37.234:48075/rules \
  -H 'Content-Type: application/json' \
  -d '{
  "id": "rule2",
  "sql": "SELECT int16 FROM demo WHERE int16 > 7000",
  "actions": [
    {
      "rest": {
        "url": "http://edgex-core-command:48082/api/v1/device/httpSub1/command/stop",
        "method": "put",
        "dataTemplate": "{\"Bool\":\"false\", \"stopSub\": \"false\"}",
        "sendSingle": true
      }
    },
    {
      "log":{}
    }
  ]
}'