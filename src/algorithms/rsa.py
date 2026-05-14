"""
- Number Theory (The foundation)
- Euclidean Algorithmn (EA) -> gcd(a,b)=gcd(b,amodb)
- Extended Euclidean Algoritmn (EEA) -> ax+by=gcd(a,b)
- Modular Arithmetic (mod N)
- Modular Inverse
- RSA

"""

def rsa(p , q , e , message_int): 
    # n 
    n = p * q
    print(n)
    
    # ϕ(n)
    o_n = (p - 1) * (q - 1)
    print(o_n)

    # # e
    # answer = math.gcd(e, o_n)
    # print(f"gcd({e},{o_n}) = {answer}")
   
   #finding d
    d = pow(e, -1, o_n)

    # Encryption: m^e % n
    encrypted = pow(message_int, e, n)
    
    # Decryption: c^d % n
    decrypted = pow(encrypted, d, n)

    #Keys
    print("Keys 🔑")
    print(f"Public Key: (e,n) = ({e}, {n})")
    print(f"Private Key: (d,n) = ({d}, {n})")
    
    return f"Encrypted message: {encrypted}, Decrypted ciphertext: {decrypted}"
