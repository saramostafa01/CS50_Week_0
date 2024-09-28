# Prompt user for input 
def main():
    text = input("Enter Text: ")
    print(convert(text))

# Covert emotions into emojis
def convert(x):
    if ":)" or ":(" in x :
        return (x.replace(":)","🙂").replace(":(","🙁"))
    else :
        return (x)


main()