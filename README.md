<h3 align="center">
  <image src="https://github.com/TasfiqulTapu/Spout/assets/66732331/6ba91903-73ca-4ebe-9cf9-2ea2b5479140" width="256" height="128" alt="Spout">
</h3>


Spout is an interpreted programming language aimed at demistifying bitwise operations 

#### Installation:
install spout from pip using
```bash
pip install spoutlang
```
#### Example program:
```py
// variable declaration
let a = 0b1010011
let b = 22

// function declaration
fn add a,b: spout a + b

// function calling
add(a,b)
print(a+b)
```
Run the progragm using,
```bash
spout example.🐳
```
or with source,
```bash
python project.py example.🐳
```

#### Language features
##### Variables and constants
In spout, variables can be declared using `let` keyword and constants can be declared with `const` keyword. Currently they can hold `int` and `string` types. Variables are mutable but constants are not (As it should be). Vars and consts are scoped. Meaning if you declare a variable inside a function, it can't be accessed outside that function. Here's syantax for declaring variables:
```py
// mutable 
let x = 23
x = 24 // fine
//immutable
const y = 23
y = 24 // error
```

##### Functions
Functions can be used with the `fn` keyword and provide a nice way to abstract your code. Currently sprout has only one function `print` (more will be added soon™). Here are all the valid ways to define a function
```py
fn add x,y: x+y
fn add (x,y): x+y
fn add x,y:(
    x+y
)
fn add (x,y):(
    x+y
)
```
Notice how you don't have to return values because functions automatically return the value of the last statement in them. 
In order to call a function we use this syntax:
```py
print("Hello World", "!")
```

##### Special keyword
Spout has a special keyword `spout`. When you use this keyword in front of a statement, a visual representation of the binary operation is shown if there are any binary operation.
For example:
```py
spout 0b11001 + 0b00110
``` 
would print out 
```bash
      11001
ADD + 00110
------------
      11111
```
when run.

##### Numbers
Currently all numbers are int and there is no proper way to get negative numbers (but there's a cheeky way to). Numbers can be written in decimal, binary, octal and hexadecimal.
```py
// These are all valid ways to express an int
256
0b100000000
0o400
0xFF
``` 

##### Strings
Use `""`to express a staring. Strings can be joined added and **subtracted** from each other. Take that, every other language out there. They can also be multiplied by ints.
```py
"Hello World" + "!" // "Hello World!"
"Hello World" - "World" // "Hello "
"Hello " * 3 // "Hello Hello Hello "
```


