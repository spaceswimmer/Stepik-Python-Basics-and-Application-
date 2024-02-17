class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
            return super().append(x)    #'super()' is important here, because you want to search for
        else:                           #'append()' in 'list' class and not in your new instance 
            raise NonPositiveError()

#Testing
test_list = PositiveList([12,2,3,5])
test_list.append(int(input()))
print(test_list)