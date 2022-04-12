# <입력>
# [열, 행, 0/1(기둥/보), 0/1(삭제/설치)]
# <출력>
# [열, 행, 0/1(기둥/보)] -> 오름차순

# 수행 결과가 조건을 만족하지 않는 작업은 무시

# 기둥은 (r, c), (r + 1, c) 에 설치
# 보는 (r, c), (r, c + 1) 에 설치

def solution(n, build_frame):
    # 기둥 조건 확인
    def check_col(r, c):
        # 기둥이 바닥 위에 있거나 다른 기둥 위에 있는지 확인
        if r == 0 or (c, r - 1, 0) in structure:
            return True

        # 기둥이 보의 한쪽 끝 부분 위에 있는지 확인
        if (c, r, 1) in structure or (c - 1, r, 1) in structure:
            return True

        return False

    # 보 조건 확인
    def check_row(r, c):
        # 보의 한쪽 끝 부분이 기둥 위에 있는지 확인 (바닥에 설치하는 경우는 없음)
        if (c, r - 1, 0) in structure or (c + 1, r - 1, 0) in structure:
            return True

        # 보가 양쪽 끝 부분이 다른 보와 연결되어 있는지 확인
        if (c - 1, r, 1) in structure and (c + 1, r, 1) in structure:
            return True

        return False

    result = []
    structure = set()

    for x, y, a, b in build_frame:
        now_structure = (x, y, a)
        if b == 0:  # 삭제
            structure.remove(now_structure)
        else:  # 설치
            structure.add(now_structure)

        # 변화가 일어날 때마다 모든 구조물에 대해 규칙을 지키고 있는지 확인
        flag = True
        for c, r, structure_type in structure:
            if structure_type == 0:  # 기둥
                flag = flag & check_col(r, c)
            else:  # 보
                flag = flag & check_row(r, c)

            # 하나라도 규칙을 지키지 않고 있다면
            if not flag:
                if b == 0:  # 삭제
                    structure.add(now_structure)
                else:  # 설치
                    structure.remove(now_structure)
                break

    result = list(structure)
    result.sort()

    return result


print(solution(5,
               [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])
      )
print([[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]])
