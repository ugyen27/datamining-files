import re

stmt = "p = i + r * 6 ;"

operators = {'=' : 'Assignment op','+' : 'Addition op','-' : 'Subtraction op','/' : 'Division op','*' : 'Multiplication op','<' : 'Lessthan op','>' : 'Greaterthan op' }
operators_key = operators.keys()

data_type = {'int' : 'integer type', 'float': 'Floating point' , 'char' : 'Character type', 'long' : 'long int' }
data_type_key = data_type.keys()

punctuation_symbol = { ':' : 'colon', ';' : 'semi-colon', '.' : 'dot' , ',' : 'comma' }
punctuation_symbol_key = punctuation_symbol.keys()

identifier = { 'a' : 'id', 'b' : 'id', 'c' : 'id' , 'd' : 'id','e':'id','f' : 'id', 'g' : 'id', 'h' : 'id' , 'i' : 'id','j':'id','k' : 'id', 'l' : 'id', 'm' : 'id' , 'n' : 'id','o':'id','p':'id','q' : 'id', 'r' : 'id', 's' : 'id' , 't' : 'id','u':'id','v' : 'id', 'w' : 'id', 'x' : 'id' , 'y' : 'id','z':'id' }
identifier_key = identifier.keys()

number = { '0' : 'num', '1' : 'num', '2' : 'num' , '3' : 'num','4':'num','5' : 'num', '6' : 'num', '7' : 'num' , '8' : 'num','9':'num'}
number_key = number.keys()

dataFlag = False


attribute_val=0
count=0
program = stmt.split("\n")
for line in program:
    count = count + 1
    print("line#" , count, "\n" , line)

    tokens=line.split(' ')
    print("Tokens are " , tokens)
    print("Line#", count, "properties \n")
    for token in tokens:
        if token in operators_key:
            print("operator is ", operators[token])
        if token in data_type_key:
            print("datatype is", data_type[token])
        if token in punctuation_symbol_key:
            print (token, "Punctuation symbol is" , punctuation_symbol[token])
        if token in identifier_key:
            print (token, "Identifier is" , identifier[token])
            attribute_val = attribute_val + 1
            print ("attribute value: ",attribute_val)
            print ("<",identifier[token] , ",", attribute_val,">")
        if token in number_key:
            print (token, "number is" , number[token])    

           
    dataFlag=False
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _") 