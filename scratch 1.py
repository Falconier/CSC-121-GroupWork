## some schinanigans
## Author: Falconier

def main():
    msg = "hello world"
    printString(msg)

def printString(message):
    for i in range(0,len(message)):
        chCode = ord(message[i])
        print("Index:",i,"=> Char:",message[i], "=> Char Code (uni-8): ",ord(message[i]))


main()
