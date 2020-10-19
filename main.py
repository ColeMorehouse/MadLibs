print("Welcome to the MADlib")
string = "There are many {} ways to choose a/an {} to read. First, you could ask for recommendations from your friends and {}. Just don't ask Aunt {}-she only reads {} books."
in1 = input("enter an adjective: ")
in2 = input("enter a noun: ")
in3 = input("enter a plural noun: ")
in4 = input("enter a name: ")
in5 = input("enter an adjective: ")
print("Your MADlib: ")
print(string.format(in1,in2,in3,in4,in5))