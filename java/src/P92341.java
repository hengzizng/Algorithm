import java.util.*;

// 60 min
//테스트 1 〉	통과 (0.63ms, 76.8MB)
//테스트 2 〉	통과 (0.42ms, 73.3MB)
//테스트 3 〉	통과 (0.88ms, 72.1MB)
//테스트 4 〉	통과 (1.29ms, 77.1MB)
//테스트 5 〉	통과 (1.77ms, 68.6MB)
//테스트 6 〉	통과 (1.88ms, 75.6MB)
//테스트 7 〉	통과 (4.69ms, 91.5MB)
//테스트 8 〉	통과 (3.42ms, 75.6MB)
//테스트 9 〉	통과 (1.50ms, 77.5MB)
//테스트 10 〉	통과 (4.37ms, 80.4MB)
//테스트 11 〉	통과 (4.83ms, 81MB)
//테스트 12 〉	통과 (5.35ms, 80.8MB)
//테스트 13 〉	통과 (0.58ms, 75.3MB)
//테스트 14 〉	통과 (0.42ms, 75.6MB)
//테스트 15 〉	통과 (0.40ms, 70.8MB)
//테스트 16 〉	통과 (0.40ms, 79.2MB)

public class P92341 {
    public static void main(String[] args) {
        solution(new int[]{1, 461, 1, 10}, new String[]{"00:00 1234 IN"});
    }

    public static int[] solution(int[] fees, String[] records) {
        // fees: [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)]
        // 입차 후 출차하지 않았으면 23:59에 출차한 것으로 간주
        // 입출차 여러 번 가능
        // records는 시각을 기준으로 오름차순 정렬
        // 차량번호 작은차부터 요금 정렬해서 리턴

        // 누적 주차 시간 <= 기본 시간 : 기본 요금
        // 누적 주차 시간 > 기본 시간 : 기본 요금 + 초과한 시간에 대한 요금
        //   초과한 시간에 대한 요금 : 올림(초과한 시간 / 단위 시간) * 단위 요금

        StringTokenizer st = null;

        // 각 차량별 분으로 변환된 입차 시각을 저장
        Map<String, Integer> enterTime = new HashMap<String, Integer>();
        // 각 차량별 분단위 누적 주차 시간을 저장
        Map<String, Integer> totalTime = new HashMap<String, Integer>();

        // 각 차량별로 누적 시간을 구한다.
        for (int i = 0; i < records.length; i++) {
            st = new StringTokenizer(records[i], " ");
            String timeString = st.nextToken(); // 입/출차 시각
            String carNo = st.nextToken(); // 차량번호
            String inOrOut = st.nextToken(); // 내역(IN 또는 OUT)

            st = new StringTokenizer(timeString, ":");
            int time = Integer.parseInt(st.nextToken()) * 60 + Integer.parseInt(st.nextToken());

            if ("IN".equals(inOrOut)) { // 입차일 경우
                enterTime.put(carNo, time);
            } else { // 출차일 경우
                if (!totalTime.containsKey(carNo)) {
                    totalTime.put(carNo, 0);
                }

                time = totalTime.get(carNo) + (time - enterTime.get(carNo));
                totalTime.put(carNo, time);

                enterTime.put(carNo, -1); // 마지막까지 출차되지 않은 차량을 구분하기 위한 값
            }
        }

        for (String carNo : enterTime.keySet()) {
            int time = 0;
            // 마지막까지 출차되지 않은 차량의 누적 시간을 더한다
            if (enterTime.get(carNo) != -1) {
                if (!totalTime.containsKey(carNo)) {
                    totalTime.put(carNo, 0);
                }

                time = totalTime.get(carNo) + ((23 * 60 + 59) - enterTime.get(carNo));
                totalTime.put(carNo, time);
            }
        }

        int index = 0;
        int[][] feeByCar = new int[totalTime.size()][2]; // {{차량번호}{요금}}
        for (String carNo : totalTime.keySet()) {
            // 차량번호 저장
            feeByCar[index][0] = Integer.parseInt(carNo);

            // 요금을 구한다
            int time = totalTime.get(carNo) - fees[0]; // 기본 시간 제외
            feeByCar[index][1] = fees[1]; // 기본 요금을 기본값으로 둔다
            if (time > 0) {
                // 초과한 시간에 대한 요금 : 올림(초과한 시간 / 단위 시간) * 단위 요금
                if (time % fees[2] > 0) {
                    feeByCar[index][1] += ((time / fees[2]) + 1) * fees[3];
                } else {
                    feeByCar[index][1] += (time / fees[2]) * fees[3];
                }
            }

            index++;
        }

        Arrays.sort(feeByCar, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });

        int[] answer = new int[feeByCar.length];
        for (int i = 0; i < feeByCar.length; i++) {
            answer[i] = feeByCar[i][1];
        }

        return answer;
    }
}
