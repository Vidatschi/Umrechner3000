def checkArgs(arg):
    if not arg:
        return False
    return True

def getValidDec(number):
    try:
        dec = int(number)
    except:
        print("Ungültige Eingabe.")
        exit()
    if dec < 0:
        print("Ungültige Eingabe.")
        exit()
    return dec

def checkValidBin(binStr):
    if all(char in '01' for char in binStr):
        return
    print("Ungültige Eingabe.")
    exit()

def binToNumberConv(binStr):
    i = len(binStr)
    decNum = 0
    exponent = 0
    while i != 0:
        i -= 1
        if int(binStr[i]) == 1:
            decNum += 2**exponent
        exponent += 1
    return decNum

def hexConv(number):
    decNum = int(number)
    if decNum == 10:
        return "A"
    elif decNum == 11:
        return "B"
    elif decNum == 12:
        return "C"
    elif decNum == 13:
        return "D"
    elif decNum == 14:
        return "E"
    elif decNum == 15:
        return "F"

def dec_to_bin(*args):
    if checkArgs(args):
        decStr = args[0]
    else:
        decStr = input("Bitte geben Sie eine Dezimalzahl größer/gleich 0 ein: ")
    dec = getValidDec(decStr)
    endString = ""
    if dec != 0:
        while dec != 0:
            rest = dec % 2
            endString = str(rest) + endString
            dec = dec // 2
    else:
        endString = str(0)
    endString = endString.zfill(8)
    return endString

def bin_to_dec(*args):
    if checkArgs(args):
        binStr = str(args[0])
    else:
        binStr = input("Bitte geben Sie eine Binärzahl ein: ")
    checkValidBin(binStr)
    return binToNumberConv(binStr)


def bin_to_hex(*args):
    if checkArgs(args):
        binStr = args[0]
    else:
        binStr = input("Bitte geben Sie eine Binärzahl ein: ")
    checkValidBin(binStr)
    hexNum = ""
    while len(binStr) > 0:
        binSub = binStr[-4:]
        binStr = binStr[:-4]
        tempNum = binToNumberConv(binSub)
        if tempNum > 9:
            hexNum = hexConv(tempNum)+ hexNum
        else:
            hexNum = str(tempNum) + hexNum
    return hexNum


if __name__ == '__main__':
    #print(dec_to_bin())
    #print(bin_to_dec())
    print(bin_to_hex())