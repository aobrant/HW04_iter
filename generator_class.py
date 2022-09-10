def flat_generator(lst:list,start=0):
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
        end = len(l1)
        while start < end:
            yield l1[start]
            start +=1
  