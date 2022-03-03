import java.io.*;
import java.util.*;

public class BJ17142 {
    public static int N, M, MIN_TIME, blankCount;
    public static int[][] lab, drdc = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    public static List<int[]> virus;

    public static void main(String[] args) throws IOException {
        // 모든 바이러스는 처음에 비활성 상태
        // 활성 상태의 바이러스는 인접한 4방향의 빈 칸으로 1초동안 복제됨
        // 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성이 활성화
        // M개의 바이러스를 활성 상태로 변경
        // 모든 빈 칸이 바이러스가 되는 최소 시간 (비활성화여도 상관 X)

        // lab의 값 - 0: 빈 칸, 1: 벽, 2: 비활성화 바이러스, 3: 활성화 바이러스
        // blankCount: 빈 칸의 수
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        //////
        String test = "7 2\n" +
                "2 0 2 0 1 1 0\n" +
                "0 0 1 0 1 0 0\n" +
                "0 1 1 1 1 0 0\n" +
                "2 1 0 0 0 0 2\n" +
                "1 0 0 0 0 1 1\n" +
                "0 1 0 0 0 0 0\n" +
                "2 1 0 0 2 0 2";
        in = new BufferedReader(new StringReader(test));
        //////

        String[] input = in.readLine().split(" ");
        N = Integer.parseInt(input[0]); // 연구소 크기
        M = Integer.parseInt(input[1]); // 활성화 바이러스 수
        MIN_TIME = N * N + 1; // 연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간
        blankCount = 0; // 빈 칸의 수

        lab = new int[N][N]; // 연구소 상태
        virus = new ArrayList<>(); // 바이러스들의 위치를 저장
        for (int i = 0; i < N; i++) {
            input = in.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                lab[i][j] = Integer.parseInt(input[j]);
                if (lab[i][j] == 0) {
                    blankCount++;
                } else if (lab[i][j] == 2) {
                    virus.add(new int[]{i, j});
                }
            }
        }

        if (blankCount == 0) {
            MIN_TIME = 0;
        } else {
            active(0, 0, new int[M][2]);
        }

        MIN_TIME = MIN_TIME == N * N + 1 ? -1 : MIN_TIME;
        System.out.println(MIN_TIME);
    }

    // 활성화시킬 M개의 바이러스를 선택
    public static void active(int start, int count, int[][] selected) {
        if (count == M) {
            spread(selected);
            return;
        }

        for (int index = start; index < virus.size(); index++) {
            selected[count] = virus.get(index);
            active(index + 1, count + 1, selected);
        }
    }

    // 활성화 바이러스가 퍼진다
    public static void spread(int[][] selected) {
        int nowBlankCount = blankCount;
        int[][] nowLab = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                nowLab[i][j] = lab[i][j];
            }
        }

        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < M; i++) {
            nowLab[selected[i][0]][selected[i][1]] = 3;
            queue.offer(new int[]{selected[i][0], selected[i][1], 0});
        }

        int[] now = null;
        while (!queue.isEmpty()) {
            now = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nr = now[0] + drdc[i][0];
                int nc = now[1] + drdc[i][1];

                if (nr < 0 || nr >= N || nc < 0 || nc >= N || nowLab[nr][nc] % 2 == 1) {
                    continue;
                }

                if (nowLab[nr][nc] == 0) {
                    if (--nowBlankCount == 0) {
                        now[2]++;
                        queue.clear();
                        break;
                    }
                }
                nowLab[nr][nc] = 3;
                queue.offer(new int[]{nr, nc, now[2] + 1});
            }
        }

        if (nowBlankCount == 0) { // 빈 칸이 모두 바이러스가 됐을 때만
            MIN_TIME = Math.min(MIN_TIME, now[2]);
        }
    }
}
