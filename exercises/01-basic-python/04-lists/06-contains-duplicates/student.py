# Write your code here
def contains_duplicates(xs):
    for x in xs:
        if xs.count(x) > 1:
            return True
    return False