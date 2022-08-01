# 22-dars: args va kwargs


def summa(x,y,*sonlar):
    return x+y+sum(sonlar)

print(summa(1,2))
print(summa(1,2,3,4,5))
print(summa(4,5,6,7))