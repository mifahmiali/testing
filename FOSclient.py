import socket
import signal
import sys


cSocket = socket.socket()
host = '192.168.56.108'
port = 8888

print('Waiting for connection')
try:
        cSocket.connect((host, port))
except socket.error as e:
        print(str(e))


Response = cSocket.recv(2048)
print(Response.decode("utf-8"))

print(			"\t\t\t* *** *** *** MENU LIST *** **** *** *\t\t\t\n")

print("   ------------------------------------------------------------------------------------")
print("   | [A]  Spaghetti Aglio Olio          RM20\n")
print("   | [B]  Spaghetti Carbonara           RM16\n")
print("   | [C]  Chicken Chop                  RM20\n")
print("   | [D]  Margherita Pizza              RM25\n")
print("   | [E]  Hawaiian Chicken Pizza        RM23\n")
print("   | [F]  Tiramisu Cake                 RM10/slice)\n")
print("   | [G]  Caramel Latte                 RM8\n")
print("   | [H]  Americano                     RM6\n")
print("   | [I]  Espresso                      RM7\n")
print("   | [J]  Ice Blended Chocolate         RM8\n")
print("   | [K]  Oreo Frappucino               RM10\n")
print("   | [L]  Orange Juice                  RM9\n")
print("   ------------------------------------------------------------------------------------")
print("=========================================================================================")
while True:
    opt = input('\nSelect Your Menu [Code Menu] Press "EXIT" if you are done..\n> ')

    if opt == "A" or opt == "B" or opt == "C" or opt == "D" or opt == "E" or opt == "F" or opt == "G" or opt == "H" or opt == "I" or opt == "J" or opt == "K" or opt == "L" or opt == "M" or opt == "N" or opt == "O" or opt == "P" or opt == "Q" or opt == "R" or opt == "S" or opt == "T":
        qty = input("Quantity per Order: ")
        prc = '0'
        Input = opt + ":" + qty + ":" + prc
        cSocket.send(str.encode(Input))
        Response = cSocket.recv(1024)
        print(Response.decode("utf-8"))

    elif opt == 'EXIT':
        print('YOUR ORDER HAS BEEN SUCCESFULLY RECORDED..\nTHANK YOU FOR YOUR ORDER :)')
        break

    else:
        print("WRONG INPUT, TRY AGAIN!!")
        cSocket.send(str.encode(Input))
        Response = cSocket.recv(1024)
        print(Response.decode("utf-8"))

cSocket.close()
