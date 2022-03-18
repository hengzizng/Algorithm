import java.io.*;
import java.util.StringTokenizer;

public class BJ14500 {
    public static int maxValue, maxSum, N, M;
    public static int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1}; // 상, 하, 좌, 우
    public static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        ////// test
        String test = "4 10\n" + "1 2 1 2 1 2 1 2 1 2\n" + "2 1 2 1 2 1 2 1 2 1\n" + "1 2 1 2 1 2 1 2 1 2\n" + "2 1 2 1 2 1 2 1 2 1";
        in = new BufferedReader(new StringReader(test));
        ////// test

        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        N = Integer.parseInt(st.nextToken()); // 행 수
        M = Integer.parseInt(st.nextToken()); // 열 수

        board = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(in.readLine(), " ");
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                maxValue = Math.max(maxValue, board[i][j]);
            }
        }

        boolean[][] checked = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                checked[i][j] = true;
                getTetromino(i, j, 1, board[i][j], checked);
                checked[i][j] = false;
            }
        }

        System.out.println(maxSum);
    }

    // (r, c) : 현재 확인할 위치, count: 지금까지 포함한 칸의 수
    // sum: 지금까지 포함한 칸에 적힌 수의 합, checked: 칸 포함여부 체크
    public static void getTetromino(int r, int c, int count, int sum, boolean[][] checked) {
        // 남은 칸들이 모두 최대값이더라도 이미 구한 max값보다 작다면
        if (sum + (maxValue * (4 - count)) < maxSum) {
            return;
        }

        // maxSum보다 작은 값들은 모두 위 if문에서 걸러졌기 때문에 sum이 maxSum이 된다.
        if (count == 4) {
            maxSum = sum;
            return;
        }

        // 현재 위치에서 인접한 네 방향을 탐색한다.
        int nr, nc;
        for (int i = 0; i < 4; i++) {
            nr = r + dr[i];
            nc = c + dc[i];

            if (nr < 0 || nr >= N || nc < 0 || nc >= M || checked[nr][nc]) {
                continue;
            }

            checked[nr][nc] = true;
            getTetromino(nr, nc, count + 1, sum + board[nr][nc], checked);
            // 2개 칸을 포함했을 때 nr, nc로 안가고 현재 위치에서 한번 더 인접한 네 방향을 탐색하면
            // ㅏ, ㅓ, ㅜ, ㅗ 모양을 만들 수 있다.
            if (count == 2) {
                getTetromino(r, c, count + 1, sum + board[nr][nc], checked);
            }
            checked[nr][nc] = false;
        }
    }
}
