import java.io.*;
import java.util.*;

public class BJ16235 {
    public static int[] dr = {-1, -1, -1, 0, 0, 1, 1, 1}, dc = {-1, 0, 1, -1, 1, -1, 0, 1};
    public static int N;

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        ////// test
        String test = "10 10 1000\n" + "100 1 1 1 1 1 1 1 1 1\n" + "1 1 1 1 1 1 1 1 1 1\n" + "1 1 1 1 1 1 1 1 1 1\n" + "1 1 1 1 1 1 1 1 1 1\n" + "1 1 1 1 1 1 1 1 1 1\n" + "1 1 1 1 1 1 1 1 1 1\n" + "1 1 1 1 1 1 1 1 1 1\n" + "1 1 1 1 1 1 1 1 1 1\n" + "1 1 1 1 1 1 1 1 1 1\n" + "1 1 1 1 1 1 1 1 1 1\n" + "1 1 1\n" + "2 2 1\n" + "3 3 1\n" + "4 4 1\n" + "5 5 1\n" + "6 6 1\n" + "7 7 1\n" + "8 8 1\n" + "9 9 1\n" + "10 10 1";
        in = new BufferedReader(new StringReader(test));
        ////// test

        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        N = Integer.parseInt(st.nextToken()); // 땅의 크기
        int M = Integer.parseInt(st.nextToken()); // 처음에 주어지는 나무의 수
        int K = Integer.parseInt(st.nextToken()); // K년 후 살아남은 나무의 수를 출력

        int[][] A = new int[N][N]; // 겨울마다 각 칸에 추가할 양분
        int[][] land = new int[N][N]; // 각 칸에 남아있는 양분
        Queue<int[]> dead = new LinkedList<>(); // 죽은 나무들 [{행, 열, 양분으로 바뀔 값}]
        LinkedList<int[]> trees = new LinkedList<>(); // 나무들 [{행, 열, 나이}]

        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(in.readLine(), " ");
            for (int c = 0; c < N; c++) {
                A[r][c] = Integer.parseInt(st.nextToken());
                land[r][c] = 5; // 가장 처음에 양분은 모든 칸에 5만큼 들어있다.
            }
        }

        int x, y, z;
        for (int m = 0; m < M; m++) {
            st = new StringTokenizer(in.readLine(), " ");
            x = Integer.parseInt(st.nextToken()) - 1; // 행
            y = Integer.parseInt(st.nextToken()) - 1; // 열
            z = Integer.parseInt(st.nextToken()); // 나이
            trees.addLast(new int[]{x, y, z});
        }
        Collections.sort(trees, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[2] - o2[2]; // 나이 오름차순 정렬
            }
        });

        for (int k = 0; k < K; k++) {
            spring(land, dead, trees);
            summerWinter(land, A, dead);
            fall(trees);
        }

        System.out.println(trees.size());
    }

    public static void spring(int[][] land, Queue<int[]> dead, LinkedList<int[]> trees) {
        int count = trees.size();
        int r, c, age, tree[];

        for (int i = 0; i < count; i++) { // 나무들 수대로 반복
            tree = trees.removeFirst();
            r = tree[0];
            c = tree[1];
            age = tree[2];

            if (age > land[r][c]) { // 땅에 양분이 부족
                dead.offer(new int[]{r, c, age / 2});
            } else { // 양분을 먹음
                land[r][c] -= age;
                trees.addLast(new int[]{r, c, age + 1});
            }
        }
    }

    public static void fall(LinkedList<int[]> trees) {
        List<int[]> breeding = new LinkedList<>(); // 번식할 나무들
        int r, c;

        // 번식할 나무를 찾는다.
        for (int[] tree : trees) {
            if (tree[2] % 5 == 0) {
                breeding.add(tree);
            }
        }

        // 번식
        for (int[] tree : breeding) {
            for (int i = 0; i < 8; i++) {
                r = tree[0] + dr[i];
                c = tree[1] + dc[i];
                if (r >= 0 && r < N && c >= 0 && c < N) {
                    trees.addFirst(new int[]{r, c, 1});
                }
            }
        }
    }

    public static void summerWinter(int[][] land, int[][] A, Queue<int[]> dead) {
        while (!dead.isEmpty()) {
            int[] deadTree = dead.poll();
            land[deadTree[0]][deadTree[1]] += deadTree[2];
        }

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                land[r][c] += A[r][c];
            }
        }
    }
}