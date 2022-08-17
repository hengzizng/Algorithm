import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ18430 {
    public static int N, M, maxValueSum;
    public static int[][] wood, drdc = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}}; // 상우하좌
    public static boolean[][] used;

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        ///// test
        String input1 = "3 3\n" + "32 83 75\n" + "24 96 56\n" + "71 88 12";
        String input2 = "2 3\n" + "7 5 4\n" + "3 2 9";
        in = new BufferedReader(new StringReader(input1));
        ///// test

        st = new StringTokenizer(in.readLine(), " ");
        N = Integer.parseInt(st.nextToken()); // 세로 크기 (행 수)
        M = Integer.parseInt(st.nextToken()); // 가로 크기 (열 수)
        wood = new int[N][M]; // 나무 재료의 각 칸의 강도
        used = new boolean[N][M]; // 나무 재료의 각 칸을 사용했는지 여부
        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(in.readLine(), " ");
            for (int c = 0; c < M; c++) {
                wood[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        make(0, 0);

        System.out.println(maxValueSum);
    }

    public static void make(int index, int valueSum) {
//        if (maxValueSum < valueSum) {
//            maxValueSum = valueSum;
//            System.out.println("----------> " + valueSum);
//            for (int r = 0; r < N; r++) {
//                for (int c = 0; c < M; c++) {
//                    System.out.print(used[r][c] + " ");
//                }
//                System.out.println();
//            }
//        }
        maxValueSum = Math.max(maxValueSum, valueSum);

        if (index == N * M) {
            return;
        }

        // 이번 칸 사용 X
        make(index + 1, valueSum);

        int r = index / M, c = index % M;
        if (!used[r][c]) {
            for (int d1 = 0; d1 < 4; d1++) {
                int nr1 = r + drdc[d1][0], nc1 = c + drdc[d1][1];
                if (!isValid(nr1, nc1)) {
                    continue;
                }

                int d2 = (d1 + 1) % 4;
                int nr2 = r + drdc[d2][0], nc2 = c + drdc[d2][1];
                if (!isValid(nr2, nc2)) {
                    continue;
                }

                used[r][c] = true;
                used[nr1][nc1] = true;
                used[nr2][nc2] = true;
                make(index + 1, valueSum + (wood[r][c] * 2) + wood[nr1][nc1] + wood[nr2][nc2]);
                used[r][c] = false;
                used[nr1][nc1] = false;
                used[nr2][nc2] = false;
            }
        }
    }

    public static boolean isValid(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M && !used[r][c];
    }
}
