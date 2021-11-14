def solution(n):
    # 3진법 문자열로 변경
    def to_ternary_str(target):
        ternary = ""
        
        while target > 0:
            # 뒤집어야하기 때문에 새로운 숫자를 앞이 아닌 뒤에 붙인다.
            ternary += str(target % 3)
            target = target // 3
            
        return ternary
    
    def to_decimal(target):
        decimal = 0
        
        for i in range(len(target)):
            # 뒤에서부터 3의 0제곱 ~ 을 곱해서 더한다.
            decimal += (3 ** i) * int(target[-1 * (i + 1)])
        
        return decimal
        
        
    return to_decimal(to_ternary_str(n))