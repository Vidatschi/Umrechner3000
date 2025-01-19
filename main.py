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

def checkValidHex(hexStr):
    if all(char in '0123456789ABCDEFabcdef' for char in hexStr):
        return
    print("Ungültige Eingabe.")
    exit()

def binToDecConv(binStr):
    i = len(binStr)
    decNum = 0
    exponent = 0
    while i != 0:
        i -= 1
        if int(binStr[i]) == 1:
            decNum += 2**exponent
        exponent += 1
    return decNum

def decToBinConv(dec):
    endString = ""
    if dec != 0:
        while dec != 0:
            rest = dec % 2
            endString = str(rest) + endString
            dec = dec // 2
    else:
        endString = str(0)
    return endString

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

def binConv(character):
    try:
        number = int(character)
        return decToBinConv(number).zfill(4)
    except:
        character = character.upper()
        if character == "A":
            return "1010"
        elif character == "B":
            return "1011"
        elif character == "C":
            return "1100"
        elif character == "D":
            return "1101"
        elif character == "E":
            return "1110"
        elif character == "F":
            return "1111"

def dec_to_bin(*args):
    if checkArgs(args):
        decStr = args[0]
    else:
        decStr = input("Bitte geben Sie eine Dezimalzahl größer/gleich 0 ein: ")
    dec = getValidDec(decStr)
    endString = decToBinConv(dec).zfill(8)
    return endString

def bin_to_dec(*args):
    if checkArgs(args):
        binStr = str(args[0])
    else:
        binStr = input("Bitte geben Sie eine Binärzahl ein: ")
    checkValidBin(binStr)
    return binToDecConv(binStr)


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
        tempNum = binToDecConv(binSub)
        if tempNum > 9:
            hexNum = hexConv(tempNum)+ hexNum
        else:
            hexNum = str(tempNum) + hexNum
    if hexNum[0] == "0":
        hexNum = hexNum[-1:]
    return hexNum

def hex_to_bin(*args):
    if checkArgs(args):
        hexStr = args[0]
    else:
        hexStr = input("Bitte geben Sie eine Hexzahl ein: ")
    checkValidHex(hexStr)
    binNum = ""
    while len(hexStr) > 0:
        hexSub = hexStr[-1:]
        hexStr = hexStr [:-1]
        binNum = binConv(hexSub) + binNum
    return binNum

def consoleMain():
    source = input("Welches Zahlensystem wollen Sie konvertieren?: ").upper().strip()
    dest = input("In welches Zahlensystem wollen Sie konvertieren?: ").upper().strip()
    if source == "BINÄR" or source == "BIN":
        if dest == "HEXA" or dest == "HEX" or dest == "HEXADEZIMAL" or dest == "HEXADECIMAL":
            print(bin_to_hex())
        elif dest == "DEZ" or dest == "DEC" or dest == "DEZIMAL":
            print(bin_to_dec())
    elif source == "DEZ" or source == "DEC" or source == "DEZIMAL":
        if dest == "HEXA" or dest == "HEX" or dest == "HEXADEZIMAL" or dest == "HEXADECIMAL":
            print(bin_to_hex(dec_to_bin()))
        elif dest == "BINÄR" or dest == "BIN":
            print(dec_to_bin())
    elif source == "HEXA" or source == "HEX" or source == "HEXADEZIMAL"  or source == "HEXADECIMAL":
        if dest == "BINÄR" or dest == "BIN":
            print(hex_to_bin())
        elif dest == "DEZ" or dest == "DEC" or dest == "DEZIMAL":
            print(bin_to_dec(hex_to_bin()))

if __name__ == '__main__':
    #print(dec_to_bin())
    #print(bin_to_dec())
    #print(bin_to_hex())
    #print(hex_to_bin())
    consoleMain()