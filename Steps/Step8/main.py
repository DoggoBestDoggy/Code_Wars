def solution(n):
    
    RNE = [
        
    (1989, "MCMLXXXIX"),
    (1889, "MDCCCLXXXIX"),
    (1000, "M"),
    (984, "CMLXXXIV"),
    (91, "XCI"),
    (89, "LXXXIX"),
    (21, "XXI"),
    (14, "XIV"),
    (6, "VI"),
    (4, "IV"),
    (1, "I"),
        
    ]
    
    result = ""
    
    for (num,r) in RNE:
        q, n = divmod(n,num)
        result += r*q
    
    return result