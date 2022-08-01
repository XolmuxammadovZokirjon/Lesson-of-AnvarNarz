with open("pi.txt") as file:
    pi = file.read()
    
print(pi)
file.close()
pi = pi.rstrip()    