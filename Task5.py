import re
 
 
actions = {
  "*": lambda x, y: str(float(x) * float(y)),
  "/": lambda x, y: str(float(x) / float(y)),
  "+": lambda x, y: str(float(x) + float(y)),
  "-": lambda x, y: str(float(x) - float(y))
}
 
priority = r"\((.+?)\)"
action = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
  
def my_eval(expresion):

    match = re.search(priority, expresion)
    
    while match:
        expresion = expresion.replace(match.group(0), my_eval(match.group(1)))
        match = re.search(priority, expresion)
 
    for symbol, acti in actions.items():
        
        match = re.search(action.format(symbol), expresion)
        
        while match:
            expresion = expresion.replace(match.group(0), acti(*match.groups()))
            match = re.search(action.format(symbol), expresion)
    
    return expresion
 
 
 
n = "(3 + 2) * 2 - (15 / 5)"
print(my_eval(n)) 
