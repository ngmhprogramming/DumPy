def dumPy():
  print(evaluate("print~Took over the python shell, QUIT to escape.;"))
  expression = str(input(""))
  run(expression)

def run(expression):
  if expression == "QUIT":
    print(evaluate("print~I'm giving back control to you, my friend.;"))
    print(evaluate("print~Call me by running dumPy().;"))
  elif expression == "":
    print(evaluate("print~There's no expression.;"))
    expression = str(input(""))
    run(expression)
  else:
    print(evaluate(expression))
    expression = str(input(""))
    run(expression)
  
def evaluate(expression):
  #for evaluating values later
  import ast
  
  #checking syntax
  if expression[-1] != ";":
    return "ERROR: No semicolon"
  elif expression[0:5] == "loop~":
    #splitting up statement
    tokens = expression[5:-1].split("~")
    
    #function loop
    #loops over a function
    try:
      times = int(tokens[0])
      if isinstance(times, int):
        tokens.pop(0)
        for time in range(times):
          print(evaluate("~".join(tokens) + ";"))
        return "OUT: Loop done"
    except ValueError:
        return "ERROR: Times to loop is not an integer"
  else:
    #splitting up statement
    tokens = expression[:-1].split("~")
    
    #function assign
    #defines a variable
    if tokens[0] == "assign":
      #make sure there is a name and value
      if tokens[2] != "=":
        return "ERROR: Invalid 'assign' statement"
      else:
        #new global variable with name and value
        globals()[tokens[1]] = ast.literal_eval(tokens[-1])
        return "OUT: Value " + ast.literal_eval(tokens[-1]) + " assigned to variable " + tokens[1]
    
    #function get 
    #outputs variable value
    elif tokens[0] == "get":
      #if variable found
      try:
        return "OUT: " + globals()[tokens[1]]
      
      #if no variable found
      except KeyError:
        return "ERROR: No variable found"
    
    #function print
    #outputs stuff
    elif tokens[0] == "print":
      return "OUT: " + tokens[1]  
    
    #interpreter doesn't understand
    else:
      return "ERROR: Invalid function"

print("DumPy is ready to roll. :)\n")

if __name__ == "__main__":
  print(evaluate("print~A really bad interpreter for a dumb language which is separated by tildes.;"))
  print(evaluate("print~Just for fun to test my logic and skill.;"))
  print(evaluate("print~Probably going to fail at concatenation and operators.;"))
  print(evaluate("print~Written in Python 3.;"))
  print(evaluate("print~Going to allow input in a text file soon.;"))
  print(evaluate("print~This will allow accurate pinpointing of errors.\n;"))
  print(evaluate("print~A brief overview of all functions.;"))
  print(evaluate("print~assign, get, print, loop.;"))
  print(evaluate("print~create variable, output variable value, output text, loop a certain number of times\n;"))
  print(evaluate("print~How functions work, and remember the tilde between each argument.;"))
  print(evaluate("print~assign<name><value>;"))
  print(evaluate("print~get<name>;"))
  print(evaluate("print~print<value>;"))
  print(evaluate("print~loop<times><expression>\n;"))
  print(evaluate("print~I will demonstrate all functionality and errors. If you type YES.;"))
  answer = str(input("Answer: "))
  if answer == "YES":
    print(evaluate("print~\n;"))
    print(evaluate("print~The next line demonstrates the syntax reading and shows that it can pick up missing semicolons.;"))
    print(evaluate("assign~whoops~=~'Lost my semicolon'"))
    print(evaluate("print~The next line shows that it can create variables.;"))
    print(evaluate("assign~name~=~'Jeff';"))
    print(evaluate("print~The next line shows that it can get values of variables;"))
    print(evaluate("get~name;"))
    print(evaluate("print~The next line shows that it can pick up the error where there is no variable found.;"))
    print(evaluate("get~thisVariableDoesntExist;"))
    print(evaluate("print~The next line shows the ability to have console output.;"))
    print(evaluate("print~Hello world;"))
    print(evaluate("print~The next line shows that it can do loops.;"))
    print(evaluate("loop~3~print~Three times.;"))
    print(evaluate("print~The next line shows how it can pick up invalid arguments in a loop.;"))
    print(evaluate("loop~three~print~See?;"))
    print(evaluate("print~The next line shows that it can identify an invalid function.;"))
    print(evaluate("interpreter~cantUnderstandThisFunction;"))

#DumPy reader    
dumPy()
