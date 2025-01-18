def checkArgs(arg):
    if not arg:
        return False
    return True

def dec_to_bin(*args):
    if checkArgs(args):
        io = args[0]
    else:
        io = input("Bitte eine Zahl zwischen 0 und 255 eingeben: ")
    try:
        dec = int(io)
    except:
        print("Eine Zahl zwischen 0 und 255!")
        exit()
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
    if all(char in '01' for char in binStr):
        i = len(binStr)
        decNum = 0
        exponent = 0
        while i != 0:
            i -= 1
            if int(binStr[i]) == 1:
                decNum += 2**exponent
            exponent += 1
        return decNum
    else:
        print("Ungültige Eingabe. Bitte geben Sie eine gültige Binärzahl ein.")

if __name__ == '__main__':
    #print(dec_to_bin())
    print(bin_to_dec())
