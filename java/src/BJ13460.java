import java.io.*;
import java.util.*;

public class BJ13460 {
    public static int N, M;
    public static int[][] drdc = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // 상하좌우
    public static char[][] board;

    public static void main(String[] args) throws IOException {
        // [성공]
        // 빨간 구슬만 구멍에

        // [실패]
        // 파란 구슬이 구멍에, 빨간 구슬과 파란 구슬이 동시에 구멍에

        // 도착 지점만을 보는 것이 아닌 가는 도중에도 계속 구멍이 있는지 확인해야함
        // 빨간 구슬이 구멍에 빠졌더라도 파란 구슬은 끝까지 이동해서 구멍에 빠졌는지 여부를 확인해야함

        // 최소 몇 번만에 빼낼 수 있는지?
        // 10번 초과이면 -1

        // 값 받을때 R, B -> '.' 으로 바꿔주기!!

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        ////// test
        String test = "10 10\n" + "##########\n" + "#.BR.....#\n" + "#.#####..#\n" + "#.#...#..#\n" + "#.#.#..O.#\n" + "#.#.#....#\n" + "#.#....#.#\n" + "#.#..#...#\n" + "#.#......#\n" + "##########";
        in = new BufferedReader(new StringReader(test));
        ////// test

        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new char[N][M];
        int[] balls = new int[4];
        for (int r = 0; r < N; r++) {
            board[r] = in.readLine().toCharArray();
            for (int c = 0; c < M; c++) {
                if (board[r][c] == 'R') { // 빨간 구슬이면
                    balls[0] = r;
                    balls[1] = c;
                    board[r][c] = '.';
                } else if (board[r][c] == 'B') { // 파란 구슬이면
                    balls[2] = r;
                    balls[3] = c;
                    board[r][c] = '.';
                }
            }
        }

        System.out.println(setMoveDir(balls));
    }

    // 이번에 기울일 방향을 정하고 구슬들을 움직인다.
    public static int setMoveDir(int[] balls) {
        boolean[][][][] visited = new boolean[N][M][N][M];
        Queue<int[]> queue = new LinkedList<>();

        visited[balls[0]][balls[1]][balls[2]][balls[3]] = true;
        queue.offer(new int[] {balls[0], balls[1], balls[2], balls[3], 0});

        while (!queue.isEmpty()) {
            int[] now = queue.poll();

            if (now[4] == 10) {
                return -1;
            }

            for (int d = 0; d < 4; d++) { // 네 방향으로 기울인다.
                int[] next = new int[] {now[0], now[1], now[2], now[3], now[4] + 1};
                int[] order = getOrder(d, next);
                boolean[] isFall = move(d, order, next);

                // 이미 확인한 위치이거나 파란 구슬이 구멍에 빠졌다면
                if (visited[next[0]][next[1]][next[2]][next[3]] || isFall[1]) {
                    continue;
                } else if (isFall[0]) { // 빨간 구슬만 구멍에 빠졌다면
                    return now[4] + 1;
                }

                visited[next[0]][next[1]][next[2]][next[3]] = true;
                queue.offer(next);
            }
        }

        return -1;
    }

    // 먼저 움직일 구슬을 구한다.
    public static int[] getOrder(int dir, int[] balls) {
        int[] order = new int[2]; // 구슬 2개 중 순서 (0,1이면 빨간구슬 먼저, 1,0이면 파란구슬 먼저)

        if (dir == 0) { // 상
            if (balls[0] < balls[2]) { // 빨간구슬이 더 위에 위치함
                order[1] = 1; // 빨간구슬, 파란구슬 순서
            } else { // 빨간구슬이 더 아래에 위치함
                order[0] = 1; // 파란구슬, 빨간구슬 순서
            }
        } else if (dir == 1) { // 하
            if (balls[0] > balls[2]) { // 빨간구슬이 더 아래에 위치함
                order[1] = 1; // 빨간구슬, 파란구슬 순서
            } else { // 빨간구슬이 더 위에 위치함
                order[0] = 1; // 파란구슬, 빨간구슬 순서
            }
        } else if (dir == 2) { // 좌
            if (balls[1] < balls[3]) { // 빨간구슬이 더 왼쪽에 위치함
                order[1] = 1; // 빨간구슬, 파란구슬 순서
            } else { // 빨간구슬이 더 오른쪽에 위치함
                order[0] = 1; // 파란구슬, 빨간구슬 순서
            }
        } else { // 우
            if (balls[1] > balls[3]) { // 빨간구슬이 더 오른쪽에 위치함
                order[1] = 1; // 빨간구슬, 파란구슬 순서
            } else { // 빨간구슬이 더 아래에 위치함
                order[0] = 1; // 파란구슬, 빨간구슬 순서
            }
        }

        return order;
    }

    // 구슬들이 움직인다.
    // 반환 값: {빨간 구슬이 구멍에 빠졌는지 여부, 파란 구슬이 구멍에 빠졌는지 여부}
    public static boolean[] move(int dir, int[] order, int[] balls) {
        boolean[] isFall = new boolean[2];

        for (int ball : order) {
            int nr = balls[ball * 2], nc = balls[ball * 2 + 1];

            // 구슬이 이동할 수 있을 동안 계속 이동
            while (board[nr][nc] == '.' && (balls[(1 - ball) * 2] != nr || balls[(1 - ball) * 2 + 1] != nc)) {
                nr += drdc[dir][0];
                nc += drdc[dir][1];
            }

            if (board[nr][nc] == 'O') { // 이번 구슬이 구멍에 도착했으면
                isFall[ball] = true;
                balls[ball * 2] = nr;
                balls[ball * 2 + 1] = nc;
            } else { // 이번 구슬이 벽에 도착했거나 다른 구슬을 만났다면
                balls[ball * 2] = nr - drdc[dir][0];
                balls[ball * 2 + 1] = nc - drdc[dir][1];
            }
        }

        return isFall;
    }

}
