class Queue:

    def __init__(self):
        self.__list = []
    
    def add(self,item):
        self.__list.append(item)

    
    def next(self):
        item=self.__list[0]
        del self.__list[0]
        return item
    def is_empty(self):
        return len(self.__list)==0           
