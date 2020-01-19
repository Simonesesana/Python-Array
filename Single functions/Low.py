def low(arr):

    l = arr[0]          #Lowest value
    i = 0               #Counter
    t = 0               #Temp var

    try:
        while (i <= len(arr)): 
            t = arr[i]
            i = i + 1
        
            if t <= l:
                l = t
            else:
                pass
    except:
        return("Error: invalid element in the array")

    return(l)
