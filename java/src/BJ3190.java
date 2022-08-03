import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class BJ3190 {
    public static int N, K, L, snakeDir;
    public static int[][] board, drdc = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}; // 우하좌상
    public static LinkedList<int[]> snake;

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        ////// test
        // 테스트케이스 주소: https://www.acmicpc.net/board/view/56469
        String test = "6\n" +
                "3\n" +
                "3 4\n" +
                "2 5\n" +
                "5 3\n" +
                "3\n" +
                "3 D\n" +
                "15 L\n" +
                "17 D";
        in = new BufferedReader(new StringReader(test));
        ////// test

        N = Integer.parseInt(in.readLine()); // 보드의 크기
        K = Integer.parseInt(in.readLine()); // 사과의 개수
        board = new int[N][N]; // 보드의 상태 (0: 빈 칸, 1: 사과, 2: 뱀)

        // 뱀 초기 설정
        board[0][0] = 2;
        snake = new LinkedList<>(); // first = head , last = tail
        snake.addLast(new int[]{0, 0});
        snakeDir = 0;

        // 사과 위치 입력
        for (int k = 0; k < K; k++) {
            st = new StringTokenizer(in.readLine(), " ");
            int r = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;
            board[r][c] = 1;
        }

        // 방향 전환 정보 입력
        L = Integer.parseInt(in.readLine()); // 뱀의 방향 변환 횟수
        int[] turnInfo = new int[10001]; // 방향 전환 정보
        for (int l = 0; l < L; l++) {
            st = new StringTokenizer(in.readLine(), " ");
            int X = Integer.parseInt(st.nextToken());
            turnInfo[X] = "D".equals(st.nextToken()) ? 1 : 3;
        }

        // 시간에 따른 뱀의 이동
        for (int time = 1; time <= 10000; time++) {
            // 뱀의 머리 이동
            if (!move()) {
                System.out.println(time);
                break;
            }

            // time 초가 끝난 뒤에 방향 회전
            snakeDir = (snakeDir + turnInfo[time]) % 4;
        }
    }

    // 뱀이 한 칸 이동한다
    // 정상적으로 이동했을 경우 true, 게임이 종료되었으면 false를 반환한다.
    public static boolean move() {
        int[] head = snake.getFirst();

        // 뱀의 머리 이동
        int nr = head[0] + drdc[snakeDir][0];
        int nc = head[1] + drdc[snakeDir][1];

        // 게임 종료 조건
        if (nr < 0 || nr >= N || nc < 0 || nc >= N || board[nr][nc] == 2) {
            return false;
        }

        // 빈 칸으로 이동했다면
        if (board[nr][nc] == 0) {
            int[] tail = snake.removeLast();
            board[tail[0]][tail[1]] = 0;
        }

        // 머리 정보 설정
        board[nr][nc] = 2;
        snake.addFirst(new int[]{nr, nc});

        return true;
    }
}
