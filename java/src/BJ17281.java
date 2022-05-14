import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ17281 {
    public static final int PLAYER_COUNT = 9;
    public static int N, outCount, orderIndex, maxScore;
    public static int[] base;
    public static int[][] results;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        /////// test
        String test1 = "2\n" + "4 3 2 1 0 4 3 2 1\n" + "1 2 3 4 1 2 3 4 0";
        String test2
                = "9\n" + "1 2 4 3 0 2 1 0 3\n" + "1 2 1 2 0 0 0 0 1\n" + "3 4 2 3 1 2 3 4 0\n" + "0 1 2 3 4 2 1 0 0\n" + "0 0 0 0 0 0 1 4 4\n" + "0 4 0 4 0 4 0 4 0\n" + "0 4 2 2 2 2 2 2 2\n" + "1 1 1 1 1 1 1 1 0\n" + "0 2 0 3 0 1 0 2 0";
        in = new BufferedReader(new StringReader(test2));
        /////// test

        N = Integer.parseInt(in.readLine()); // 이닝 수
        results = new int[N][PLAYER_COUNT]; // 각 선수가 각 이닝에서 얻는 결과
        base = new int[3]; // 1루 ~ 3루에 선수의 존재 여부(있으면 1, 없으면 0)

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(in.readLine(), " ");
            for (int j = 0; j < PLAYER_COUNT; j++) {
                results[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[] orders = new int[PLAYER_COUNT]; // orders[타순] = 선수 번호
        boolean[] isSelected = new boolean[PLAYER_COUNT]; // 선수의 타순이 배정되었는지 여부
        orders[3] = 0; // 4번 타자(4번째 순서)는 1번 선수
        isSelected[0] = true;
        setOrder(0, orders, isSelected);

        System.out.println(maxScore);
    }

    // 선수들의 타순을 정한다.
    public static void setOrder(int count, int[] orders, boolean[] isSelected) {
        if (count == PLAYER_COUNT) {
            // 타순을 다 정했으면 게임을 진행
            play(orders);
            return;
        }

        // 4번째 순서는 이미 선수가 정해져있다.
        if (count == 3) {
            setOrder(count + 1, orders, isSelected);
        } else {
            for (int player = 1; player < PLAYER_COUNT; player++) {
                if (!isSelected[player]) {
                    orders[count] = player;
                    isSelected[player] = true;
                    setOrder(count + 1, orders, isSelected);
                    isSelected[player] = false;
                }
            }
        }
    }

    // 게임을 진행하고, 최대 점수를 set
    public static void play(int[] orders) {
        int score = 0; // 이번 게임에서 얻은 점수
        orderIndex = 0; // 현재 공을 칠 선수를 구하기 위한 값

        // 이닝별로 반복
        for (int inning = 0; inning < N; inning++) {
            Arrays.fill(base, 0);
            outCount = 0; // 이번 이닝에서 아웃 수

            while (outCount < 3) {
                int player = orders[orderIndex];
                score += getScore(results[inning][player], base);
                orderIndex = (orderIndex + 1) % PLAYER_COUNT;
            }
        }

        maxScore = Math.max(maxScore, score);
    }

    // base의 상태와 이번 결과에 따라 얻는 점수를 반환한다.
    public static int getScore(int result, int[] base) {
        int score = 0;

        if (result == 0) {
            outCount++;
            return score;
        }

        for (int i = 2; i >= 0; i--) {
            if (i + result > 2) {
                score += base[i];
            } else {
                base[i + result] = base[i];
            }
            base[i] = 0;
        }

        // 현재 타자가 홈런이면 점수 증가, 아니라면 베이스로 이동
        if (result == 4) {
            score += 1;
        } else {
            base[result - 1] = 1;
        }

        return score;
    }
}
