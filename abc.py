val = input ("Please Enter the Phone Number ") 

dict ={
"A":"2","B":"2","C":"2",
"D":"3","E":"3","F":"3",
"G":"4", "H":"4", "I":"4",
"J":"5","K":"5","L":"5",
"M":"6","N":"6","O":"6",
"P":"7", "Q":"7", "R":"7","S":"7",
"T":"8","U":"8","V":"8",
"W":"9","X":"9","Y":"0", "Z" : "9"
}

result  = "";

for c in val:
    s = ""
    s =  s+ c
    if( s.isalpha() ):
        result = result + dict[s]
    else:
        result = result + s;
        
print(result)
