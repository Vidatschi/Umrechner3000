import main as c3k
import tkinter as tk


def guiMain():
    root = tk.Tk()
    root.geometry("450x150")
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
        rightEntry = c3k.consoleMain(source, dest, leftEntry)
        rightLabelField.delete(0,"end")
        rightLabelField.insert(0,rightEntry)
        rightLabelField.config(state=tk.DISABLED)

    variableLeft = tk.StringVar(root)
    variableLeft.set("Binär")
    variableRight = tk.StringVar(root)
    variableRight.set("Dezimal")

    optionLeft = tk.OptionMenu(root, variableLeft, *OPTIONS)
    optionLeft.config(
        activebackground="LIGHTGREY",
        width=10
    )
    optionLeft.grid(column=0, row=0, padx=0, pady=10)

    zuLabel = tk.Label(root, text="zu")
    zuLabel.grid(column=1, row=0)

    optionRight = tk.OptionMenu(root, variableRight, *OPTIONS)
    optionRight.config(
        activebackground="LIGHTGREY",
        width=10
    )
    optionRight.grid(column=2, row=0, padx=0, pady=10)

    leftLabelField = tk.Entry()
    leftLabelField.grid(column=0, row=1, padx=10, pady=10)

    rightLabelField = tk.Entry()
    rightLabelField.config(state=tk.DISABLED)
    rightLabelField.grid(column=2, row=1, padx=10, pady=10)

    enterButton = tk.Button(root, text="Umrechnen!", command=guiEval, height=2, width=15)
    enterButton.grid(column=1, row=3, padx=0, pady=10)
    enterButton.config(
        activebackground="LIGHTGREY"
    )

    root.mainloop()


if __name__ == '__main__':
    guiMain()