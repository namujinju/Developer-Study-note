def meeting(s):
    arr = []
    s = s.split(";")
    
    
    for i in s:
        i = i.upper().split(":")
        tuple_str = "(" + i[1] + ", " + i[0] + ")"
        arr.append(tuple_str)
        
    
    return "".join(list(sorted(arr)))

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
print(meeting(s))