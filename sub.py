import requests
import json
import time


edgex_url = 'http://172.17.37.234:49986/api/v1/resource/httpSub1'
pi_url = 'http://192.168.1.35:5000'


def depth():
  depth = requests.get(pi_url + '/depth')
  print('Depth:')
  print(depth.text)
  print(depth.status_code)
  print(depth.reason)
  print()
  data = json.loads(depth.text)
  push(data, '/subDepth')


def pressure():
  pressure = requests.get(pi_url + '/pressure')
  print('Pressure:')
  print(pressure.text)
  print(pressure.status_code)
  print(pressure.reason)
  print()
  data = json.loads(pressure.text)
  push(data, '/subPressure')


def push(x, ext):
  r = requests.post((edgex_url + ext), data=json.dumps(x), verify=False)
  print('Pushing data to edgex')
  print(r.status_code)
  print(r.reason)
  print()


def status():
  x = requests.get(pi_url + '/status')
  if x.text == 'False':
    return False
  else:
    return True


def reset():
  x = requests.get(pi_url + '/reset')
  print(x.status_code)
  print(x.text)


def main():
  stat = True
  while(1):
    depth()
    pressure()
    stat = status()
    time.sleep(10)
  print('WARNING: Maximum external pressure exceeded')
  reset()
  
main()
