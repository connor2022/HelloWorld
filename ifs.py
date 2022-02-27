bank = float(input("insert bank balance: "))

if bank > 1000:
    print("pog")
elif bank > 500:
    print("not too bad")
elif bank >= 0:
    print("oh no")
else:
    print("youre in debt")
    print("Bank balance: ?????")
    exit(0)

print("Bank balance: $",bank)