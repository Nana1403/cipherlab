from flask import Flask, render_template, request
from algorithms.rsa import rsa
from algorithms.caesarcipher import encryption, decryption, brute_force
from algorithms.vigenerecipher import vigenere
from algorithms.shahashing import sha256, sha3_512, shake_256, sha512, blake2b
from algorithms.diffie_hellman import diffie_hellman
from algorithms.aes import encrypt, decrypt

main =  Flask(__name__)


@main.route('/', methods=["GET", "POST"])
def  mainage():
     if request.method == "GET":
        return render_template("mainpage.html")
     
     
     return render_template("mainpage.html")


@main.route('/rsa-page', methods=["GET", "POST"])
def rsa_page():
     if request.method == "GET":
        return render_template("rsa.html")
     
     action = request.form.get("action")
     
     if action == "rsa":
        p = int(request.form.get('p'))
        print(request.form)
        q = int(request.form.get('q'))
        e = int(request.form.get('e'))
        m = int(request.form.get('m'))
        result = rsa(p, q, e, m)
     return render_template("rsa.html", results=result)


@main.route('/cc-page', methods=['GET', 'POST'])
def cc_page():
     if request.method == "GET":
        return render_template("cc.html")

     action = request.form.get("action")

     if action == "encryption":
        message = list(request.form["message"])
        key = int(request.form["key"])
        result = encryption(message, key)
        return render_template("cc.html", results=result, message=message, key=key)

     elif action == "decryption":
        message = list(request.form["message"])
        key = int(request.form["key"])
        result = decryption(message, key)
        return render_template("cc.html", results=result, message=message, key=key)

     elif action == "brute-force":
        message = list(request.form["message"])
        results_list = brute_force(message)
        return render_template("cc.html", results_bf=results_list, message=message)

        
     return render_template("cc.html")

@main.route('/vc-page', methods=['GET', 'POST'])
def vc_page():
     if request.method == "GET":
        return render_template("vc.html")
     
     action = request.form.get("action")

     if action == "vc":
        text = request.form.get('text')
        key = request.form.get('key')
        e_or_d = request.form.get('e_or_d')
        results = vigenere(text, key, e_or_d)
        print(results)
        print("ACTION:", action)
        return render_template("vc.html", results=results)
     
     return render_template("vc.html")

@main.route('/dh-page', methods=['GET', 'POST'])
def dh_page():
     if request.method == "GET":
        return render_template("dh.html")
       
     action = request.form.get('action')

     if action == "dh":
        p = int(request.form.get('p'))
        g = int(request.form.get('g'))
        f = int(request.form.get('f'))
        s = int(request.form.get('s'))
        results = diffie_hellman(p, g, f, s)
        return render_template("dh.html", results=results)
     
     return render_template("dh.html", results=results)


@main.route('/aes-page', methods=['GET', 'POST'])
def aes_page():
     if request.method == "GET":
        return render_template("aes.html")
     
     action = request.form.get('action')
     if action == "encrypt":
        text = request.form.get('text')
        key_size = int(request.form.get('key_size'))
        encrypt_results = encrypt(text, key_size)
        return render_template("aes.html", encrypt_results=encrypt_results)

     elif action == "decrypt":
         key = int(request.form.get('key'))
         nonce = int(request.form.get('nonce'))
         tag = request.form.get('tag')
         ciphertext = request.form.get('ct')
         decrypt_results = decrypt(key, nonce, tag, ciphertext)
         return render_template("aes.html", decrypt_results=decrypt_results)
     
     return render_template("aes.html")


@main.route('/sha-hashing-page', methods=['GET', 'POST'])
def sha_hashing_page():
     if request.method == "GET":
        return render_template("sha-hashing.html")
     
     action = request.form.get('action')
      
     if action == "sha256": 
        text = request.form.get('text')
        results = sha256(text)
        return render_template('sha-hashing.html', results=results)

     elif action == "sha512":
        text = request.form.get('text')
        results = sha512(text)
        return render_template('sha-hashing.html', results=results)
   
     elif action == "sha3_512":
        text = request.form.get('text')
        results = sha3_512(text)
        return render_template('sha-hashing.html', results=results)
        
     elif action == "shake256":
        text = request.form.get('text')
        results = shake_256(text)
        return render_template("sha-hashing.html", results=results)
     
     elif action == "blake2b": 
        text = request.form.get('text')
        results = blake2b(text)
        return render_template("sha-hashing.html", results=results)

     return render_template("sha-hashing.html", results=results)

if __name__ == "__main__":
     main.run(debug=True)