
#Helping user know what to input
print("Encrypt = e", "\nDecrypt = d")
close = False
#Loop for cypher
while close is False:
    question = input("Would you like to encrypt to decrypt? ")
    #Validating they entered the correct values
    if question.lower() == "e" or question.lower() == "d":       
        text = input("Input Text- ")
        ascii = []
        if question.lower() == "e":
            for i in text:
                #Converting text value to ASCII
                ascii.append(ord(i)+3)
        else:
            for i in text:
                ascii.append(ord(i)-3)
                #Converting ASCII to string
        print(''.join([chr(c) for c in ascii]))
            #Validating if they want to close 
        close = input("Would you like to close? ").lower() == 'yes'
    else:
        print("please enter e or d")
