'''
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a
given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with
'good'. Return the resulting string.
'''
'''
s= "This man is not a poor."
pnot=s.find("not")
ppoor=s.find("poor")

print("Position of not :",pnot)
print("Position of poor :",ppoor)

if pnot<ppoor:
    print(s[:pnot]+"good")
 '''   
def not_poor(str1):
    snot=str1.find("not")
    spoor=str1.find("poor")
    if spoor>snot and spoor>0 and snot>0:
        str1 = str1.replace(str1[snot:(spoor+4)], 'good')
        return str1
    else:
        return str1
print(not_poor("the song is not that poor."))
    
