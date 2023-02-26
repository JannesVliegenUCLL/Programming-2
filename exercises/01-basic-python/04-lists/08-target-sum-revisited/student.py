# Write your code here
def target_sum(ns,target):
    for x in ns:
        for y in ns:
            if ns.index(y) != ns.index(x) and y+x==target:
                return True
        
    return False
                
                
            
           
            