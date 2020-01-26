def ema(n):
    try:
        i = 0           #Counter
        a = []          #Empty array

        while i < n:
            a.append(0)
            i = i + 1

        return (a)
    
    except:
        return("Invalid argument in the function call")
