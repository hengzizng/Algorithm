from collections import defaultdict


def solution(orders, course):
    def get_order_count(new_course): # 각 코스별로 몇 번 주문되었는지 count
        count = 0
        for order in orders:
            if new_course & set(order) == new_course:
                count += 1
        return count
        
    def make_course(target_count, index, count, selected):
        if count == target_count: # 코스 조합을 다 만들었다
            order_count = get_order_count(set(selected)) # 만든 코스가 주문된 횟수를 구한다
            
            if order_count < 2: # 주문 횟수가 2보다 작다면 저장할 필요 없다
                return
            
            courses[order_count].add(''.join(selected))
            return
        
        if index == len(order):
            return
        
        selected[count] = order_arr[index]
        make_course(target_count, index + 1, count + 1, selected)
        make_course(target_count, index + 1, count, selected)

        
    result = set()
    for target_count in course: # 만들어야할 코스의 단품 개수
        courses = defaultdict(set) # 주문횟수 별 코스들
        for order in orders: # 주문별로 반복
            order_arr = sorted(list(order)) # 문자열을 분리해 정렬한 리스트

            selected = [''] * target_count # 코스 조합을 만들기 위해 사용하는 배열
            make_course(target_count, 0, 0, selected)

        if courses:
            max_count = max(courses.keys())
            result = result | courses[max_count]
    
    return sorted(list(result))