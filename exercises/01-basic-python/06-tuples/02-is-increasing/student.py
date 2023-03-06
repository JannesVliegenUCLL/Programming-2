# Write your code here
def is_increasing(ns):
    if len(ns)>1:
        for (x, y) in zip(ns, ns[1:]):
            if x>y:
                return False
            return True
    return True

            

