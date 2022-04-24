import java.io.*;
import java.util.*;

public class SWEA2383 {
    public static int N, minCompleteTime;
    public static List<int[]> people, stairs;

    public static void main(String[] args) throws Exception {
        // 내려가기 시작한 사람 수
        // 0 2 1 2 0 0 0 0 0
        // 각 시간별로 (4분이 걸리는)계단을 내려가고 있는 사람 수
        // 0 2 3 5 5 3 2 0 0 ->
        // 0 2 3 3 5 3 2 2 0 ->
        // 0 2 3 3 3 3 2 2 2

        ////// test
        System.setIn(new FileInputStream("testcase/2383input.txt"));
        ////// test
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

//        ////// test
//        String test = "1\n" + "5\n" + "0 1 1 0 0\n" + "0 0 1 0 3\n" + "0 1 0 1 0\n" + "0 0 0 0 0\n" + "1 0 5 0 0";
//        in = new BufferedReader(new StringReader(test));
//        ////// test

        int T = Integer.parseInt(in.readLine()); // 테스트케이스 수
        int temp;
        for (int t = 1; t <= T; t++) {
            N = Integer.parseInt(in.readLine()); // 방의 한 변의 길이
            minCompleteTime = N * 2 * 10; // 최소 완료 시간
            people = new ArrayList<>();
            stairs = new ArrayList<>();

            // 사람들과 계단의 위치를 저장한다.
            for (int r = 0; r < N; r++) {
                st = new StringTokenizer(in.readLine(), " ");
                for (int c = 0; c < N; c++) {
                    temp = Integer.parseInt(st.nextToken());
                    if (temp == 1) { // 사람
                        people.add(new int[]{r, c});
                    } else if (temp >= 2) { // 계단
                        stairs.add(new int[]{r, c, temp});
                    }
                }
            }

            // 각 사람이 내려갈 계단을 선택하고, 최소 완료 시간을 갱신한다.
            selectStair(0, new int[people.size()]);

            sb.append("#").append(t).append(" ").append(minCompleteTime).append("\n");
        }

        System.out.println(sb.toString());
    }

    // 계단을 내려가기 시작한 시간을 구한다.
    public static int getDepartTime(int[] stair, int[] person) {
        // 계단을 내려가기 시작한 시간 = 계단 입구까지 이동 시간 + 1
        return Math.abs(person[0] - stair[0]) + Math.abs(person[1] - stair[1]) + 1;
    }

    // 각 시간별로 계단을 내려가고 있는 사람 수를 구한다.
    // selected: 이용할 계단 번호
    public static void setGoCount(int[] selected) {
        int stairNo, departTime, duration, maxDepartTime = 0;
        int[][] goCount = new int[2][N * 2 * 10];

        for (int personNo = 0; personNo < people.size(); personNo++) {
            stairNo = selected[personNo];
            duration = stairs.get(stairNo)[2];
            departTime = getDepartTime(stairs.get(stairNo), people.get(personNo));
            maxDepartTime = Math.max(maxDepartTime, departTime);
            for (int i = 0; i < duration; i++) {
                goCount[stairNo][departTime + i]++;
            }
        }

        setMinCompleteTime(maxDepartTime, goCount);
    }

    // 모든 사람들이 계단을 완전히 내려간 시간을 구해서 최소 시간을 갱신한다.
    public static void setMinCompleteTime(int maxDepartTime, int[][] goCount) {
        int duration;

        for (int time = 0; time < minCompleteTime; time++) {
            for (int stairNo = 0; stairNo < 2; stairNo++) {
                duration = stairs.get(stairNo)[2];
                if (goCount[stairNo][time] > 3) {
                    goCount[stairNo][time + duration] += (goCount[stairNo][time] - 3);
                    goCount[stairNo][time] = 3;
                }

            }
            // 마지막으로 계단을 내려가기 시작한 사람도 다 내려갔다면 종료
            if (time > maxDepartTime && goCount[0][time] + goCount[1][time] == 0) {
                minCompleteTime = time;
                break;
            }
        }
    }

    public static void selectStair(int personNo, int[] selected) {
        if (personNo == people.size()) {
            setGoCount(selected);
            return;
        }

        // 첫 번째 계단 선택
        selected[personNo] = 0;
        selectStair(personNo + 1, selected);
        // 두 번째 계단 선택
        selected[personNo] = 1;
        selectStair(personNo + 1, selected);
    }

}
