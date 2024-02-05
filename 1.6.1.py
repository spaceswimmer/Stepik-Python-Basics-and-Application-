#Creating a dict with all values
mre_dict = {}
#Putting values into the dict
for _ in range(int(input())):
    #Have to do this because sometimes classes have no parents
    child = None
    parents = None
    input_string = input()
    if ':' in input_string:
        child, parents = input_string.split(' : ')
        parents = parents.split()
    else:
        child = input_string

    #We need this to create the key for the 1 instance
    if not (child in mre_dict):
        mre_dict[child] = []

    #Adding parents to dict if the class has any
    if parents != None:
        for par in parents:
            if not (par in mre_dict[child]):
                mre_dict[child].append(par)

#Recursive breadth search function 
def is_related(child, parent):
    #Have to check if parent = child and parent = obj because they are always True
    if (parent in mre_dict[child]) or (parent == child) or (parent == 'Obj'):
        return True
    else:
        for chld in mre_dict[child]:
            if is_related(chld, parent):
                return True

#Creating answer buffer
result = []

#Checking for relation
for _ in range(int(input())):
    parent, child = input().split()
    if is_related(child, parent):
        result.append('Yes')
    else:
        result.append('No')

for ans in result:
    print(ans)
