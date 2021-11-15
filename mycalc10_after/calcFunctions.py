from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'
    
    if n >= 4000:
        return 'Error!'
    
    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
          (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
           (1, 'I')
    ]

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value
    
    return result

def romanToDec(numStr):
    n = numStr
    result = 0

    romans = [
        (900, 'CM'), (1000, 'M'), (400, 'CD'), (500, 'D'),
        (90, 'XC'), (100, 'C'), (40, 'XL'), (50, 'L'),
        (9, 'IX'), (10, 'X'), (4, 'IV'), (5, 'V'),
        (1, 'I')
    ]

    for value, roman in romans:
        while roman in n:
            n = n[len(roman):]
            result += value

    return str(result)

