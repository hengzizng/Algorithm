import java.io.*;
import java.util.*;

public class BJ17837 {
    public static int N, K;
    public static int[][] board, locations, drdc = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}}; // →, ←, ↑, ↓
    public static List<Integer>[][] tokens;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        ////// test
        String test1 = "4 4\n" + "0 0 2 0\n" + "0 0 1 0\n" + "0 0 1 2\n" + "0 2 0 0\n" + "2 1 1\n" + "3 2 3\n" + "2 2 1\n" + "4 1 2";
        String test4 = "6 10\n" + "0 1 2 0 1 1\n" + "1 2 0 1 1 0\n" + "2 1 0 1 1 0\n" + "1 0 1 1 0 2\n" + "2 0 1 2 0 1\n" + "0 2 1 0 2 1\n" + "1 1 1\n" + "2 2 2\n" + "3 3 4\n" + "4 4 1\n" + "5 5 3\n" + "6 6 2\n" + "1 6 3\n" + "6 1 2\n" + "2 4 3\n" + "4 2 1";
        in = new BufferedReader(new StringReader(test4));
        ////// test

        // 1 -> K 순서대로 말 이동
        // 한 말이 이동할 때 위에 올려진 말도 함께 이동
        // 진행 중 말이 4개 이상 쌓이는 순간 게임 종료

        // 이동하려는 곳에 따른 작업
        // 흰색: 이동가능 (새로 이동한 말들이 원래 있던 말들 위로 쌓임)
        // 빨간색: 이동가능 (이동할 말들의 순서를 뒤집어서 원래 있던 말들 위로 쌓임)
        // 파란색 or 체스판 밖: 이동하려는 말 하나의 방향을 반대로 하고 한 칸 이동
        //   -> 그래도 파란색 or 체스판 밖이면 방향만 바뀐채로 이동하지 않음

        st = new StringTokenizer(in.readLine(), " ");
        N = Integer.parseInt(st.nextToken()); // 체스판의 크기
        K = Integer.parseInt(st.nextToken()); // 말의 개수
        board = new int[N][N]; // 체스판 정보 (각 칸의 색 - 0: 흰색, 1: 빨간색, 2: 파란색)
        locations = new int[K][4]; // 각 말들의 [행, 열, 위치한 높이, 방향]
        tokens = new ArrayList[N][N]; // 각 위치별로 말 리스트

        int r, c, d, k;
        for (r = 0; r < N; r++) {
            st = new StringTokenizer(in.readLine(), " ");
            for (c = 0; c < N; c++) {
                board[r][c] = Integer.parseInt(st.nextToken());
                tokens[r][c] = new ArrayList<>();
            }
        }

        for (k = 0; k < K; k++) {
            st = new StringTokenizer(in.readLine(), " ");
            r = Integer.parseInt(st.nextToken()) - 1; // 행
            c = Integer.parseInt(st.nextToken()) - 1; // 열
            d = Integer.parseInt(st.nextToken()) - 1; // 이동 방향

            locations[k][0] = r;
            locations[k][1] = c;
            locations[k][3] = d;

            tokens[r][c].add(k);
        }

        int turn = 1;
        for (; turn <= 1000; turn++) {
            if (!moveAll()) {
                break;
            }
        }

        System.out.println(turn == 1001 ? -1 : turn);
    }

    public static boolean moveAll() {
        for (int tokenNo = 0; tokenNo < K; tokenNo++) {
            if (!moveOne(tokenNo, 0)) {
                return false;
            }
        }
        return true;
    }

    // 말 하나가 이동 (게임이 종료되면 false 반환)
    public static boolean moveOne(int tokenNo, int count) {
        int r = locations[tokenNo][0], c = locations[tokenNo][1];
        int h = locations[tokenNo][2];
        int d = locations[tokenNo][3];

        // 이동할 위치
        int nr = r + drdc[d][0], nc = c + drdc[d][1];

        // 이동할 위치가 벽이거나 파란색이라면
        if (nr < 0 || nr >= N || nc < 0 || nc >= N || board[nr][nc] == 2) {
            if (count == 0) { // 첫 번째 이동일 때의 이동 불가능이라면 방향을 변경해서 다시 이동한다.
                locations[tokenNo][3] = d ^ 1;
                return moveOne(tokenNo, count + 1);
            } else { // 두 번째 이동일 때의 이동 불가능이라면 이동하지 않고 다음 순서로 넘어간다.
                return true;
            }
        }

        List<Integer> moving = new ArrayList<>(); // 이동할 말들의 번호

        int i = h, top = tokens[r][c].size();
        if (board[nr][nc] == 0) { // 이동할 위치가 흰색이라면
            // 이동할 말의 위에 있는 모든 말들이 이동 (현재 말부터 가장 위의 말까지 이동)
            while (i < top) {
                moving.add(tokens[r][c].get(h));
                tokens[r][c].remove(h);
                i++;
            }
        } else if (board[nr][nc] == 1) { // 이동할 위치가 빨간색이라면
            // 이동할 말의 위에 있는 모든 말들이 이동 (가장 위의 말부터 현재 말까지 이동)
            i = top - 1;
            while (i >= h) {
                moving.add(tokens[r][c].get(i));
                tokens[r][c].remove(i);
                i--;
            }
        }

        for (int nowTokenNo : moving) {
            locations[nowTokenNo][0] = nr;
            locations[nowTokenNo][1] = nc;
            locations[nowTokenNo][2] = tokens[nr][nc].size();
            tokens[nr][nc].add(nowTokenNo);

            if (tokens[nr][nc].size() >= 4) {
                return false;
            }
        }

        return true;
    }
}
