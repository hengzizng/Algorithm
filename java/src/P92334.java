// 40분
//테스트 1 〉	통과 (0.15ms, 75.1MB)
//테스트 2 〉	통과 (0.19ms, 73.1MB)
//테스트 3 〉	통과 (130.96ms, 138MB)
//테스트 4 〉	통과 (0.34ms, 81.1MB)
//테스트 5 〉	통과 (0.41ms, 74MB)
//테스트 6 〉	통과 (4.17ms, 74.2MB)
//테스트 7 〉	통과 (5.09ms, 86.4MB)
//테스트 8 〉	통과 (11.07ms, 111MB)
//테스트 9 〉	통과 (89.31ms, 133MB)
//테스트 10 〉	통과 (59.01ms, 126MB)
//테스트 11 〉	통과 (113.78ms, 150MB)
//테스트 12 〉	통과 (0.92ms, 76.8MB)
//테스트 13 〉	통과 (0.89ms, 71.1MB)
//테스트 14 〉	통과 (80.43ms, 140MB)
//테스트 15 〉	통과 (98.19ms, 154MB)
//테스트 16 〉	통과 (1.10ms, 74.6MB)
//테스트 17 〉	통과 (0.67ms, 86.1MB)
//테스트 18 〉	통과 (1.57ms, 76.7MB)
//테스트 19 〉	통과 (2.34ms, 83.8MB)
//테스트 20 〉	통과 (66.30ms, 138MB)
//테스트 21 〉	통과 (106.32ms, 155MB)
//테스트 22 〉	통과 (0.13ms, 71.4MB)
//테스트 23 〉	통과 (0.17ms, 80MB)
//테스트 24 〉	통과 (0.12ms, 76.2MB)

import java.util.*;

public class P92334 {
    public static int userCount; // 총 유저 수

    public static void main(String[] args) {

        // 한 유저는 서로 다른 유저를 계속해서 신고 가능
        // 한 유저가 다른 한 유저를 여러 번 신고하면 신고 횟수는 1회로 처리
        // -> 한 유저의 최대 신고 횟수 = 한 유저가 받을 수 있는 최대 신고 횟수 = (유저 수 - 1)

        // 신고를 k번 이상 받은 유저는 게시판 이용 정지
        // 이용 정지당한 유저를 신고한 유저에게 알림

        // {신고당한 유저1 : [신고한 유저1, 신고한 유저2, ...], 신고당한 유저2: {}}
        // -> {신고한 유저1 : 신고횟수, 신고한 유저2 : 신고횟수, ...}

        String[] id_list = new String[] {"con", "ryan"};
        String[] report = new String[] {"ryan con", "ryan con", "ryan con", "ryan con"};
        int[] answer = solution(id_list, report, 2);
        System.out.println(Arrays.toString(answer));
    }

    public static int[] solution(String[] id_list, String[] report, int k) {
        userCount = id_list.length;

        // 유저 이름 -> 인덱스 로 변경하기 위한 map
        Map<String, Integer> userMap = new HashMap<>();
        for (int i = 0; i < userCount; i++) {
            userMap.put(id_list[i], i);
        }

        // reportersByUser[신고당한 유저1] = [신고한 유저1, 신고한 유저2, ...]
        HashSet<String>[] reportersByUser = new HashSet[userCount];
        StringTokenizer st = null;
        for (int i = 0; i < report.length; i++) {
            st = new StringTokenizer(report[i], " ");
            String reporter = st.nextToken(); // 신고한 사람
            int reporteeIndex = userMap.get(st.nextToken()); // 신고당한 사람 인덱스

            if (reportersByUser[reporteeIndex] == null) {
                reportersByUser[reporteeIndex] = new HashSet<String>();
            }

            reportersByUser[reporteeIndex].add(reporter);
        }

        // 인덱스에 해당하는 유저가 다른 유저를 정지시킨 횟수
        int[] makeStopCount = new int[userCount];
        for (int user = 0; user < userCount; user++) {
            // 만약 user가 정지당했다면
            if (reportersByUser[user] != null && reportersByUser[user].size() >= k) {
                // user를 신고한 유저의 카운트를 증가시킨다
                for (String reporter : reportersByUser[user]) {
                    makeStopCount[userMap.get(reporter)]++;
                }
            }
        }

        return makeStopCount;
    }
}