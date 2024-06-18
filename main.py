from sympy import Abs
"""
    Convertidor IEEE754 - Coma Flotante
    tener presente que:
        bit     representa
        1       signo
        8       exponente
        23      mantisa

"""
def separarDecEnt(x:float):
    numero = str(Abs(x))
    partes = numero.split(".")
    parte_entera = partes[0] if partes else ""
    parte_decimal = partes[1] if partes and len(partes) > 1 else ""
    return parte_entera, parte_decimal

def binarioDecimal(x:str):
    num = int(x)
    dec = num/(10**len(x))
    binario_decimal = ''
    for n in range(23):
         bin = int(dec * 2)
         dec = -bin + dec * 2
         binario_decimal+=str(bin)
    return binario_decimal

def CalcularExponente(x:int):
    exp = 127+x
    if exp <= 127:
        exp_bin = bin(exp).replace('0b','')
        exp_bin = '0'+exp_bin
    else:
        exp_bin = bin(exp).replace('0b','')
    return exp_bin

def CalcularMantisa(x:str, y:str):
    mantisa = x + y
    mantisa = mantisa[:23]
    return mantisa

def transformarDecimal(x:list[str]):
    subcadena = []
    for i in x:
        dec = 0
        for j in range(0, len(i), 4):
            cuarteto = i[j:j+4]
            dec += int(cuarteto,2 )
        subcadena.append(dec)
    return subcadena

def transformarHex(x:list[int]):
    expHex = ''
    for i in x:
        expHex += hex(i).replace('0x','')
    return expHex

def __main__():
    x = input('Ingrese el valor a transformar: ')
    try:
        x = float(x)
        entero, decimal = separarDecEnt(x)
        bin_entero = bin(int(entero))
        bin_entero = bin_entero.replace('0b', '')
        bin_dec = binarioDecimal(decimal)

        signo = 1 if x < 0 else 0
        
        exponente = CalcularExponente(x=len(bin_entero)-1)
        print(exponente)
        mantisa = CalcularMantisa(x=bin_entero[1:],y=bin_dec)

        numeroIEEE754 = str(signo)+exponente+mantisa
        subcadenas = [numeroIEEE754[i:i+4] for i in range(0, len(numeroIEEE754), 4)]

        cadenaDecimales = transformarDecimal(subcadenas)
        cadenaHexadecimal = transformarHex(cadenaDecimales)


        print(f'El número {x} representado en IEE754 es {signo} {exponente} {mantisa} y su expresión en Hexadecimal es {cadenaHexadecimal}')

    except ValueError:
        return 'Ingrese un valor numérico válido'

__main__()