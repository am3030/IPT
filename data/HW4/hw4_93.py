




def main():

    hail=int(input("Please enter the starting height of the hailstone: "))
    while hail != 1:
        
        if hail % 2 == 0:
            hail = (hail/2)
            print("",hail)
        else:
            hail = (hail*3)+1
            print("",hail)

main()
