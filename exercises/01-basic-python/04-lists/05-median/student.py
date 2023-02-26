# Write your code here
def median(ns):
    ns_sorted = sorted(ns)
    if len(ns) % 2 != 0:
        return ns_sorted[len(ns)//2]
    else:
        return (ns_sorted[len(ns)//2-1] + ns_sorted[len(ns)//2])/2