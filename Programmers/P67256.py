def solution(numbers, hand):
    hands = [[3, 0], [3, 2]] # 왼손, 오른손의 위치
    
    def find_near_hand(row, col, hand):
        left_distance = abs(row - hands[0][0]) + abs(col - hands[0][1])
        right_distance = abs(row - hands[1][0]) + abs(col - hands[1][1])

        if left_distance < right_distance:
            hands[0] = [row, col]
            return 'L'
        elif left_distance > right_distance:
            hands[1] = [row, col]
            return 'R'
        else:
            if hand == 'left':
                hands[0] = [row, col]
                return 'L'
            else:
                hands[1] = [row, col]
                return 'R'

    answer = ""
    for number in numbers:
        number = 10 if number == 0 else number - 1
        row = number // 3
        col = number % 3
        if col == 0:
            hands[0][0], hands[0][1] = row, col
            answer += 'L'
        elif col == 2:
            hands[1][0], hands[1][1] = row, col
            answer += 'R'
        else:
            answer += find_near_hand(row, col, hand)

    return answer

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))
print("LRLLRRLLLRR")