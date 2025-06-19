import sys

if len(sys.argv)!= 2:
    print("none")
else:
    expected = sys.argv[1]
    user_input = input("What was the parameter? ")
    if user_input == expected:
        print("good job!")
    else:
        print("Nope,sorry...")
        