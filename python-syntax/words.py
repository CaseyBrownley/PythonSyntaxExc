def print_upper_words(words):
    """print each word on seperate line uppercased
    
    >>>print_upper_words(["I", "love", "coding])
    I
    LOVE
    CODING
    """
    for word in  words:
        print(word.upper())

def print_upper_words2(words):

    """print words that only start with the letter E
    
     >>>print_upper_words2(["Eli", "Apple", "Eagle"])
     ELI
     EAGLE
    """

    for word in words:

        if word.startwith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    """>>>print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
                   
                   "HELLO", "HEY", "YO", and "YES"
                   """
    for word in must_start_with:
        if word.startswith("letter"):
            print(word.upper()) 
            break   