class MoneyBox:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.money = 0
    
    def can_add(self, v: int):
        if v < 0 or not isinstance(v, int):
            return False

        return bool(self.money + v <= self.capacity)
        
    
    def add(self, v: int):
        if self.can_add(v):
            self.money += v

x = MoneyBox(15)
x.add(5)
x.add(9)
x.add(3)

print(x.money)
