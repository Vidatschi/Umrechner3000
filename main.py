def checkArgs(arg):
    if not arg or arg[0] == None:
        return False
    return True


def getValidDec(number):
    try:
        dec = int(number)
    except:
        return("Ungültige Eingabe.")
    if dec < 0:
        return("Ungültige Eingabe.")
    return dec


def checkValidBin(binStr):
    if all(char in '01' for char in binStr):
        return
    return("Ungültige Eingabe.")


def checkValidHex(hexStr):
    if all(char in '0123456789ABCDEFabcdef' for char in hexStr):
        return
    return("Ungültige Eingabe.")


def binToDecConv(binStr):
    i = len(binStr)
    decNum = 0
    exponent = 0
    while i != 0:
        i -= 1
        if int(binStr[i]) == 1:
            decNum += 2 ** exponent
        exponent += 1
    return decNum


def decToBinConv(dec):
    endString = ""
    if dec != 0:
        while dec != 0:
            rest = dec % 2
            endString = str(rest) + endString
            dec = dec // 2
            endStringTemp = endString.replace(" ", "")
            if len(endStringTemp) % 4 == 0:
                endString = " " + endString
    else:
        endString = str(0)
    return endString


def hexCheck(number):
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


def hexToBinConv(character):
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
        decStr = input("Bitte geben Sie eine Dezimalzahl größer/gleich 0 ein: ").replace(" ", "")
    dec = getValidDec(decStr)
    if dec != "Ungültige Eingabe.":
        endString = decToBinConv(dec)
        while len(endString.replace(" ", "")) % 4 != 0:
            endString = "0" + endString
        if len(endString.replace(" ", "")) == 4:
            endString = "0000 " + endString
        elif len(endString.replace(" ", "")) % 8:
            endString = "0000 " +endString
        return endString
    else:
        return "Ungültige Eingabe."


def bin_to_dec(*args):
    if checkArgs(args):
        binStr = str(args[0]).replace(" ", "")
    else:
        binStr = input("Bitte geben Sie eine Binärzahl ein: ").replace(" ", "")
    if checkValidBin(binStr) != "Ungültige Eingabe.":
        return binToDecConv(binStr)
    else:
        return "Ungültige Eingabe."


def bin_to_hex(*args):
    if checkArgs(args):
        binStr = args[0].replace(" ", "")
    else:
        binStr = input("Bitte geben Sie eine Binärzahl ein: ").replace(" ", "")
    if checkValidBin(binStr) != "Ungültige Eingabe.":
        hexNum = ""
        while len(binStr) > 0:
            binSub = binStr[-4:]
            binStr = binStr[:-4]
            tempNum = binToDecConv(binSub)
            if tempNum > 9:
                hexNum = hexCheck(tempNum) + hexNum
            else:
                hexNum = str(tempNum) + hexNum
        hexNum = hexNum.lstrip("0")
        return hexNum
    else:
        return "Ungültige Eingabe."


def hex_to_bin(*args):
    if checkArgs(args):
        hexStr = args[0]
    else:
        hexStr = input("Bitte geben Sie eine Hexzahl ein: ").replace(" ", "")
    if checkValidHex(hexStr) != "Ungültige Eingabe.":
        binNum = ""
        while len(hexStr) > 0:
            hexSub = hexStr[-1:]
            hexStr = hexStr[:-1]
            binNum = hexToBinConv(hexSub) + " " + binNum
        if len(binNum.replace(" ", "")) % 8:
            binNum = "0000 " + binNum
        return binNum
    else:
        return "Ungültige Eingabe."


def consoleMain(*args):
    if checkArgs(args):
        source = args[0].upper().strip()
        dest = args[1].upper().strip()
        inputVal = args[2]
    else:
        source = input("Welches Zahlensystem wollen Sie konvertieren?: ").upper().strip()
        dest = input("In welches Zahlensystem wollen Sie konvertieren?: ").upper().strip()
        inputVal = None
    if source == dest:
        return "gleiches System!"
    if source == "BINÄR" or source == "BIN":
        if dest == "HEXA" or dest == "HEX" or dest == "HEXADEZIMAL" or dest == "HEXADECIMAL":
            return(bin_to_hex(inputVal))
        elif dest == "DEZ" or dest == "DEC" or dest == "DEZIMAL":
            return(bin_to_dec(inputVal))
        else:
            return("Bitte erneut versuchen.")
    elif source == "DEZ" or source == "DEC" or source == "DEZIMAL":
        if dest == "HEXA" or dest == "HEX" or dest == "HEXADEZIMAL" or dest == "HEXADECIMAL":
            return(bin_to_hex(dec_to_bin(inputVal)))
        elif dest == "BINÄR" or dest == "BIN":
            return(dec_to_bin(inputVal))
        else:
            return("Bitte erneut versuchen.")
    elif source == "HEXA" or source == "HEX" or source == "HEXADEZIMAL" or source == "HEXADECIMAL":
        if dest == "BINÄR" or dest == "BIN":
            return(hex_to_bin(inputVal))
        elif dest == "DEZ" or dest == "DEC" or dest == "DEZIMAL":
            return(bin_to_dec(hex_to_bin(inputVal)))
        else:
            return("Bitte erneut versuchen.")
    else:
        return("Bitte erneut versuchen.")


if __name__ == '__main__':
    # print(dec_to_bin())
    # print(bin_to_dec())
    # print(bin_to_hex())
    # print(hex_to_bin())
    print(consoleMain())
