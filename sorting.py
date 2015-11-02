

def msort(array):
    n = len(array)
    if n <= 1:
        return array
    left = array[:n/2]
    right = array[n/2:]
    return merge(msort(left), msort(right))

def merge(array1, array2):
    merged_array = []
    while array1 or array2:
        if not array1:
            merged_array.append(array2.pop(0))
        elif (not array2) or array1[0] < array2[0]:
            merged_array.append(array1.pop(0))
        else:
            merged_array.append(array2.pop(0))
    return merged_array

def qsort(array):
    if len(array) <= 1:
        return array
    else:
        # the pop permanently changes initial array!
        pivot = array.pop(int(len(array)/2))
        a_lower = []
        a_higher = []
        for ii in range(0,len(array)):
            if array[ii]<=pivot:
                a_lower.append(array[ii])
            else:
                a_higher.append(array[ii])
        return qsort(a_lower) + [pivot] + qsort(a_higher)


a = [9,2,5,6,7,1,8,4,3]
b = list(a)
print "Starting array = ", a
print "Qsorted array = ", qsort(b)
# a = [9,2,5,6,7,1,8,4,3]
msorted_a = msort(a)
print "Msorted array = ", msorted_a
