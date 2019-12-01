dec = int(input("enter your decimal number:"))
rem = dec
quit = 1
hex  = ''
while quit != 0:
    quit = rem // 16
    rem = rem % 16
    if rem == 15:
        rem = "f"
    if rem == 14:
        rem = "e"
    if rem == 13:
        rem = 'd'
    if rem == 12:
        rem = 'c'
    if rem == 11:
        rem = 'b'
    if rem == 10:
        rem = 'a'
    #print(rem)
    hex = hex + str(rem)
    rem = quit
print("decimal: %i"%(dec))
print("hexadecimal: "+hex[::-1])
