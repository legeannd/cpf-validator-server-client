def cpfValidator(data):
    
    if(len(data)!=11):
        return False
    else:
        sum = 0
        b = 1
        number = list(data)

        number.pop(9)
        number.pop(9)

        for j in number:
            mult = 11 - b
            sum = sum + int(j) * mult
            b+=1

        ult = sum%11

        if(ult < 2):
            number.append('0')
        else:
            ult = (11 - ult)
            number.append(str(ult))

        sum = 0
        b = 1

        for j in number:
            mult = 12 - b
            sum = sum + int(j) * mult
            b+=1

        ult = sum%11

        if(ult < 2):
            number.append('0')
        else:
            ult = (11 - ult)
            number.append(str(ult))    

        i = 0
        word = ''
        while (i < 11):
            word+=number[i]
            i+=1

        if(word == data):
            return True
        else: 
            return False