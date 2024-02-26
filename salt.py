import random
from werkzeug.security import generate_password_hash

class gen_pass:
    def saltting(password):
        chars = []
        ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$^&*_-+=?;:'"
        for i in range(20):
            chars.append(random.choice(ALPHABET))
        salt ="".join(chars)
        pass_hash = generate_password_hash(salt+password)
        chars=[]
        return salt,pass_hash
