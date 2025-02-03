import main as c3k
import tkinter as tk


def guiMain():
    root = tk.Tk()
    root.geometry("400x150")
    root.title("Umrechner3000 - Jetzt auch ohne Bugs!")
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)

    OPTIONS = [
        "Binär",
        "Dezimal",
        "Hexadezimal"
    ]


    def guiEval():
        rightLabelField.config(state=tk.NORMAL)
        source = variableLeft.get()
        dest = variableRight.get()
        leftEntry = leftLabelField.get().replace(" ", "")
        if leftEntry == "":
            leftEntry = "0"

        if source == "Binär":
            if dest == "Hexadezimal":
                rightLabelField.delete(0,"end")
                rightLabelField.insert(0,c3k.bin_to_hex(leftEntry))
            elif dest == "Dezimal":
                rightLabelField.delete(0,"end")
                rightLabelField.insert(0,c3k.bin_to_dec(leftEntry))
            else:
                rightLabelField.delete(0,"end")
                rightLabelField.insert(0,"selbes System!")
        elif source == "Dezimal":
            if dest == "Hexadezimal":
                rightLabelField.delete(0,"end")
                rightLabelField.insert(0,c3k.bin_to_hex(c3k.dec_to_bin(leftEntry)))
            elif dest == "Binär":
                rightLabelField.delete(0,"end")
                rightLabelField.insert(0,c3k.dec_to_bin(leftEntry))
            else:
                rightLabelField.delete(0,"end")
                rightLabelField.insert(0,"selbes System!")
        elif source == "Hexadezimal":
            if dest == "Binär":
                rightLabelField.delete(0,"end")
                rightLabelField.insert(0,c3k.hex_to_bin(leftEntry))
            elif dest == "Dezimal":
                rightLabelField.delete(0,"end")
                rightLabelField.insert(0,c3k.bin_to_dec(c3k.hex_to_bin(leftEntry)))
            else:
                rightLabelField.delete(0,"end")
                rightLabelField.insert(0,"selbes System!")
        else:
            rightLabelField.delete(0,"end")
            rightLabelField.insert(0,"selbes System!")
        rightLabelField.config(state=tk.DISABLED)

    variableLeft = tk.StringVar(root)
    variableLeft.set("Binär")
    variableRight = tk.StringVar(root)
    variableRight.set("Dezimal")

    optionLeft = tk.OptionMenu(root, variableLeft, *OPTIONS)
    optionLeft.config(
        activebackground="LIGHTGREY"
    )
    optionLeft.grid(column=0, row=0, padx=0, pady=10)

    zuLabel = tk.Label(root, text="zu")
    zuLabel.grid(column=1, row=0)

    optionRight = tk.OptionMenu(root, variableRight, *OPTIONS)
    optionRight.config(
        activebackground="LIGHTGREY"
    )
    optionRight.grid(column=2, row=0, padx=0, pady=10)

    leftLabelField = tk.Entry()
    leftLabelField.grid(column=0, row=1, padx=10, pady=10)

    rightLabelField = tk.Entry()
    rightLabelField.config(state=tk.DISABLED)
    rightLabelField.grid(column=2, row=1, padx=10, pady=10)

    enterButton = tk.Button(root, text="Umrechnen!", command=guiEval)
    enterButton.grid(column=1, row=3, padx=0, pady=10)
    enterButton.config(
        activebackground="LIGHTGREY"
    )

    root.mainloop()


if __name__ == '__main__':
    guiMain()