


def main():
    
    temp1 = float(input("Please enter the temperature: " ))
    temp2 = str(input("Please enter'C' for Celsius, or 'K' for Kelvin: " ))
    if temp2 == "C":
       if temp1 > 0 and temp1 < 100 :
           print("At this temperature, water is liquid.")
       elif temp1 < 0 :
           print("At this temperature, water is a (frozen) solid.")
       else :
           print("At this temperature, water is a gas.")

    elif temp2 == "K":
        if temp1 > 273 and temp1 < 373 :
            print("At this temperature, water is liquid.")
        elif temp1 < 273 :
            print("At this temperature, water is a (frozen) solid.")
        else :
            print("At this temperature, water is gas.")
















main()
