import java.io.*;
import java.util.StringTokenizer;

public class BJ19237 {
    // N: 격자 크기, M: 상어의 수, k: 냄새 유효 시간
    public static int N, M, k, sharks[][], board[][][], priority[][][];
    public static int sharkCount;
    public static int[][] drdc = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // 상 하 좌 우

    public static void main(String[] args) throws IOException {
        // 상어의 이동
        // - 가능한 칸이 여러 개일 때는 상어, 방향마다의 우선순위를 따른다.
        // - 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 있다면 가장 작은 번호의 상어만 남는다.
        //   -> 이동할 때 그 위치에 상어가 있다면 번호가 작은 상어만 남김
        // 1. 인접한 칸 중 냄새 없는 칸
        // 2. 자신의 냄새가 있는 칸

        // 1번 상어만 남게 되기까지 걸리는 시간
        // 1001초 이상이면 -1

        // board 에 있어야 할 정보
        // - 냄새가 뿌려진 시각(초)
        // - 냄새를 뿌린 상어 번호

        // sharks 에 있어야 할 정보
        // - 각 상어의 위치(행, 열)
        // - 각 상어의 방향

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        ///// test
        String test1
                = "5 4 4\n" + "0 0 0 0 3\n" + "0 2 0 0 0\n" + "1 0 0 0 4\n" + "0 0 0 0 0\n" + "0 0 0 0 0\n" + "4 4 3 1\n" + "2 3 1 4\n" + "4 1 2 3\n" + "3 4 2 1\n" + "4 3 1 2\n" + "2 4 3 1\n" + "2 1 3 4\n" + "3 4 1 2\n" + "4 1 2 3\n" + "4 3 2 1\n" + "1 4 3 2\n" + "1 3 2 4\n" + "3 2 1 4\n" + "3 4 1 2\n" + "3 2 4 1\n" + "1 4 2 3\n" + "1 4 2 3";
        String test2
                = "4 2 6\n" + "1 0 0 0\n" + "0 0 0 0\n" + "0 0 0 0\n" + "0 0 0 2\n" + "4 3\n" + "1 2 3 4\n" + "2 3 4 1\n" + "3 4 1 2\n" + "4 1 2 3\n" + "1 2 3 4\n" + "2 3 4 1\n" + "3 4 1 2\n" + "4 1 2 3";
        String test3
                = "5 4 1\n" + "0 0 0 0 3\n" + "0 2 0 0 0\n" + "1 0 0 0 4\n" + "0 0 0 0 0\n" + "0 0 0 0 0\n" + "4 4 3 1\n" + "2 3 1 4\n" + "4 1 2 3\n" + "3 4 2 1\n" + "4 3 1 2\n" + "2 4 3 1\n" + "2 1 3 4\n" + "3 4 1 2\n" + "4 1 2 3\n" + "4 3 2 1\n" + "1 4 3 2\n" + "1 3 2 4\n" + "3 2 1 4\n" + "3 4 1 2\n" + "3 2 4 1\n" + "1 4 2 3\n" + "1 4 2 3";
        String test4
                = "5 4 10\n" + "0 0 0 0 3\n" + "0 0 0 0 0\n" + "1 2 0 0 0\n" + "0 0 0 0 4\n" + "0 0 0 0 0\n" + "4 4 3 1\n" + "2 3 1 4\n" + "4 1 2 3\n" + "3 4 2 1\n" + "4 3 1 2\n" + "2 4 3 1\n" + "2 1 3 4\n" + "3 4 1 2\n" + "4 1 2 3\n" + "4 3 2 1\n" + "1 4 3 2\n" + "1 3 2 4\n" + "3 2 1 4\n" + "3 4 1 2\n" + "3 2 4 1\n" + "1 4 2 3\n" + "1 4 2 3";
        String test5
                = "5 6 7\n" + "0 0 0 0 3\n" + "0 2 0 0 0\n" + "1 0 0 0 4\n" + "0 6 0 0 0\n" + "0 0 5 0 0\n" + "4 4 3 1 4 2\n" + "2 3 1 4\n" + "4 1 2 3\n" + "3 4 2 1\n" + "4 3 1 2\n" + "2 4 3 1\n" + "2 1 3 4\n" + "3 4 1 2\n" + "4 1 2 3\n" + "4 3 2 1\n" + "1 4 3 2\n" + "1 3 2 4\n" + "3 2 1 4\n" + "3 4 1 2\n" + "3 2 4 1\n" + "1 4 2 3\n" + "1 4 2 3\n" + "3 4 1 2\n" + "3 2 4 1\n" + "1 4 2 3\n" + "1 4 2 3\n" + "3 4 1 2\n" + "4 1 2 3\n" + "4 3 2 1\n" + "1 4 3 2";
        in = new BufferedReader(new StringReader(test5));
        ///// test

        st = new StringTokenizer(in.readLine(), " ");
        N = Integer.parseInt(st.nextToken()); // 격자 크기
        M = Integer.parseInt(st.nextToken()); // 상어의 수
        sharkCount = M; // 남은 상어의 수
        k = Integer.parseInt(st.nextToken()); // 냄새 유효 시간

        board = new int[N][N][2]; // 각 위치에 {냄새가 뿌려진 시각, 냄새를 뿌린 상어 번호}
        sharks = new int[M + 1][3]; // 각 상어의 {행, 열, 방향}
        priority = new int[M + 1][4][4]; // 각 상어의 우선순위

        // 격자 입력
        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(in.readLine(), " ");
            for (int c = 0; c < N; c++) {
                int sharkNo = Integer.parseInt(st.nextToken());
                // 상어가 있다면
                if (sharkNo > 0) {
                    // 냄새를 뿌린 상어 설정
                    board[r][c][1] = sharkNo;
                    // 냄새를 뿌린 시각 설정
                    board[r][c][0] = 1;
                    // 상어 위치 설정
                    sharks[sharkNo][0] = r;
                    sharks[sharkNo][1] = c;
                }
            }
        }

        // 상어 현재 방향 입력
        st = new StringTokenizer(in.readLine(), " ");
        for (int sharkNo = 1; sharkNo <= M; sharkNo++) {
            sharks[sharkNo][2] = Integer.parseInt(st.nextToken()) - 1;
        }

        // 상어 방향 우선순위 입력
        for (int sharkNo = 1; sharkNo <= M; sharkNo++) { // 상어별 반복
            for (int d = 0; d < 4; d++) { // 방향별 반복
                st = new StringTokenizer(in.readLine(), " ");
                for (int i = 0; i < 4; i++) { // 우선순위별 반복
                    priority[sharkNo][d][i] = Integer.parseInt(st.nextToken()) - 1;
                }
            }
        }

        int time; // +1 인 2초부터 시작
        int[][] moveInfo = new int[M + 1][3];
        for (time = 2; time <= 1001; time++) { // 1001초까지 반복

            for (int sharkNo = 1; sharkNo <= M; sharkNo++) { // 상어번호 오름차순
                if (sharks[sharkNo][0] == -1) {
                    continue;
                }

                // sharkNo 상어가 이동할 위치를 찾는다.
                moveInfo[sharkNo] = getMoveInfo(sharkNo, time);
            }

            // 모든 상어가 이동할 위치를 다 찾았다면 상어들이 움직인다.
            moveAllShark(time, moveInfo);

            // 상어가 한마리 남았다면 종료
            if (sharkCount == 1) {
                break;
            }
        }

        System.out.println(time == 1002 ? -1 : time - 1);
    }

    // 상어 한 마리가 이동할 위치, 방향을 찾는다.
    public static int[] getMoveInfo(int sharkNo, int time) {
        int r = sharks[sharkNo][0], c = sharks[sharkNo][1], d = sharks[sharkNo][2];
        int nd, nr, nc;

        // 현재 방향의 우선순위별 확인
        for (int i = 0; i < 4; i++) {
            nd = priority[sharkNo][d][i];
            nr = r + drdc[nd][0];
            nc = c + drdc[nd][1];
            if (isValid(nr, nc)) {
                // (nr, nc) 가 냄새가 없는 칸이어서 이동 가능하면
                if (board[nr][nc][0] == 0 || time > board[nr][nc][0] + k) {
                    return new int[]{nr, nc, nd};
                }
            }
        }

        // 이동 가능한 칸을 못찾았다면 자신의 냄새가 있는 방향을 찾는다.
        for (int i = 0; i < 4; i++) {
            nd = priority[sharkNo][d][i];
            nr = r + drdc[nd][0];
            nc = c + drdc[nd][1];
            if (isValid(nr, nc)) {
                // (nr, nc) 가 자신의 냄새가 있는 칸이면
                if (board[nr][nc][1] == sharkNo) {
                    return new int[]{nr, nc, nd};
                }
            }
        }

        return new int[]{}; // 여기까지 오는 경우는 없음
    }

    // 상어들이 움직이고, 냄새를 뿌린다.
    public static void moveAllShark(int time, int[][] moveInfo) {
        // 번호가 작은 상어부터 이동
        for (int sharkNo = 1; sharkNo <= M; sharkNo++) {
            if (sharks[sharkNo][0] == -1) {
                continue;
            }

            int r = moveInfo[sharkNo][0], c = moveInfo[sharkNo][1], d = moveInfo[sharkNo][2];

            // 이미 이 위치로 이번에 이동한 작은 번호의 상어가 있다면
            if (board[r][c][0] == time) {
                sharks[sharkNo][0] = -1;
                sharkCount--;
                continue;
            }

            // sharkNo 상어가 이동하고, 냄새를 뿌린다.
            board[r][c][0] = time;
            board[r][c][1] = sharkNo;
            sharks[sharkNo][0] = r;
            sharks[sharkNo][1] = c;
            sharks[sharkNo][2] = d;
        }
    }

    // (r,c) 위치의 유효 여부 반환
    public static boolean isValid(int r, int c) {
        if (r < 0 || r >= N || c < 0 || c >= N) {
            return false;
        }
        return true;
    }

}
