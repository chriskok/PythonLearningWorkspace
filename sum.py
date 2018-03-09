# ---------- MODULES ----------
# Your Python programs will contain a main program that
# includes your main function. Then you will create many
# modules in separate files. Modules also end with .py
# just like any other Python file

# ————— sum.py —————
def getSum(*args):
    sum = 0

    for i in args:
        sum += i

    return sum

# ————— End of sum.py —————
