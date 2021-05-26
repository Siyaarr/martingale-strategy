import hashlib

server_seed = "49dd413ab6beba5dc9d92bfc64fba04981336fc252c9737c17916d4ebde35125"
public_seed = "3420053526"
round = "6302656"
line = "-"

combinedString = server_seed + line + public_seed + line + round

shaVersion = hashlib.sha256(combinedString.encode()).hexdigest()

roll = int(shaVersion[0:8], 16) % 15

print(roll)
