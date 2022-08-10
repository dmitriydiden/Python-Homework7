import re
a = "2-(1+5)*6+(6+2)+5+(3+7)*3"
def calc_int(x):
    list = []
    for i in x:
        list.append(i)
    i = 0 
    result = 0
    list1 = []
     
    while i < len(list):
        if list[i] == '(' and (len(list)>5) and (list[i+5] == '*' or list[i+5] == '/'):
            if list[i+2]=='+':
                result = result + (int(list[i+1])+int(list[i+3]))
            elif list[i+2]=='-':
                result = result + (int(list[i+1])-int(list[i+3]))
            if list[i+5]=='*':
                result = result*int(list[i+6])
            elif list[i+5]=='/':
                result = result/int(list[i+6])
            list1.append(str(result))
            result = 0
            for j in range(6):
                list.pop(i)
            
        elif list[i] == '(':
            if list[i+2]=='+':
                    result = result + (int(list[i+1])+int(list[i+3]))
            elif list[i+2]=='-':
                    result = result + (int(list[i+1])-int(list[i+3]))
            list1.append(result)
            result = 0
            for j in range(4):
                list.pop(i)
        else:
            list1.append(list[i])      
        i+=1
    result = int(list1[0])
    i=0
    while i < len(list1):
        match list1[i]:
            case '+': result+=int(list1[i+1])
            case '-': result-=int(list1[i+1])
        i+=1
    return result   
def calc_float(x):    
    str = ''
    list = []
    for i in x:
        if i != '-' and i != '+' and i != '*' and i != '/' and i != '(' and i != ')':
            str+=i
        else:
            list.append(str)
            str = ''
        match i:
            case '-': list.append(i)
            case '+': list.append(i)
            case '*': list.append(i)
            case '/': list.append(i)
            case '(': list.append(i)
            case ')': list.append(i)
    
    list.append(str)
    i=0
    while i < (len(list)):
        if list[i] == '':
            list.pop(i)
        i+=1
            
    i = 0 
    result = 0.0
    list1 = []
    
    while i < len(list):
        if list[i] == '(' and (len(list)>5) and (list[i+5] == '*' or list[i+5] == '/'):
            if list[i+2]=='+':
                result = result + (float(list[i+1])+float(list[i+3]))
            elif list[i+2]=='-':
                result = result + (float(list[i+1])-float(list[i+3]))
            if list[i+5]=='*':
                result = result*float(list[i+6])
            elif list[i+5]=='/':
                result = result/float(list[i+6])
            list1.append((result))
            result = 0
            for j in range(6):
                list.pop(i)
                
        elif list[i] == '(':
            if list[i+2]=='+':
                    result = result + (float(list[i+1])+float(list[i+3]))
            elif list[i+2]=='-':
                    result = result + (float(list[i+1])-float(list[i+3]))
            list1.append(result)
            result = 0
            for j in range(4):
                list.pop(i)
        else:
            list1.append(list[i])      
        i+=1
    result = float(list1[0])
    i=0
    while i < len(list1):
        match list1[i]:
            case '+': result+=float(list1[i+1])
            case '-': result-=float(list1[i+1])
        i+=1
    return round(result, 1)

  




#    match list[i]:
#       case '(': list.pop(i)
#        case ')': list.pop(i)
#    i+=1
