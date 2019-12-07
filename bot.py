import random
import json

answers = ['I\'m afraid I don\'t understand what you just said']
feelings = ['bad.', 'good.', 'great!', 'super!', 'terrible. :(', 'okay.', 'fine.']
feelingQuestions = [' How are you?', ' How about you?']
userWorseFeelings = ['Terrible', 'Bad', 'Tired', 'Worn out', ]
jokes = ["Did you hear about the mathematician who's afraid of"
         "negative numbers? They'll stop at nothing to avoid them.",
         "Why do we tell actors to \"break a leg\"? Because every play (or musical) has a cast.",
         "Calibri and Times New Roman walk into a restaurant. \"Get out of here!\" shouts the waiter. \"We don\'t serve your type!\"",
         "A bear walks into a snack shop and says, \“Give me a juice box and … milk.\” \“Why the big pause?\” asks the bartender. The bear shrugged. \“I\’m not sure; I was born with them.\”"]
d = {}

while True:
    print("My dictionary: {}".format(d))

    user_input = input("Enter something: ")
    if user_input.lower() == 'hi' or user_input.lower() == 'hello':
        print("Hello, how are you?")
    elif user_input.lower() == 'how are you?' or user_input.lower() == 'hello, how are you?':
        print("I'm feeling " + random.choice(feelings) + random.choice(feelingQuestions))
    elif user_input.lower() == 'terrible' or user_input.lower() == 'bad' or user_input.lower() == 'tired' or \
            user_input.lower() == 'worn out':
        print("I\'m sorry. Sounds like you've had a rough day. Would it cheer you up if I told you a joke?")
        user_input = input("Type something: ")
        if user_input.lower() == 'yes':
            print(random.choice(jokes))
    elif user_input.lower() == "good" or user_input.lower() == "super" or user_input.lower() == "great" or \
            user_input.lower() == "fine":
        print("That's good")
    elif user_input.lower() == "Let's do some math" or user_input.lower() == "math":
        x = float(input("Enter a number: "))
        y = float(input("Enter a number: "))
        print("What operation?")
        operation = input("Type an operation: ")
        if operation == "Multiplication":
            print(x * y)
        elif operation == "Division":
            print(x / y)
        elif operation == "Addition":
            print(x + y)
        elif operation == "Subtraction":
            print(x - y)
    elif user_input.lower() == "Add feelings":
        feel = input("Enter a feeling: ")
        feelings.append(feel)
    #elif user_input.lower() == "Add jokes" or "Add joke":
        #joke = input("Enter a joke: ")
        #jokes.append(joke)
    elif user_input.lower() == "Could you tell me a joke?":
        print(random.choice(jokes))
    elif user_input.lower() == "add value":
        key = input("Enter a key: ")
        val = input("Enter a value: ")
        d[key] = val
    elif user_input.lower() == "print value":
        x = input("Enter the key of the value you are trying to retrieve: ")
        print(d.get(x, "This key does not exist!"))
        #while user_input.lower() != "end":
         #   if x == key:
         #       print(val)
         #       x = input("Enter the key of the value you are trying to retrieve: ")
         #       #continue
         #   elif x == "end":
         #       break
    elif user_input.lower() == 'stop':
        break
    else:
        print(answers)
