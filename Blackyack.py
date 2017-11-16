from random import shuffle
import time
#deck =["1♡", "2♡", "2♡", "4♡", "5♡", "6♡", "7♡", "8♡", "9♡", "10♡", "J♡", "Q♡", "K♡", "A♡"]
J = 10
Q = 10
K = 10
A = 11
r = 0
resultados = []
ganador = []
ideck = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9 , 10, J, Q, K, A,
        1, 2, 3, 4, 5, 6 ,7 ,8 ,9 , 10, J, Q, K, A,
        1, 2, 3, 4, 5, 6 ,7 ,8 ,9 , 10, J, Q, K, A,
        1, 2, 3, 4, 5, 6 ,7 ,8 ,9 , 10, J, Q, K, A]

deck = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9 , 10, J, Q, K, A,
        1, 2, 3, 4, 5, 6 ,7 ,8 ,9 , 10, J, Q, K, A,
        1, 2, 3, 4, 5, 6 ,7 ,8 ,9 , 10, J, Q, K, A,
        1, 2, 3, 4, 5, 6 ,7 ,8 ,9 , 10, J, Q, K, A]


#manos

manod = []
mano1 = []
mano2 = []
mano3 = []
mano4 = []
mano5 = []

#repartir una a cada uno

def repartir ():
    mano1.append(deck.pop())
    mano2.append(deck.pop())
    mano3.append(deck.pop())
    mano4.append(deck.pop())
    mano5.append(deck.pop())
    manod.append(deck.pop())

#barajar

def barajar ():
    shuffle(deck)

#dealer

def dealer ():
    repartir()
    repartir()
    print("Jugador1   Jugador2   Jugador3   Jugador4   Jugador5   Dealer")
    print("   ▓      "+"     ▓       "+"   ▓       "+"  ▓       "+"  ▓       "+"    ▓"   )
    print( "  ", mano1[0], "        ", mano2[0], "        " , mano3[0], "       " , mano4[0], "      " , mano5[0] , "        ", "▓")


#Players

def player2 ():
    apuestaj2.apostar(n/10)
    while sum(mano2) < 21:
        mano2.append(deck.pop())

def player3 ():
    apuestaj3.apostar(n/2)
    while sum(mano3) < 12:
        mano3.append(deck.pop())

def player4 ():
    apuestaj4.apostar(n/5)
    while sum(mano4) < 15:
        mano4.append(deck.pop())

def player5 ():
    apuestaj5.apostar(n/20)
    while sum(mano5) < 18:
        mano5.append(deck.pop())

def playerd ():
    while sum(manod) < 17:
        manod.append(deck.pop())

#apuestas $$$

class jugadores:
    def __init__(self, mano, saldo):
        self.saldo = saldo
        self.mano = mano
        self.valor = 0
    def apostar(self, monto):
        self.valor = monto
        self.saldo -= self.valor
    def ganarapuesta (self):
        self.saldo += (self.valor*2)
    def __str__(self):
        return("El saldo del %s es de %d" % (self.mano, self.saldo))


#START
#saldo

n = int(input("¿Con qué cantidad quiere entrar a la mesa? Todos los jugadores en la mesa recibirán este valor: "))
apuestaj1 = jugadores("jugador1", n)
apuestaj2 = jugadores("jugador2", n)
apuestaj3 = jugadores("jugador3", n)
apuestaj4 = jugadores("jugador4", n)
apuestaj5 = jugadores("jugador5", n)

#***
print (deck)
barajar()
dealer()


# mostrar mano
d = 1
while sum(mano1) < 21:
    print ("Estas son sus cartas: ")
    print(mano1)
    print(d)
    # apostar


    if d == 1:
        montojug1 = int(input("cuanto quiere apostar? "))
        apuestaj1.apostar(montojug1)
        d = 2

    #jugador robar carta y consultar saldo

    r = int(input("[Presione 3 para consultar su saldo] \n ¿Quiere carta? (Presione 1 para SI ó 2 para NO): "))
    print(apuestaj1)
    if r == 1:
        mano1.append(deck.pop())
        print("Estas son sus nuevas cartas")
        print(mano1)
        print(d)
    elif r == 3:
        print(apuestaj1)
    else:
        print(mano1)

player2()
player3()
player4()
player5()
playerd()

print(apuestaj2)
print(apuestaj3)
print(apuestaj4)
print(apuestaj5)


#Selección de ganador

print("Estos son los valores finales de cada jugador y el ganador de la ronda:")
print("Jugador1     Jugador2    Jugador3     Jugador4     Jugador5     Dealer")
print( "  ", sum(mano1), "        ", sum(mano2), "         " , sum(mano3), "          " , sum(mano4), "       " , sum(mano5) ,"         ", sum(manod))
resultados.append(sum(mano1))
resultados.append(sum(mano2))
resultados.append(sum(mano3))
resultados.append(sum(mano4))
resultados.append(sum(mano5))
resultados.append(sum(manod))

for i in resultados:
    if i <= 21:
        ganador.append(i)

#ganadores

if sum(manod) < 21:
    if (sum(mano1) > sum(manod) and sum(mano1) < 21):
        print ("jugador 1 gana")
        apuestaj1.saldo += int(apuestaj1.valor*2)
    if (sum(mano2) > sum(manod) and sum(mano2) < 21):
        print ("jugador 2 gana")
        apuestaj2.saldo += int(apuestaj2.valor*2)
    if (sum(mano3) > sum(manod) and sum(mano3) < 21):
        print ("jugador 3 gana")
        apuestaj3.saldo += int(apuestaj3.valor*2)
    if (sum(mano4) > sum(manod) and sum(mano4) < 21):
        print ("jugador 4 gana")
        apuestaj4.saldo += int(apuestaj4.valor*2)
    if (sum(mano5) > sum(manod) and sum(mano5) < 21):
        print ("jugador 5 gana")
        apuestaj5.saldo += int(apuestaj5.valor*2)
    else:
        print ("dealer gana")
elif sum(manod) > 21:
        if (sum(mano1))<= 21:
            print ("jugador 1 gana")
            apuestaj1.saldo += int(apuestaj1.valor*2)
        if (sum(mano2))<= 21:
            print ("jugador 2 gana")
            apuestaj1.saldo += int(apuestaj2.valor*2)
        if (sum(mano3))<= 21:
            print ("jugador 3 gana")
            apuestaj1.saldo += int(apuestaj3.valor*2)
        if (sum(mano4))<= 21:
            print ("jugador 4 gana")
            apuestaj1.saldo += int(apuestaj4.valor*2)
        if (sum(mano5))<= 21:
            print ("jugador 5 gana")
            apuestaj1.saldo += int(apuestaj5.valor*2)



print("El mayor valor ganador es: ")
print(max(ganador))
print(apuestaj1)



# def apuesta $$$  /// extras // nueva ronda (+deck caundo se este acabado el deck)
