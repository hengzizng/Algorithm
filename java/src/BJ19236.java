import java.io.*;
import java.util.StringTokenizer;

public class BJ19236 {
    // 공간의 가로, 세로 크기
    public static final int SIZE = 4;
    // 상어가 먹을 수 있는 물고기 번호의 합의 최댓값
    public static int maxSum;
    // 방향 벡터 (↑, ↖, ←, ↙, ↓, ↘, →, ↗)
    public static int[] dr = {-1, -1, 0, 1, 1, 1, 0, -1}, dc = {0, -1, -1, -1, 0, 1, 1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        ////// test
        String test = "2 6 10 8 6 7 9 4\n" + "1 7 16 6 4 2 5 8\n" + "3 7 8 6 7 6 14 8\n" + "12 7 15 4 11 3 13 3";
        in = new BufferedReader(new StringReader(test));
        ////// test

        int[][] board = new int[SIZE][SIZE]; // 각 위치별 물고기 번호 (물고기 없으면 0)
        int[][] fishes = new int[SIZE * SIZE][3]; // 물고기 번호별 위치, 방향 (물고기 없으면 -1)
        for (int fishNo = 0; fishNo < SIZE * SIZE; fishNo++) {
            fishes[fishNo][0] = -1;
        }

        for (int r = 0; r < SIZE; r++) {
            st = new StringTokenizer(in.readLine());
            for (int c = 0; c < SIZE; c++) {
                int fishNo = Integer.parseInt(st.nextToken()) - 1;
                int fishDirection = Integer.parseInt(st.nextToken()) - 1;

                board[r][c] = fishNo;
                fishes[fishNo][0] = r;
                fishes[fishNo][1] = c;
                fishes[fishNo][2] = fishDirection;
            }
        }

        // 상어 (0,0)에 들어감
        int r = 0, c = 0;
        int fishNo = board[r][c];
        board[r][c] = -1;
        fishes[fishNo][0] = -1;

        // 물고기 이동 -> 상어 이동 -> 물고기 이동 ...
        moveAll(r, c, fishes[fishNo][2], fishNo + 1, board, fishes);

        // 상어가 먹을 수 있는 물고기 번호 합의 최댓값
        System.out.println(maxSum);
    }

    public static void moveAll(int r, int c, int d, int eatSum, int[][] board, int[][] fishes) {
        // 물고기가 이동
        moveFish(r, c, board, fishes);

        int nr, nc, nd, fishNo;
        for (int i = 1; i < SIZE; i++) {
            // 상어의 이동: 방향에 있는 모든 칸으로 이동 가능 (한 번에 여러 칸 이동 가능)
            nr = r + (dr[d] * i);
            nc = c + (dc[d] * i);
            // 이동 가능하고 물고기가 있는 칸으로만 이동 가능
            if (isValid(nr, nc) && board[nr][nc] >= 0) {
                int[][] newBoard = getCopied(board);
                int[][] newFishes = getCopied(fishes);

                // 이동해서 물고기를 먹음
                fishNo = newBoard[nr][nc];
                nd = newFishes[fishNo][2];
                newBoard[nr][nc] = -1;
                newFishes[fishNo][0] = -1;

                // 다음 위치 탐색
                moveAll(nr, nc, nd, eatSum + (fishNo + 1), newBoard, newFishes);
            }
        }

        // 매번 최댓값 갱신
        maxSum = Math.max(maxSum, eatSum);
    }

    // 물고기의 이동
    public static void moveFish(int sharkR, int sharkC, int[][] board, int[][] fishes) {
        int r, c, d, nr = -1, nc = -1, nd, target;
        for (int fishNo = 0; fishNo < SIZE * SIZE; fishNo++) { // 물고기 번호 오름차순으로 확인
            if (fishes[fishNo][0] == -1) { // 물고기 번호 fishNo인 물고기가 없다면
                continue;
            }

            // 이번 물고기의 원래 위치, 방향 정보
            r = fishes[fishNo][0];
            c = fishes[fishNo][1];
            d = fishes[fishNo][2];

            nd = d;
            for (int i = 0; i < 8; i++) {
                nr = r + dr[nd];
                nc = c + dc[nd];

                // 이동 가능한 방향이 없다면 반시계 방향으로 45도 회전
                if (!isValid(nr, nc) || (nr == sharkR && nc == sharkC)) {
                    nd = (nd + 1) % 8;
                    continue;
                }

                // 이동 가능한 방향이 있다면 (빈 칸, 다른 물고기가 있는 칸)
                target = board[nr][nc]; // 위치를 교환할 물고기

                // 물고기 이동 (서로 위치 교환)
                fishes[fishNo][0] = nr;
                fishes[fishNo][1] = nc;
                fishes[fishNo][2] = nd;
                if (target >= 0) {
                    fishes[target][0] = r;
                    fishes[target][1] = c;
                }

                board[nr][nc] = fishNo;
                board[r][c] = target;
                break;
            }
        }
    }

    public static int[][] getCopied(int[][] target) {
        int rowLen = target.length, colLen = target[0].length;
        int[][] copied = new int[rowLen][colLen];

        for (int r = 0; r < rowLen; r++) {
            for (int c = 0; c < colLen; c++) {
                copied[r][c] = target[r][c];
            }
        }

        return copied;
    }

    // 공간 안에 있는지 여부 반환
    public static boolean isValid(int r, int c) {
        if (r < 0 || r >= SIZE || c < 0 || c >= SIZE) {
            return false;
        }
        return true;
    }
}
