# Write a method that accepts a name from the user and then returns it. Here’s the javascript:

# const getName = () => {
#   let name = prompt("what is your name?");
#   return name;
# };
#write this in pyhton
def getName():
    name = input("What is your name? ")
    return print(name)
getName()

# const reverseIt = () => {
#   let string = "a man, a plan, a canal, frenemies!";

#   let reverse = "";

#   for (let i=0; i < string.length; i++) {
#     reverse += string[string.length - (i+1)];
#   };

#   alert(reverse);
# };
# Write a method that reverses a string. Here’s the python:


def reverseIT():
    string = 'a man, a plan, a canal, frenemies!'
    reversed_string = "".join(reversed(string))
    return print("Original string:", string, "The string in reverse:", reversed_string)

reverseIT()

# const swapEm = () => {
#   let a = 10;
#   let b = 30;
#   let temp;

#   temp = b;
#   b = a;
#   a = temp;

#   alert("a is now " + a + ", and b is now " + b);
# };

# Write a method that swaps the values of two variables around. Here’s the python:

def swap_em():
    a = 10
    b = 30
    temp = a
    a = b
    b = temp
    return print(f"a is now {a}, and b is now {b}")

swap_em()


