import hashlib

# print(hashlib.algorithms_guaranteed)

#{'shake_128', 'sha224', 'sha256', 'sha3_384', 'shake_256', 'sha3_256', 'sha384', 'sha1', 'sha3_224', 'blake2s', 'sha512', 'md5', 'sha3_512', 'blake2b'}


def sha256(text):
    sha256_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()

    return sha256_hash

def sha512(text):
    sha512_hash = hashlib.sha512(text.encode('utf-8')).hexdigest()

    return sha512_hash

def sha3_512(text):
    sha3_512_hash = hashlib.sha3_512(text.encode('utf-8')).hexdigest()

    return sha3_512_hash

def shake_256(text):
     shake_256 = hashlib.shake_256(text.encode('utf-8')).hexdigest(32)

     return shake_256

def blake2b(text):
    blake2b = hashlib.blake2b(text.encode('utf-8')).hexdigest()

    return blake2b