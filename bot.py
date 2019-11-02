import random

answers = ['I\'m afraid I don\'t understand what you just said']
feelings = ['bad.', 'good.', 'great!', 'super!', 'terrible. :(', 'okay.', 'fine.']
feelingQuestions = [' How are you?', ' How about you?']
userWorseFeelings = ['Terrible', 'Bad', 'Tired', 'Worn out', ]
jokes = ["Did you hear about the mathmatician who's afraid of negative numbers? They'll stop at nothing to avoid them.",
         "Why do we tell actors to \"break a leg\"? Because every play (or musical) has a cast.",
         "Calibri and Times New Roman walk into a resturant. \"Get out of here!\" shouts the waiter. \"We don\'t serve your type!\"",
         "A bear walks into a snack shop and says, \“Give me a juice box and … milk.\” \“Why the big pause?\” asks the bartender. The bear shrugged. \“I\’m not sure; I was born with them.\”"]

user_input = input("Type something: ")

while True:
    if user_input.lower() == 'hi' or user_input.lower() == 'hello':
        print("Hello, how are you?")
    elif user_input.lower() == 'how are you?' or user_input.lower() == 'hello, how are you?':
        print("I'm feeling " + random.choice(feelings) + random.choice(feelingQuestions))
    elif user_input.lower() == 'terrible' or user_input.lower() == 'bad' or user_input.lower() == 'tired' or user_input.lower() == 'worn out':
        print("I\'m sorry. Sounds like you've had a rough day. Would it cheer you up if I told you a joke?")
        if user_input.lower() == 'yes':
            print(random.choice(jokes))
    else:
        print(random.choice(answers))
    break

