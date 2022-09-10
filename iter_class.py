from functools import reduce


class FlatIterator:
    

    def __init__(self,lst:list):

       flag = 1
       l1 = lst
       l = []
       while flag:
        flag = 0
        for ls in l1:
            if isinstance(ls,list):
                l.extend(ls)
            else:
                l.append(ls)
        l1 = l
        l = []
        for ls in l1:
            if isinstance(ls,list):
                flag = 1


       self.lst = l1
       self.start = 0
       self.end = int(len(l1))


   
    def __iter__(self):

        self.cursor = self.start - 1
        return self


    def __next__(self):


        self.cursor +=1
        if self.cursor >= self.end:
            raise StopIteration
        i = int(self.cursor)

        return self.lst[i]


        