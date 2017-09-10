class Averager():
    def __init__(self):
        self.series = []

    def __call__(self,new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)
        
equivalent using closures
def make_average():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager

#efficient way
def make_average():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count,total #nonlocal because mutable variables become local on assignemnt and cannot be used as closures
        count += 1
        total += new_value
        return total/count

    return averager

avg = make_average()
avg(10)
avg(11)
print(avg(12))