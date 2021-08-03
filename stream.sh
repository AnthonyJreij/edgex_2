curl -X POST \
  http://$kuiper_docker:48075/streams \
  -H 'Content-Type: application/json' \
  -d '{"sql": "create stream demo() WITH (FORMAT=\"JSON\", TYPE=\"edgex\")"}'