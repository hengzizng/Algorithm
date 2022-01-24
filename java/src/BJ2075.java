import java.io.*;
import java.util.*;

// 317212 KB, 828 ms

public class BJ2075 {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(in.readLine());

        long[][] numbers = new long[N][N];
        for (int i = 0; i < N; i++) {
            String[] numbersInARow = in.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                numbers[i][j] = Long.parseLong(numbersInARow[j]);
            }
        }

        // numbers[0]: 숫자, numbers[1]: 열 인덱스, numbers[2]: 행 인덱스
        Queue<long[]> pq = new PriorityQueue<long[]>(new Comparator<long[]>() {
            @Override
            public int compare(long[] o1, long[] o2) {
                return o1[0] > o2[0] ? -1 : 1;
            }
        });
        for (int i = 0; i < N; i++) {
            pq.add(new long[]{numbers[N - 1][i], i, N - 1});
        }

        long answer = 0;
        for (int i = 0; i < N; i++) {
            long[] now = pq.poll();
            answer = now[0];

            int col = (int) now[1];
            int row = (int) now[2];
            if (row > 0) {
                pq.add(new long[]{numbers[row - 1][col], col, row - 1});
            }
        }

        System.out.println(answer);
    }
}
