import java.io.*;
import java.util.*;

public class BJ20058 {
    public static int N;
    public static int[][] A, spareA;
    public static int[][] drdc = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        ////// test
        String test = "3 10\n" +
                "1 0 3 4 5 6 7 0\n" +
                "8 0 6 5 4 3 2 1\n" +
                "1 2 0 4 5 6 7 0\n" +
                "8 7 6 5 4 3 2 1\n" +
                "1 2 3 4 0 6 7 0\n" +
                "8 7 0 5 4 3 2 1\n" +
                "1 2 3 4 5 6 7 0\n" +
                "0 7 0 5 4 3 2 1\n" +
                "1 2 3 1 2 3 1 2 3 1\n";
        in = new BufferedReader(new StringReader(test));
        ////// test

        String[] input = in.readLine().split(" ");
        N = 1 << Integer.parseInt(input[0]); // 얼음판의 한 변의 길이
        int Q = Integer.parseInt(input[1]); // 단계(실행 횟수)
        A = new int[N][N]; // 얼음판의 각 위치별 얼음 양

        for (int r = 0; r < A.length; r++) {
            input = in.readLine().split(" ");
            for (int c = 0; c < A.length; c++) {
                A[r][c] = Integer.parseInt(input[c]);
            }
        }

        input = in.readLine().split(" ");
        for (int q = 0; q < Q; q++) {
            int L = Integer.parseInt(input[q]); // 2^L: 각 실행 단계의 부분 격자 크기

            // 모든 부분 격자들이 시계 방향으로 90도 회전
            spareA = new int[N][N]; // 회전을 위해 두는 여분의 행렬
            divide(1 << L, N, 0, 0);
            A = spareA;

            // 회전이 끝나면 얼음이 있는 인접한 칸이 3개 미만일 때 1씩 줄여준다.
            List<int[]> decreaseList = new LinkedList<>();
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    if (A[r][c] == 0) {
                        continue;
                    }

                    int validCount = 0, nr = r, nc = c;

                    for (int i = 0; i < 4; i++) {
                        nr = r + drdc[i][0];
                        nc = c + drdc[i][1];
                        if (isValid(nr, nc) && A[nr][nc] > 0) {
                            validCount++;
                        }
                    }

                    if (validCount < 3) {
                        decreaseList.add(new int[]{r, c});
                    }
                }
            }

            for (int[] now : decreaseList) {
                --A[now[0]][now[1]];
            }
        }

        int maxSize = 0, totalSum = 0; // 가장 큰 얼음 덩어리 크기, 얼음의 합
        boolean[][] check = new boolean[N][N]; // 방문 체크
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (A[r][c] == 0 || check[r][c]) {
                    continue;
                }

                int[] nowInfo = findIce(r, c, check, A);
                maxSize = Math.max(maxSize, nowInfo[0]);
                totalSum += nowInfo[1];
            }
        }

//        totalSum = 0;
//        for (int r = 0; r < N; r++) {
//            for (int c = 0; c < N; c++) {
//                System.out.print(A[r][c] + " ");
//                totalSum += A[r][c];
//            }
//            System.out.println();
//        }

        // 남아있는 얼음의 합 출력
        System.out.println(totalSum);
        // 가장 큰 덩어리가 차지하는 칸의 개수 출력
        System.out.println(maxSize);
    }

    // 행렬을 부분 행렬로 나눈다
    public static void divide(int targetSize, int size, int startR, int startC) {
        if (size == targetSize) {
            rotate(startR, startC, size);
            return;
        }

        size /= 2;
        divide(targetSize, size, startR, startC);
        divide(targetSize, size, startR + size, startC);
        divide(targetSize, size, startR, startC + size);
        divide(targetSize, size, startR + size, startC + size);
    }

    // 각 부분 격자가 시계 방향으로 90도 회전
    public static void rotate(int startR, int startC, int size) {
        for (int r = 0; r < size; r++) {
            for (int c = 0; c < size; c++) {
                spareA[startR + c][startC + size - 1 - r] = A[startR + r][startC + c];
            }
        }
    }

    // bfs로 얼음 덩어리를 찾는다.
    public static int[] findIce(int r, int c, boolean[][] check, int[][] A) {
        Queue<int[]> queue = new LinkedList<>();
        int iceCount = 0, iceSum = 0; // 이번 얼음 덩어리의 크기, 얼음들의 합

        queue.offer(new int[]{r, c});
        check[r][c] = true;

        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            iceCount++;
            iceSum += A[now[0]][now[1]];

            for (int i = 0; i < 4; i++) {
                int nr = now[0] + drdc[i][0];
                int nc = now[1] + drdc[i][1];

                if (!isValid(nr, nc) || check[nr][nc] || A[nr][nc] == 0) {
                    continue;
                }

                queue.offer(new int[]{nr, nc});
                check[nr][nc] = true;
            }
        }

        return new int[]{iceCount, iceSum};
    }


    public static boolean isValid(int r, int c) {
        if (r >= 0 && r < N && c >= 0 && c < N) {
            return true;
        }
        return false;
    }
}
