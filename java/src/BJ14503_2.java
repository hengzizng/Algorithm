import java.io.*;
import java.util.StringTokenizer;

public class BJ14503_2 {
    public static int N, M, cleanCount, map[][];
    public static int[][] drdc = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}}; // 북, 동, 남, 서
    public static boolean[][] isClean;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        ///// test
        String test1 = "3 3\n" + "1 1 0\n" + "1 1 1\n" + "1 0 1\n" + "1 1 1";
        String test2
                = "11 10\n" + "7 4 0\n" + "1 1 1 1 1 1 1 1 1 1\n" + "1 0 0 0 0 0 0 0 0 1\n" + "1 0 0 0 1 1 1 1 0 1\n" + "1 0 0 1 1 0 0 0 0 1\n" + "1 0 1 1 0 0 0 0 0 1\n" + "1 0 0 0 0 0 0 0 0 1\n" + "1 0 0 0 0 0 0 1 0 1\n" + "1 0 0 0 0 0 1 1 0 1\n" + "1 0 0 0 0 0 1 1 0 1\n" + "1 0 0 0 0 0 0 0 0 1\n" + "1 1 1 1 1 1 1 1 1 1";
        in = new BufferedReader(new StringReader(test1));
        ///// test

        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        N = Integer.parseInt(st.nextToken()); // 세로 크기
        M = Integer.parseInt(st.nextToken()); // 가로 크기

        st = new StringTokenizer(in.readLine(), " ");
        int robotR = Integer.parseInt(st.nextToken()); // 로봇청소기 행 위치
        int robotC = Integer.parseInt(st.nextToken()); // 로봇청소기 열 위치
        int robotD = Integer.parseInt(st.nextToken()); // 로봇청소기 방향

        map = new int[N][M]; // 지도
        isClean = new boolean[N][M]; // 청소했는지 여부
        for (int n = 0; n < N; n++) {
            st = new StringTokenizer(in.readLine(), " ");
            for (int m = 0; m < M; m++) {
                map[n][m] = Integer.parseInt(st.nextToken());
            }
        }

        work(robotR, robotC, robotD);

        System.out.println(cleanCount);
    }

    public static void work(int r, int c, int d) {
        // 1. 현재 위치를 청소한다.
        isClean[r][c] = true;
        cleanCount++;

        int[] next = check(r, c, d, 0);
        if (next[0] > -1) {
            work(next[0], next[1], next[2]);
        }
    }

    public static int[] check(int r, int c, int d, int checkCount) {
        // 2. 왼쪽 방향부터 차례대로 인접한 칸을 탐색
        int nd = (d + 3) % 4; // 현재 방향에서 왼쪽 방향
        int nr = r + drdc[nd][0], nc = c + drdc[nd][1];
        if (isValid(nr, nc) && !isClean[nr][nc]) { // a. 왼쪽 방향 청소 가능
            return new int[]{nr, nc, nd};
        } else { // b. 청소 불가능
            if (checkCount < 4) { // 네 방향 모두 확인 전
                return check(r, c, nd, checkCount + 1);
            } else { // 네 방향 모두 확인
                // 후진
                nd = (d + 2) % 4;
                nr = r + drdc[nd][0];
                nc = c + drdc[nd][1];
                if (isValid(nr, nc)) { // 후진 가능
                    return check(nr, nc, d, 0);
                } else { // 후진 불가능
                    return new int[]{-1};
                }
            }
        }
    }

    public static boolean isValid(int r, int c) {
        if (r < 0 || r >= N || c < 0 || c >= M || map[r][c] == 1) {
            return false;
        } else {
            return true;
        }
    }
}
