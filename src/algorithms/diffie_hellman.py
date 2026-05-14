#modular exponentiation

def diffie_hellman(p, g, f, s):

    #first person's private key 
    first_private_key = pow(g, f, p) 

    # second person's private key
    second_private_key= pow(g, s, p) 

    # Both compute the shared secret
    person1_secret = pow(second_private_key, f, p) 
    person2_secret = pow(first_private_key, s, p)  

    return person1_secret, person2_secret