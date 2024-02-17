#Creating a dict with all values
exception_dict = {}
#Putting values into the dict
for _ in range(int(input())):
    #Have to do this because sometimes exceptions have no parents
    child = None
    parents = None
    input_string = input()
    if ':' in input_string:
        child, parents = input_string.split(' : ')
        parents = parents.split()
    else:
        child = input_string

    #We need this to create the key for the 1 instance
    if not (child in exception_dict):
        exception_dict[child] = []

    #Adding parents to dict if the exception has any
    if parents != None:
        for par in parents:
            if not (par in exception_dict[child]):
                exception_dict[child].append(par)

#Recursive breadth search function 
def is_related(child, parent):
    #Have to check if parent = child and parent = obj because they are always True
    if (parent in exception_dict[child]) or (parent == child):
        return True
    else:
        for chld in exception_dict[child]:
            if is_related(chld, parent):
                return True

result = []
prev_exceptions = []

#Checking for relation
for _ in range(int(input())):
    current_exception = input()

    if len(prev_exceptions) == 0:
        prev_exceptions.append(current_exception)
        continue

    for exc in prev_exceptions:
        if is_related(current_exception, exc):
            result.append(current_exception)
            break

    prev_exceptions.append(current_exception)

for ans in result:
    print(ans)