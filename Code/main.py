# stars v1.2
inp = ""
stars = ""
num: int = 0
amntStars: int = 0
try:
    inp = input("Type how large you want the base to be:")
except:
    print("Error, failed to accept your input")
num = inp

try:
    while int(num) >= amntStars:
        stars = stars + "*"
        print(stars)
        amntStars = amntStars + 1
        if int(num) == amntStars:
            break
except:
    print("ERROR: prolly an invalid number")



