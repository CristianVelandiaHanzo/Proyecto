# -*- coding: utf-8 -*-

def avarage_tempts(temps):
    suma_of_temps=0

    for temp in temps:
        suma_of_temps += float (temp)

    return suma_of_temps/len(temps)

if __name__=='__main__':

    temps = [21, 22, 22 , 23, 24, 24]

    AV=avarage_tempts(temps)

    print('Temperatura:  {}  '.format(AV))


