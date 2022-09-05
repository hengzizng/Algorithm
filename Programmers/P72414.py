# play_time: 동영상 길이, adv_time: 광고 길이, logs: 시청 기록
def solution(play_time, adv_time, logs):
    # HH:MM:SS 형식의 시간 문자열을 초 단위로 변환하는 함수
    def time_to_sec(time_str):
        temp = time_str.split(':')
        return int(temp[0]) * 3600 + int(temp[1]) * 60 + int(temp[2])

    # 초 단위의 시간 정보를 HH:MM:SS 형식의 시간 문자열로 변환하는 함수
    def sec_to_time(sec):
        temp = []

        hour = sec // 3600
        minute = (sec % 3600) // 60

        temp.append(str(hour).zfill(2))
        temp.append(str(minute).zfill(2))
        temp.append(str(sec % 60).zfill(2))

        return ':'.join(temp)

    # 초 단위의 동영상, 광고 길이
    play_sec = time_to_sec(play_time)
    adv_sec = time_to_sec(adv_time)

    # 각 시각별로 시청자 수
    count_by_sec = [0] * 360001
    for no, log in enumerate(logs):
        start, end = log.split('-')
        # 초 단위의 시청 시작 시각, 시청 종료 시각
        start_sec, end_sec = time_to_sec(start), time_to_sec(end)

        count_by_sec[start_sec] += 1
        count_by_sec[end_sec] -= 1

    # [광고 시작 시각(초), 최고 누적 시청 시간]
    answer = [-1, -1]
    # 현재 누적 시청 시간
    time_sum = 0

    # 초 오름차순으로 확인
    for sec in range(play_sec + 1):
        # 누적합으로 시청자 수를 구한다.
        count_by_sec[sec] += count_by_sec[sec - 1]
        # sec를 광고 종료 시간으로 두었을 때 광고 시작 시간
        adv_start = sec - adv_sec + 1

        # 시청 시간 누적
        time_sum += count_by_sec[sec]
        if adv_start > 0:
            time_sum -= count_by_sec[adv_start - 1]

        # 누적 시간이 더 클 경우 답 갱신
        if adv_start >= 0 and time_sum > answer[1]:
            answer[0] = adv_start
            answer[1] = time_sum

    return sec_to_time(answer[0])
