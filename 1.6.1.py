#Creating a dict with all values
mre_dict = {}
#Putting values into the dict
for _ in range(int(input())):
    child, parents = input().split(' : ')
    parents = parents.split()

    #We need this to create the key for the 1 instance
    if not (child in mre_dict):
        mre_dict[child] = [child]

    #Adding values
    for par in parents:
        if not (par in mre_dict[child]):
            mre_dict[child].append(par)

result = []
for _ in range(int(input())):
    par, child = input().split()
    