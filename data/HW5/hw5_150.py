

def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please the enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")

    for i in range(height):

 
        if i == 0 or i + 1 == height:
            print(width * outline)

        elif i != height - 1:
            print(outline  + fill * (width - 2) + outline)

main()
