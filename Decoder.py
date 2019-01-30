## decoder group activity
## Filename: Decoder.py
## Author('s): Jacob Emory Bullin
import datetime
def main():
    theMessage = input("What message do you want decode?")
    decode(theMessage)

def decode():
    startTime = datetime.datetime.now()

    ## code for decoder here

    endTime = datetime.datetime.now()

    elapsedTime = endTime - startTime
    ##PrintFormatter
    if(elapsedTime.min > 0):
        print("Minutes:", elapsedTime.min, ", Seconds:", elapsedTime.seconds, ", MicroSeconds:", elapsedTime.microseconds)
    elif(elapsedTime.seconds > 0):
        print("Seconds:", elapsedTime.seconds, ", MicroSeconds:", elapsedTime.microseconds)
    else:
        print("MicroSeconds:", elapsedTime.microseconds)
    ##endPrintFormatter
main()
