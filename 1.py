class Avto:
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1
    def __str__(self):
        return f"Avto: {self.make} {self.model}"

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)