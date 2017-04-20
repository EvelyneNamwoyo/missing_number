def find_missing(list1,list2):

    if len(list1)==len(list2):
        return 0

    elif len(list1)==0 and len(list2)==0:
        return 0
        
    else:
        for i in list2:
            if i not in list1:
                return i



print(find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66]))




            