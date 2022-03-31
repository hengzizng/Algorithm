import java.io.*;
import java.util.*;

public class BJ12100 {
    public static int[][] drdc = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // 상하좌우 방향벡터
    public static int N, maxBlock;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        ////// test
        String test = "3\n" + "2 2 2\n" + "4 4 4\n" + "8 8 8";
        in = new BufferedReader(new StringReader(test));
        ////// test

        N = Integer.parseInt(in.readLine());
        int[][] board = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(in.readLine(), " ");
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        setDirection(0, board);

        System.out.println(maxBlock);
    }

    // 이번에 이동할 방향을 정한다.
    public static void setDirection(int count, int[][] board) {
        if (count == 5) {
            return;
        }

        setDirection(count + 1, upOrDown(1, 0, board));
        setDirection(count + 1, upOrDown(0, N - 1, board));
        setDirection(count + 1, leftOrRight(3, 0, board));
        setDirection(count + 1, leftOrRight(2, N - 1, board));
    }

    // 블록들을 위(type=1) 또는 아래(type=0) 로 이동시킨다.
    public static int[][] upOrDown(int type, int startR, int[][] board) {
        int[][] newBoard = new int[N][N];
        Deque<Integer> numbers = new LinkedList<>();
        boolean isMix = false;

        for (int c = 0; c < N; c++) {
            int r = startR;

            while (r >= 0 && r < N) {
                if (board[r][c] > 0) {
                    if (!isMix && !numbers.isEmpty() && numbers.peekLast() == board[r][c]) {
                        numbers.offer(numbers.pollLast() * 2);
                        isMix = true;
                    } else {
                        numbers.offer(board[r][c]);
                        isMix = false;
                    }
                }

                r += drdc[type][0];
            }

            r = startR;
            while (!numbers.isEmpty()) {
                newBoard[r][c] = numbers.pollFirst();
                maxBlock = Math.max(maxBlock, newBoard[r][c]);
                r += drdc[type][0];
            }
        }

        return newBoard;
    }

    // 블록들을 왼쪽(type=3) 또는 오른쪽(type=2) 으로 이동시킨다.
    public static int[][] leftOrRight(int type, int startC, int[][] board) {
        int[][] newBoard = new int[N][N];
        Deque<Integer> numbers = new LinkedList<>();
        boolean isMix = false;

        for (int r = 0; r < N; r++) {
            int c = startC;

            while (c >= 0 && c < N) {
                if (board[r][c] > 0) {
                    if (!isMix && !numbers.isEmpty() && numbers.peekLast() == board[r][c]) {
                        numbers.offer(numbers.pollLast() * 2);
                        isMix = true;
                    } else {
                        numbers.offer(board[r][c]);
                        isMix = false;
                    }
                }

                c += drdc[type][1];
            }

            c = startC;
            while (!numbers.isEmpty()) {
                newBoard[r][c] = numbers.pollFirst();
                maxBlock = Math.max(maxBlock, newBoard[r][c]);
                c += drdc[type][1];
            }
        }

        return newBoard;
    }
}
