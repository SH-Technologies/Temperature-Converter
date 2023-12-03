#Simple Temperature Converter  Celsius <=> Fahrenheit
#Coded by Castro 2023


print("CCCCC   AAAAA   SSSSS   TTTTT   RRRRR   OOOOO")
print("CC      AAAAA   S         T     R   R   O   O")
print("CC      A   A   S         T     R  RR   O   O")
print("CC      AA AA   SSSSS     T     RRRR    O   O")
print("CC      AA AA       S     T     R  R    O   O")
print("CC      A   A       S     T     R   R   O   O")
print("CCCCC   A   A   SSSSS     T     R   R   OOOOO")

print("""Please insert a Temperature - just Numbers. In The Next Step you can choose
between Celsius or Fahrenheit. Enjoy""")
print("--------------------------------------------------------------------------------")

temp = input("Temperature:")
conv = input("Convert to: (C)elsius or (F)ahrenheit")

if conv == "C":
    print("The Temperature in Celsius is:")
    print((float(temp) - 32) * 5/9)
elif conv == "F":
    print("The Temperature in Fahrenheit is:")
    print(float(temp) * 9/5 + 32)