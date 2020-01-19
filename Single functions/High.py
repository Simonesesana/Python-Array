def high(arr):

    h = 0               #Highest value
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
