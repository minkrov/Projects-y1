def translate(phrase):
    translate = ""
    for letter in phrase:
        if letter in "EUIOAeuioa":
            translate += "g"
        else:
            translate += letter
    return translate

print(translate(input("Enter a phrase: ")))