import java.io.*;
import java.util.*;

public class BJ15683_2 {
    public static int N, M, zeroCount, maxCheckCount;
    public static int[][] drdc = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // 상하좌우
    public static int[][][] directionMap = { // CCTV별 방향 벡터
            {{0}, {1}, {2}, {3}}, // 1번 CCTV 방향 리스트
            {{0, 1}, {2, 3}}, // 2번 CCTV 방향 리스트
            {{0, 3}, {3, 1}, {1, 2}, {2, 0}}, // 3번 CCTV 방향 리스트
            {{0, 1, 2}, {0, 1, 3}, {0, 2, 3}, {1, 2, 3}}, // 4번 CCTV 방향 리스트
            {{0, 1, 2, 3}} // 5번 CCTV 방향 리스트
    };
    public static List<int[]> cctvs;

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        ////// test
        String test1 = "4 6\n" + "0 0 0 0 0 0\n" + "0 0 0 0 0 0\n" + "0 0 1 0 6 0\n" + "0 0 0 0 0 0";
        String test2 = "6 6\n" + "0 0 0 0 0 0\n" + "0 2 0 0 0 0\n" + "0 0 0 0 6 0\n" + "0 6 0 0 2 0\n" + "0 0 0 0 0 0\n" + "0 0 0 0 0 5";
        String test3 = "6 6\n" + "1 0 0 0 0 0\n" + "0 1 0 0 0 0\n" + "0 0 1 0 0 0\n" + "0 0 0 1 0 0\n" + "0 0 0 0 1 0\n" + "0 0 0 0 0 1";
        String test4 = "3 7\n" + "4 0 0 0 0 0 0\n" + "0 0 0 2 0 0 0\n" + "0 0 0 0 0 0 4";
        in = new BufferedReader(new StringReader(test4));
        ////// test

        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        N = Integer.parseInt(st.nextToken()); // 행 수
        M = Integer.parseInt(st.nextToken()); // 열 수
        cctvs = new ArrayList<>(); // cctv 정보 [행, 열, 종류]
        int[][] office = new int[N][M]; // 사무실 정보
        for (int n = 0; n < N; n++) {
            st = new StringTokenizer(in.readLine(), " ");
            for (int m = 0; m < M; m++) {
                int temp = Integer.parseInt(st.nextToken());
                office[n][m] = temp;
                if (temp == 0) {
                    zeroCount++;
                } else if (temp <= 5) {
                    cctvs.add(new int[]{n, m, temp - 1});
                }
            }
        }

        setDirection(0, 0, office);

        System.out.println(zeroCount - maxCheckCount);
    }

    // 각 CCTV의 방향을 정한다.
    public static void setDirection(int cctvNo, int checkCount, int[][] office) {
        if (cctvNo == cctvs.size()) {
            maxCheckCount = Math.max(maxCheckCount, checkCount);
            return;
        }

        int r = cctvs.get(cctvNo)[0], c = cctvs.get(cctvNo)[1], type = cctvs.get(cctvNo)[2];
        for (int direction = 0; direction < directionMap[type].length; direction++) {
            int[][] newOffice = copy(office);
            setDirection(cctvNo + 1, checkCount + check(r, c, type, direction, newOffice), newOffice);
        }
    }

    // 이번 CCTV로 감시할 수 있는 부분을 체크한다.
    public static int check(int r, int c, int type, int direction, int[][] office) {
        int checkCount = 0;
        Queue<int[]> queue = new LinkedList<>();

        for (int d : directionMap[type][direction]) {
            queue.offer(new int[]{r, c, d});
        }

        while (!queue.isEmpty()) {
            int[] now = queue.poll();

            r = now[0] + drdc[now[2]][0];
            c = now[1] + drdc[now[2]][1];
            if (r >= 0 && r < N && c >= 0 && c < M && office[r][c] < 6) {
                if (office[r][c] == 0) {
                    checkCount++;
                }

                queue.offer(new int[]{r, c, now[2]});
                office[r][c] = -1;
            }
        }

        return checkCount;
    }

    // 사무실 정보를 복사한다.
    public static int[][] copy(int[][] target) {
        int[][] copied = new int[N][M];

        for (int n = 0; n < N; n++) {
            for (int m = 0; m < M; m++) {
                copied[n][m] = target[n][m];
            }
        }

        return copied;
    }
}
