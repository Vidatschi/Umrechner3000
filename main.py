def dec_to_bin():
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
    print(endString)

if __name__ == '__main__':
    dec_to_bin()
