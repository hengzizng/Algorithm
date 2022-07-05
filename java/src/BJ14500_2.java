import java.io.*;
import java.util.*;

public class BJ14500_2 {
    public static int N, M, maxNum, maxSum;
    public static int[][] board, drdc = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    public static boolean[][] checked;

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        ////// test
        String test = "4 10\n" + "1 2 1 2 1 2 1 2 1 2\n" + "2 1 2 1 2 1 2 1 2 1\n" + "1 2 1 2 1 2 1 2 1 2\n" + "2 1 2 1 2 1 2 1 2 1";
        in = new BufferedReader(new StringReader(test));
        ////// test

        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        N = Integer.parseInt(st.nextToken()); // 행 수
        M = Integer.parseInt(st.nextToken()); // 열 수
        board = new int[N][M]; // 종이에 적혀있는 수
        checked = new boolean[N][M]; // 방문체크를 위한 배열

        for (int n = 0; n < N; n++) {
            st = new StringTokenizer(in.readLine(), " ");
            for (int m = 0; m < M; m++) {
                board[n][m] = Integer.parseInt(st.nextToken());
                maxNum = Math.max(maxNum, board[n][m]);
            }
        }

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                plus(r, c, 0, 0);
            }
        }

        System.out.println(maxSum);
    }

    public static void plus(int r, int c, int count, int sum) {
        if (sum + maxNum * (4 - count) < maxSum) {
            return;
        }

        if (count == 4) {
            maxSum = Math.max(maxSum, sum);
            return;
        }

        for (int d = 0; d < 4; d++) {
            int nr = r + drdc[d][0], nc = c + drdc[d][1];

            if (nr >= 0 && nr < N && nc >= 0 && nc < M && !checked[nr][nc]) {
                checked[nr][nc] = true;
                plus(nr, nc, count + 1, sum + board[nr][nc]);
                checked[nr][nc] = false;

                if (count == 2) {
                    checked[nr][nc] = true;
                    plus(r, c, count + 1, sum + board[nr][nc]);
                    checked[nr][nc] = false;
                }
            }
        }
    }
}
