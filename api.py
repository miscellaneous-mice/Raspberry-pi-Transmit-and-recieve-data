import requests
r =requests.get('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=U8BPF72VJYF3AVM3')
print r.text
