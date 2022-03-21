import java.io.*;
import java.util.*;

public class BJ23290 {
    public static final int SIZE = 4; // 격자 크기
    public static int M, maxFishCount, minOrder;
    public static int shark[], smell[][], fishes[][][];


    // 상어의 이동 (↑, ←, ↓, →)
    public static int[][] drdc = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
    // 물고기의 이동 (←, ↖, ↑, ↗, →, ↘, ↓, ↙)
    public static int[] dr = {0, -1, -1, -1, 0, 1, 1, 1}, dc = {-1, -1, 0, 1, 1, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        ////// test
        String test
                = "10 25\n" + "1 1 1\n" + "1 1 2\n" + "1 1 3\n" + "1 1 4\n" + "1 1 5\n" + "1 1 6\n" + "1 1 7\n" + "1 1 8\n" + "2 1 1\n" + "2 1 1\n" + "2 1";
        in = new BufferedReader(new StringReader(test));
        ////// test

        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        M = Integer.parseInt(st.nextToken()); // 물고기의 수
        int S = Integer.parseInt(st.nextToken()); // 마법 연습 횟수

        shark = new int[2]; // 상어의 {행, 열}
        smell = new int[SIZE][SIZE]; // 각 위치의 물고기의 냄새 남은 유효 시간
        fishes = new int[SIZE][SIZE][8]; // 위치별, 방향별로 물고기들의 수

        for (int m = 0; m < M; m++) {
            st = new StringTokenizer(in.readLine(), " ");
            int x = Integer.parseInt(st.nextToken()) - 1; // 행 위치
            int y = Integer.parseInt(st.nextToken()) - 1; // 열 위치
            int d = Integer.parseInt(st.nextToken()) - 1; // 방향
            fishes[x][y][d]++;
        }

        st = new StringTokenizer(in.readLine(), " ");
        shark[0] = Integer.parseInt(st.nextToken()) - 1;
        shark[1] = Integer.parseInt(st.nextToken()) - 1;

        for (int s = 0; s < S; s++) { // 마법 연습 횟수만큼 반복
            List<int[]> movedFishes = moveAllFish(); // 물고기 이동
            moveShark(); // 상어 이동
            removeSmell(); // 물고기 냄새 제거
            addFishes(movedFishes);
        }

        System.out.println(M); // 남아있는 물고기의 수 출력
    }

    // 모든 물고기가 이동한다.
    public static List<int[]> moveAllFish() {
        List<int[]> originFishes = new LinkedList<>(); // 원래 물고기 목록 {행, 열, 방향, 물고기 수}
        List<int[]> moveFishes = new LinkedList<>(); // 움직인 물고기 목록 {행, 열, 방향, 물고기 수}

        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++) {
                for (int d = 0; d < 8; d++) {
                    int count = fishes[r][c][d];

                    if (count == 0) {
                        continue;
                    }

                    // 각 물고기가 각자 방향으로 이동(8방향)
                    originFishes.add(new int[]{r, c, d, count});
                    moveFishes.add(getNewPosition(r, c, d, count));
                    M += count; // 물고기 수 증가

                    fishes[r][c][d] = 0;
                }
            }
        }

        for (int[] fish : moveFishes) {
            fishes[fish[0]][fish[1]][fish[2]] += fish[3];
        }

        return originFishes;
    }

    // 물고기 한마리가 이동한다.
    public static int[] getNewPosition(int r, int c, int d, int count) {
        int nr = r + dr[d], nc = c + dc[d], nd = d, i = 0;

        for (; i < 8; i++) { // 8방향
            // 이동할 수 없는 방향이면 이동할 수 있는 방향일 때까지 반시계 방향 45도 회전해서 한 칸 이동
            if (nr < 0 || nr >= SIZE || nc < 0 || nc >= SIZE || smell[nr][nc] > 0 || (nr == shark[0] && nc == shark[1])) {
                nd = (nd + 7) % 8;
                nr = r + dr[nd];
                nc = c + dc[nd];
            } else { // 이동할 수 있는 방향(물고기 냄새 X, 상어 X, 격자 범위 밖)이라면 한 칸 이동
                break;
            }
        }

        if (i == 8) { // 이동하지 못함
            nr = r;
            nc = c;
            nd = d;
        }

        return new int[]{nr, nc, nd, count};
    }

    // 원래 물고기들을 추가
    public static void addFishes(List<int[]> originFishes) {
        for (int[] fish : originFishes) {
            fishes[fish[0]][fish[1]][fish[2]] += fish[3];
        }
    }

    // 상어가 이동한다. (연속 3칸, 4방향, 상하좌우)
    public static void moveShark() {
        // 3칸 모두 이동해야 함 (중간에 격자 범위 밖으로 가면 안됨)
        maxFishCount = 0;
        minOrder = Integer.MAX_VALUE;

        moveSharkOnce(shark[0], shark[1], 0, 0, 0, smell, fishes);

        M -= maxFishCount; // 물고기의 수 감소
    }

    // 상어가 한번 이동한다.
    public static void moveSharkOnce(int r, int c, int moveCount, int fishCount, int order, int[][] nowSmell, int[][][] nowFishes) {
        if (moveCount == 3) { // 3번 모두 이동을 완료하면
            // 가능한 이동 방법 중 제외되는 물고기 많은 순, 사전 순으로 앞선 순으로 이동
            if (maxFishCount < fishCount || (maxFishCount == fishCount && minOrder > order)) {
                shark[0] = r;
                shark[1] = c;
                maxFishCount = fishCount;
                minOrder = order;

                smell = nowSmell;
                fishes = nowFishes;
            }
            return;
        }

        for (int d = 0; d < 4; d++) { // 상하좌우 중 이동
            int nr = r + drdc[d][0], nc = c + drdc[d][1];

            if (nr >= 0 && nr < SIZE && nc >= 0 && nc < SIZE) {
                int[][][] copiedFishes = getCopiedFishes(nowFishes);
                int[][] copiedSmell = getCopiedSmell(nowSmell);

                // 이동 중 물고기가 있는 칸을 만나면 그 칸의 모든 물고기는 격자에서 제외 후 냄새 남김
                int nowFishCount = 0;
                for (int i = 0; i < 8; i++) {
                    if (copiedFishes[nr][nc][i] >= 1) {
                        nowFishCount += copiedFishes[nr][nc][i];
                        copiedFishes[nr][nc][i] = 0;
                        copiedSmell[nr][nc] = 3;
                    }
                }

                moveSharkOnce(nr, nc, moveCount + 1, fishCount + nowFishCount, order * 10 + d, copiedSmell, copiedFishes);
            }
        }
    }

    public static int[][] getCopiedSmell(int[][] origin) {
        int[][] copied = new int[SIZE][SIZE];

        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++) {
                copied[r][c] = origin[r][c];
            }
        }

        return copied;
    }

    public static int[][][] getCopiedFishes(int[][][] origin) {
        int[][][] copied = new int[SIZE][SIZE][8];

        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++) {
                for (int d = 0; d < 8; d++) {
                    copied[r][c][d] = origin[r][c][d];
                }
            }
        }

        return copied;
    }

    // 물고기 냄새 유효기간을 1씩 빼준다.
    public static void removeSmell() {
        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++) {
                if (smell[r][c] == 0) {
                    continue;
                }
                smell[r][c]--;
            }
        }
    }
}