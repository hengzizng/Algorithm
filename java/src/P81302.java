import java.util.LinkedList;
import java.util.Queue;


public class P81302 {
    public static final int SIZE = 5;
    public static int[][] drdc = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public static void main(String[] args) {
        String[][] places = new String[][]{{"POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"},
                {"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"},
                {"PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"},
                {"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"},
                {"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"}};

        solution(places);
    }

    public static int[] solution(String[][] places) {
        int[] answer = new int[places.length];

        for (int i = 0; i < places.length; i++) {
            answer[i] = checkAll(places[i]);
        }

        return answer;
    }

    // 각 장소별로 거리두기를 지키고 있는지 확인
    public static int checkAll(String[] place) {
        // 모든 위치 확인
        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++) {
                // 사람을 만나면 주변 확인
                if (place[r].charAt(c) == 'P') {
                    // 거리두기를 지키지 않았다면 다른 사람 확인하지 않고 바로 결과 반환
                    if (check(r, c, place) == 0) {
                        return 0;
                    }
                }
            }
        }
        // 모든 사람을 확인했지만 결과가 반환되지 않았다면, 모두 거리두기를 지키고 있다.
        return 1;
    }

    // 한 명의 사람에 대해 거리두기를 지키고 있는지 확인
    public static int check(int r, int c, String[] place) {
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[SIZE][SIZE];

        queue.offer(new int[]{r, c, 0});
        visited[r][c] = true;

        while (!queue.isEmpty()) {
            // now: {행 위치, 열 위치, 시작점으로부터의 거리}
            int[] now = queue.poll();

            for (int d = 0; d < 4; d++) {
                int nr = drdc[d][0] + now[0];
                int nc = drdc[d][1] + now[1];

                if (now[2] == 2 || nr < 0 || nr >= SIZE || nc < 0 || nc >= SIZE || visited[nr][nc]) {
                    continue;
                }

                // 거리 2 이내에 다른 사람이 있다면
                if (place[nr].charAt(nc) == 'P') {
                    return 0;
                }
                // 파티션을 만났다면
                if (place[nr].charAt(nc) == 'X') {
                    continue;
                }

                queue.offer(new int[]{nr, nc, now[2] + 1});
                visited[nr][nc] = true;
            }
        }

        return 1;
    }
}
