
def main():
    hailHeight = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height: ", hailHeight)
    while hailHeight != 1:
        if hailHeight % 2 == 0:
            hailHeight = hailHeight // 2
        else:
            hailHeight = (hailHeight * 3) + 1
        print("Hail is currently at height: " , hailHeight)
    print("Hail has stopped at 1.")

main()
