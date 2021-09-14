def solution(lines):
    def get_time(time_str):
        time_arr = time_str.split()
        T = int(float(time_arr[2][:-1]) * 1000) # 처리시간
        time_arr = time_arr[1].split(":")
        
        # start: 요청 시작 시간, end: 요청 종료 시간, after_sec: 요청 종료 후 0.999초 뒤
        end = (int(time_arr[0]) * (60 ** 2) + int(time_arr[1]) * 60) * 1000 + int(float(time_arr[2]) * 1000)
        start = end - (T - 1)
        after_sec = end + 999
        
        return [start, end, after_sec]
    
    
    times = []
    for log in lines:
        times.append(get_time(log))
    
    max_throughput = 0 # 초당 최대 처리량
    # time[0]: 요청 시작 시간, time[1]: 요청 종료 시간, time[2]: 요청 종료 후 0.999초 뒤
    for index, time in enumerate(times):
        throughput = 1 # 이번 케이스의 처리량
        for next_index in range(index + 1, len(lines)):
            if times[next_index][0] <= time[2]:
                throughput += 1
        max_throughput = max(max_throughput, throughput)
    
    return max_throughput