import java.io.*;
import java.util.*;

public class BJ15683 {
    public static int N, M, totalZeroCount, minZeroCount = Integer.MAX_VALUE;
    public static int[][][] dr = {
            {{-1}, {0}, {1}, {0}},
            {{-1, 1}, {0, 0}},
            {{-1, 0}, {0, 1}, {1, 0}, {0, -1}},
            {{-1, 0, 1}, {0, 1, 0}, {1, 0, -1}, {0, -1, 0}},
            {{-1, 0, 1, 0}}
    },
            dc = {
                    {{0}, {1}, {0}, {-1}},
                    {{0, 0}, {-1, 1}},
                    {{0, 1}, {1, 0}, {0, -1}, {-1, 0}},
                    {{0, 1, 0}, {1, 0, -1}, {0, -1, 0}, {-1, 0, 1}},
                    {{0, 1, 0, -1}}
            };
    public static List<int[]> cctvList;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        N = Integer.parseInt(st.nextToken()); // 행 수
        M = Integer.parseInt(st.nextToken()); // 열 수
        int[][] office = new int[N][M]; // 사무실 상태
        cctvList = new ArrayList<>();
        for (int n = 0; n < N; n++) {
            st = new StringTokenizer(in.readLine(), " ");
            for (int m = 0; m < M; m++) {
                office[n][m] = Integer.parseInt(st.nextToken());
                if (office[n][m] == 0) { // 빈 칸
                    totalZeroCount++;
                } else if (office[n][m] <= 5) { // CCTV
                    cctvList.add(new int[]{n, m});
                }
            }
        }

        setCctvDirection(0, totalZeroCount, office);

        System.out.println(minZeroCount);
    }

    // 각 CCTV별로 감시할 방향을 정한다.
    public static void setCctvDirection(int cctvNo, int zeroCount, int[][] office) {
        if (cctvNo == cctvList.size()) {
            minZeroCount = Math.min(minZeroCount, zeroCount);
            return;
        }

        int[] cctv = cctvList.get(cctvNo); // cctv 위치 {행, 열}
        int cctvType = office[cctv[0]][cctv[1]] - 1; // cctv 유형 (1~5) - 1

        for (int i = 0; i < dr[cctvType].length; i++) { // 이번 cctv가 세팅될 수 있는 방향의 수
            // 이번 cctv 방향을 i로 선택하고, 선택된 방향에 따른 감시할 수 있는 곳을 표시
            int[][] newOffice = getCopiedOffice(office);
            int checkedCount = check(cctvType, i, cctv, newOffice);
            setCctvDirection(cctvNo + 1, zeroCount - checkedCount, newOffice);
        }
    }

    public static int[][] getCopiedOffice(int[][] office) {
        int[][] copiedOffice = new int[N][M];

        for (int n = 0; n < N; n++) {
            for (int m = 0; m < M; m++) {
                copiedOffice[n][m] = office[n][m];
            }
        }

        return copiedOffice;
    }

    // cctv와 그 방향에 따라 감시할 수 있는 곳을 표시하고 그 개수를 반환
    public static int check(int cctvType, int direction, int[] cctv, int[][] office) {
        int watchCount = 0; // 이번 cctv로 새로 감시할 수 있는 위치의 수
        int nr, nc;

        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < dr[cctvType][direction].length; i++) { // CCTV가 direction 방향일 때 감시할 수 있는 모든 방향
            queue.offer(new int[]{cctv[0], cctv[1], i}); // 행, 열, 탐색을 진행할 방향
        }

        while (!queue.isEmpty()) {
            cctv = queue.poll(); // {행, 열, 탐색을 진행할 방향}

            nr = cctv[0] + dr[cctvType][direction][cctv[2]];
            nc = cctv[1] + dc[cctvType][direction][cctv[2]];
            if (!isValid(nr, nc) || office[nr][nc] == 6) {
                continue;
            }

            if (office[nr][nc] == 0) {
                watchCount++;
                office[nr][nc] = cctvType + 1;
            }
            queue.offer(new int[]{nr, nc, cctv[2]}); // 행, 열, bfs를 진행할 방향
        }

        return watchCount;
    }


    public static boolean isValid(int r, int c) {
        if (r < 0 || r >= N || c < 0 || c >= M) {
            return false;
        } else {
            return true;
        }
    }
}