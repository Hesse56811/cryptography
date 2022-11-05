import hashlib

hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())