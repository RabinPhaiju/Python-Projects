# Data types -> numbers,operations,type conversion,f-string

1.  concatination "123" + "456"
2.  type error, type checking,type conversion
    - type checking : - type(variable)
3.  integer,strings, float,boolean,

    1. Integer

       - eg_int = 10
       - str(eg_int)
       - int("10")
       - print(type(10\*\*10)) => int
       - int('0b1010', 2) => 10
       - int('0o12', 8) => 10

       1. Binary
          - print('binary -> decimal', 0b111) => 7
          - print(type(0b111)) => int
       2. Octal
          - print('octal -> decimal', 0o10) =>8
          - print(type(0o10)) => int
       3. Hexadecimal
          - print('hexadecimal -> decimal', 0xb) => 11
          - print(type(0xb)) => int

    2. Float

       - print(type(3.1415)) => float
       - print(float("10.4")) => 10.4
       - eg_float = 10.01

    3. String

       - eg_str = 'Welcome to Python World'
       - print(type("string")) => str
       - print("", type("")) => str

       - String operation

         - text.isalpha()
         - text.isalnum()
         - text.isnumeric()
         - text.isspace()
         - text.istitle()
         - text.startswith('H')
         - text.endswith('d')

         - print(' , '.join(['1', '2', '3', '4']))

         - print('hello'.rjust(10, '\*'))
         - print('hello'.ljust(10,'\*'))
         - print('hello'.center(20,'='))

         - text.split(' ')
         - text.replace('Hello', 'Bye')
         - text.upper()

         - text = ' some text '
         - len(text.strip())
         - len(text.rstrip())
         - len(text.lstrip())

    4. Complex
       - eg_complex = 2 + 3j => type complex
    5. Boolean
       - eg_bool = True
    6. None
       - eg_None = None

4.  Type Conversion

    - print('decimal -> hex', format(10, 'x')) => a
    - print('deciaml -> binary', format(7, 'b')) => 111
    - print('deciaml -> binary', format(8, 'o')) => 10

    - print(bin(34)) => 0b100010
    - print(hex(45)) => 0x2d
    - print(oct(10)) => 0o12
    - print(hex(0b10101001)) =>0xa9

5.  f string

    - print(f"my name is {name}")

6.  Print formatting

    - print('This is the string {}'.format('Inserted'))
    - print('The {0} {0} {0} '.format('fox', 'brown', 'quick'))
    - print('The {} {} {} '.format('fox', 'brown', 'quick'))
    - print('The {q} {b} {f} '.format(f = 'fox', b = 'brown', q= 'quick'))

7.  Float formatting

    - print('the result was {r:0.3f}'.format(r = 100/777))

8.  number manipulation

    - int(8/3) :-round the number
    - round(8/3) = 2.666
    - round(8/3,2) = 2.67
    - int(4/2) = 2.0
    - 8//2 = 2 :- floor division
    - score -= 1
    - score += 1
    - score /= 1
    - score \*= 1

9.  math operations

    - 3 \*\* 5 exponent
    - 3 \* 5 times
    - 3 / 5 divide
    - 3 / 5 floor divide
    - 3 + 5 sum
    - 3 - 5 diff
