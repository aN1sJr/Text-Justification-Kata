
#The quick brown fox jumps over the lazy dog and runs away swiftly across the meadow under the bright blue sky.


def textJustify(lenghtInput):
    textInput = input("Please enter youre text: ")
    textOutput = ""
    endLigne = "\n"
    spaceCounter = 0
    counter = 1
    for i in range(len(textInput)):
        while textInput.startswith(" "):
            textInput = textInput[1:]
        if len(textInput) < lenghtInput:
            textOutput += textInput
            break
        if counter == lenghtInput:
            slice_end = min(lenghtInput, len(textInput))
            counter = 0
            spaceCounter = 0
            if textInput[slice_end] != " ":
                x = slice_end
                while True:
                    x -= 1
                    if textInput[x] != " ":
                        spaceCounter += 1
                    else:
                        spaceCounter += 1
                        break
            chek = True
            for j in range(slice_end - spaceCounter):
                 if textInput[j] == " " and chek:
                     for k in range(spaceCounter):
                         textOutput += " "
                         chek = False
                 else:
                     textOutput += textInput[j]
            else:
                chek = True
                for j in range(slice_end - 1):
                    if textInput[j] == " " and chek:
                        textOutput += " "
            textOutput += endLigne
            textInput = textInput[slice_end:]
        counter += 1
    print(textOutput)


textJustify(20)