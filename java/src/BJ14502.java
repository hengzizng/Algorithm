import java.io.*;
import java.util.*;

public class BJ14502 {
    public static int N, M, totalBlankCount, maxBlankCount;
    public static int[][] drdc = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    public static List<Integer> viruses;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        ////// test
        String test = "8 8\n" + "2 0 0 0 0 0 0 2\n" + "2 0 0 0 0 0 0 2\n" + "2 0 0 0 0 0 0 2\n" + "2 0 0 0 0 0 0 2\n" + "2 0 0 0 0 0 0 2\n" + "0 0 0 0 0 0 0 0\n" + "0 0 0 0 0 0 0 0\n" + "0 0 0 0 0 0 0 0";
        in = new BufferedReader(new StringReader(test));
        ////// test

        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        N = Integer.parseInt(st.nextToken()); // 행 수
        M = Integer.parseInt(st.nextToken()); // 열 수

        int[][] map = new int[N][M]; // 지도 상태
        viruses = new LinkedList<>(); // 바이러스들의 위치값
        totalBlankCount = -3; // 벽을 세우고 바이러스가 퍼지지 않았을 때 안전 영역의 수
        for (int n = 0; n < N; n++) {
            st = new StringTokenizer(in.readLine(), " ");
            for (int m = 0; m < M; m++) {
                map[n][m] = Integer.parseInt(st.nextToken());
                if (map[n][m] == 0) {
                    totalBlankCount++;
                } else if (map[n][m] == 2) {
                    viruses.add(n * M + m);
                }
            }
        }

        makeWall(0, 0, map);
        System.out.println(maxBlankCount);
    }

    public static void makeWall(int wallCount, int position, int[][] map) {
        if (wallCount == 3) {
            spreadVirus(map);
            return;
        }

        for (int nextPosition = position; nextPosition < N * M; nextPosition++) {
            int nr = nextPosition / M;
            int nc = nextPosition % M;

            if (map[nr][nc] == 0) {
                map[nr][nc] = 1;
                makeWall(wallCount + 1, nextPosition + 1, map);
                map[nr][nc] = 0;
            }
        }
    }

    public static void spreadVirus(int[][] map) {
        int r, c, nr, nc, blankCount = totalBlankCount;
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[N][M];

        for (int virus : viruses) {
            r = virus / M;
            c = virus % M;

            queue.add(new int[]{r, c});
            visited[r][c] = true;
        }

        while (!queue.isEmpty()) {
            int[] now = queue.poll();

            for (int i = 0; i < 4; i++) {
                nr = drdc[i][0] + now[0];
                nc = drdc[i][1] + now[1];

                if (nr < 0 || nr >= N || nc < 0 || nc >= M || map[nr][nc] == 1 || visited[nr][nc]) {
                    continue;
                }

                queue.add(new int[]{nr, nc});
                visited[nr][nc] = true;
                blankCount--;
            }
        }

        maxBlankCount = Math.max(maxBlankCount, blankCount);
    }
}
