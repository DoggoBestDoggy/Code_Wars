def score(dice):
    result = 0
    
    listCount = {}
    for i in dice:
        listCount[i] = dice.count(i)
        
    for key,value in listCount.items():
        while value>0:
            if value >= 3:
                if key>1:
                    result += key*100
                else:
                    result += 1000
                value-=2
            elif key == 1:
                result += 100
            elif key == 5:
                result += 50
            value-=1
            
        else:
                value = 0
                
    return result