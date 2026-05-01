import random

passLength = int(input("Parolanızın uzunuluğu (karakter sayısı): "))
availableChars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

for i in range(passLength):
    randomPass = random.choice(availableChars)
    print(randomPass, end="")
