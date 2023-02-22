# Write your code here
def target_sum(ns,target):
    for x in range(ns):
        for y in range(ns):
            if x + y == target:
                return True