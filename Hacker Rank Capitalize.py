
name = ""

def solve(name):
    first_name = name.split(" ")[0]
    last_name = name.split(" ")[1]
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    print (first_name + " " + last_name)
    
solve('dan brown')
