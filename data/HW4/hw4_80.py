
def main():
    height = int(input("Please enter the starting theight of the hailstone: "))
    print("Hail is currently at height", height)
    while height != 1:
       if height%2 != 0:
           height = (height*3)+1 
           print("Hail is currently at height", height)
       if height%2 == 0:
           height = (height//2)
           print("Hail is currently at height", height)
    print("Hail stopped at height 1")
main()
