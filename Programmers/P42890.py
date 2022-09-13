def solution(relation):
    # 최소성을 만족하는지 여부
    def is_min(bin_key):
        for candidate_key in candidate_keys:
            if bin_key & candidate_key == candidate_key:
                return False
        return True

    # 유일성을 만족하는지 여부
    def is_unique(key):
        values = set()
        # 모든 행 반복
        for row in range(row_cnt):
            # 키로 선택된 열끼리 합친 값을 만든다
            value = ''
            for col in key:
                value += relation[row][col] + " "
            # 만들어진 값을 이미 가지고 있다면 유일성을 만족하지 않는다
            if value in values:
                return False
            values.add(value)
        return True

    # 후보키로 만들 열을 선택한다
    def make_key(key_cnt, cnt, start, key, bin_key):
        if key_cnt == cnt:
            if is_unique(key):
                candidate_keys.add(bin_key)
            return

        for col in range(start, col_cnt):
            key[cnt] = col
            new_bin_key = bin_key | (1 << col)
            if is_min(new_bin_key):
                make_key(key_cnt, cnt + 1, col + 1, key, new_bin_key)

    row_cnt = len(relation)
    col_cnt = len(relation[0])
    candidate_keys = set()
    for key_cnt in range(1, col_cnt + 1):
        make_key(key_cnt, 0, 0, [-1] * key_cnt, 0)

    return len(candidate_keys)
