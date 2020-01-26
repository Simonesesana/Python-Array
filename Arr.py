def high(arr):

    h = 0               #Highest value
    i = 0               #Counter
    t = 0               #Temp var

    
    try:
        while (i < len(arr)): 
            t = arr[i]
            i = i + 1
        
            if t >= h:
                h = t
            else:
                pass
    except:
        return("Error: invalid element in the array")

    return (h)


def low(arr):

    l = arr[0]          #Lowest value
    i = 0               #Counter
    t = 0               #Temp var

    try:
        while (i < len(arr)): 
            t = arr[i]
            i = i + 1
        
            if t <= l:
                l = t
            else:
                pass
    except:
        return("Error: invalid element in the array")

    return(l)

def avg(arr):

    a = 0               #Average value
    i = 0               #Counter
    
    try:
        while (i < len(arr)):
            a = a + arr[i]
            i = i + 1

    except:
        return("Error: invalid element in the array")

    return(a/i)
