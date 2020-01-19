def high(arr):

    h = 0               #Highest element
    i = 0               #Counter
    t = 0               #Temp var

    
    try:
        while (i <= (len(arr)-1)): 
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

    l = arr[0]          #Lowest element
    i = 0               #Counter
    t = 0               #Temp var

    try:
        while (i <= (len(arr)-1)): 
            t = arr[i]
            i = i + 1
        
            if t <= l:
                l = t
            else:
                pass
    except:
        return("Error: invalid element in the array")

    return(l)


e = [2, 4, 1, 312, 1, 31298, 3719, 312, -1.3, -1.31, -0.5, 312]
h = low(e)
print (h)
