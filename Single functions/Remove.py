def rmv(arr, x):
    
    i = 0               #Counter
    a = []              #Array
    t = 0               #Temp var

    try:
        while (i < len(arr)):
            t = arr[i]
            i = i + 1
        
            if t == x:
                pass
            else:
                a.append(t)
        return(a)
    
    except:
        return("Error: invalid argument in the function call")
