



def main():

    temperature = float(input("Please enter the tempreture: ")) 

    tempType = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    if (tempType == "C") and (temperature <= 0):
        print("At this temperature, water is a (frozen) solid.")

    elif (tempType == "C") and (temperature >= 100):
        print("At this temperature, water is gas.")

    elif (tempType == "C") and (temperature < 100):
        print("At this temperature, water is a liquid .")

    elif (tempType == "K") and (temperature <= 273 ):
        print("At this temperature, water is a (frozen) solid.")

    elif (tempType == "K") and (temperature >= 373):
        print("At this temperature, water is gas.")

    elif (tempType == "K") and (temperature < 373):
        print("At this temperature, water is a liquid .")


main()
