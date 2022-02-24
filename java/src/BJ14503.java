import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BJ14503 {

    public static int N, M;

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        String[] input = in.readLine().split(" ");
        N = Integer.parseInt(input[0]); // 행 수
        M = Integer.parseInt(input[1]); // 열 수

        input = in.readLine().split(" ");
        int[] robot = new int[3]; // 로봇 청소기 정보
        robot[0] = Integer.parseInt(input[0]); // 행 좌표
        robot[1] = Integer.parseInt(input[1]); // 열 좌표
        // 바라보는 방향
        if ("0".equals(input[2])) { // 북
            robot[2] = 0;
        } else if ("1".equals(input[2])) { // 동
            robot[2] = 3;
        } else if ("2".equals(input[2])) { // 남
            robot[2] = 2;
        } else { // 서
            robot[2] = 1;
        }

        int[][] map = new int[N][M]; // 지도 상태
        for (int n = 0; n < N; n++) {
            input = in.readLine().split(" ");
            for (int m = 0; m < M; m++) {
                map[n][m] = Integer.parseInt(input[m]);
            }
        }

        System.out.println(clean(robot, map));
    }

    public static int clean(int[] robot, int[][] map) {
        int[][] drdc = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}}; // 북, 서, 남, 동
        int cleanCount = 0, failCount = 0, nextDir;
        int[] nextAxis = {robot[0], robot[1]};

        while (failCount < 4) {
            // 1. 현재 위치 청소
            map[robot[0]][robot[1]] = 2;
            cleanCount++;

            // 2. 현재 방향을 기준으로 왼쪽부터 탐색
            failCount = 0;
            while (true) {
                nextDir = (robot[2] + 1) % 4;
                nextAxis[0] = robot[0] + drdc[nextDir][0];
                nextAxis[1] = robot[1] + drdc[nextDir][1];

                // 2-a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면
                if (nextAxis[0] >= 0 && nextAxis[0] < N &&
                        nextAxis[1] >= 0 && nextAxis[1] < M &&
                        map[nextAxis[0]][nextAxis[1]] == 0
                ) {
                    robot[2] = nextDir;
                    robot[0] = nextAxis[0];
                    robot[1] = nextAxis[1];
                    break;
                }

                // 2-b. 왼쪽 방향에 청소할 공간이 없다면
                robot[2] = nextDir;
                failCount++;

                // 2-c. 네 방향 모두 청소할 공간이 없다면
                if (failCount == 4) {
                    // 한칸 후진
                    nextDir = (robot[2] + 2) % 4;
                    robot[0] += drdc[nextDir][0];
                    robot[1] += drdc[nextDir][1];

                    if (robot[0] < 0 || robot[0] >= N || robot[1] < 0 || robot[1] >= M ||
                            map[robot[0]][robot[1]] == 1
                    ) { // 후진 불가능
                        break;
                    } else { // 후진 가능
                        failCount = 0;
                    }
                }
            }
        }

        return cleanCount;
    }

}
