import hashlib
name = input('Input your word:')
md5hash = hashlib.md5(name.encode('utf-8')).hexdigest()
#md5hash = hex
print (md5hash)
