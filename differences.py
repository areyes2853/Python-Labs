import math

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

# Write a method that multiplies all numbers in a given array/list and returns the final product. Here’s the javascript:

# const multiplyArray = (ary) => {
#   if (ary.length == 0) { return 1; };

#   let total = 1;
#   // let total = ary[0];

#   for (let i=0; i < ary.length; i++) {
#     total = total * ary[i];
#   };

#   return total;
# };

# Write a method that multiplies all numbers in a given array/list and returns the final product. in python


def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


numbers = [2, 3, 4]
result = multiply_list(numbers)
print(result)  

# Write a method that takes a number argument and returns “fizz” if the number is divisible by three, “buzz” if the number is divisible by five, and “fizzbuzz” if it’s divisible by both. Here’s the javascript:
# const fizzbuzzer = (x) => {
#   if( x%(3*5) == 0 ) {
#     return 'fizzbuzz'
#   } else if( x%3 == 0 ) {
#     return 'fizz'
#   } else if ( x%5 == 0 ) {
#     return 'buzz'
#   } else {
#     return 'archer'
#   }
# }


# Write a method that takes a number argument and returns “fizz” if the number is divisible by three, “buzz” if the number is divisible by five, and “fizzbuzz” if it’s divisible by both. please do it in python:
def fizzbuzzer(x):
    if x % 15 == 0:
        return 'fizzbuzz'
    elif x % 3 == 0:
        return 'fizz'
    elif x % 5 == 0:
        return 'buzz'
    else:
        return 'archer'
print(fizzbuzzer(15))

# Write a method that finds the fibonacci number at the nth position and returns it. Here is the javascript:
# const nthFibonacciNumber = () => {
#   let fibs = [1, 1];
#   let num = prompt("which fibonacci number do you want?");

#   while (fibs.length < parseInt(num)) {
#     let length = fibs.length;
#     let nextFib = fibs[length - 2] + fibs[length - 1];
#     fibs.push(nextFib);
#   }

#   alert(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
# };

# Write a method that finds the fibonacci number at the nth position and returns it. python:

def fibonacci_binet(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi ** n - (-1 / phi) ** n) / math.sqrt(5))

# Write a method that searches through an array/list for a value and returns true or false depending on whether or not the value is present in the array/list. Here is the javascript:

# const searchArray = (array, value) => {
#   for(let i = 0; i < array.length-1; i++) {
#     if(array[i] == value) {
#       return true;
#       break;
#     }
#   }
#   return -1;
# };

# here it is in python
def search_array(array, value):
    for item in array:
        if item == value:
            return True
    return False

search_array([1, 2, 3], 2)  # Returns: True
search_array([1, 2, 3], 5)  # Returns: False

# Write a method that checks whether or not a string is a palindrome. Here is the javascript:

# const isPalindrome = (str) => {
#   for(let i = 0; i < str.length/2; i++){
#     if(str[i] != str[str.length-i-1]){
#       return false;
#       break;
#     }
#   }
#   return true;
# };

# now in python

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False

# Write a method that checks whether or not an array/list has any duplicates. Here is the javascript:

# const hasDupes = (arr) => {
#   let obj = {};
#   for (i = 0; i < arr.length; i++) {
#     if(obj[arr[i]]) {
#       return true;
#     }
#     else {
#       obj[arr[i]] = true;
#     }
#   }
#   return false;
# };

# in python

def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False
print(has_duplicates([1, 2, 3, 4]))  # Output: False
print(has_duplicates([1, 2, 3, 2]))  # Output: True
