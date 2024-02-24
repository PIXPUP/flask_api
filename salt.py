import random

class generate_salt:
    def saltting():
        chars = []
        ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$^&*_-+=?;:'"
        for i in range(20):
            chars.append(random.choice(ALPHABET))
        r ="".join(chars)
        chars=[]
        return r

generate_salt.saltting()