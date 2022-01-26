// 140min 12512KB 344ms

import java.io.*;

public class BJ20055 {
    public static void main(String[] args) throws IOException {
        // A[i] : i번 칸의 내구도
        // 벨트 1번 칸 ~ 2N번 칸
        // 1번 칸 : 로봇을 올리는 위치, N번 칸 : 로봇이 내리는 위치
        // 로봇을 올리거나 로봇이 이동하면 내구도 -1

        // 로봇 이동 과정
        // 1. 벨트 한칸 회전 (모든 칸이 시계방향으로 한칸 이동)
        // 2. 먼저 올라간 순으로 시계방향으로 한 칸 이동 (이동하려는 칸이 비어있고 내구도가 1 이상일때)
        // 3. 올리는 위치에 로봇을 올린다 (그 위치 내구도가 1 이상이면)
        // 4. 내구도가 0인 칸 개수 >= K 이면 과정종료

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        //////
        String test1 = "3 2\n" + "1 2 1 2 1 2";
        String test2 = "3 6\n" + "10 10 10 10 10 10";
        String test3 = "4 5\n" + "10 1 10 6 3 4 8 2";
        String test4 = "5 8\n" + "100 99 60 80 30 20 10 89 99 100";
        in = new BufferedReader(new StringReader(test4));
        //////

        String[] tokens = in.readLine().split(" ");
        int N = Integer.parseInt(tokens[0]);
        int K = Integer.parseInt(tokens[1]);

        tokens = in.readLine().split(" ");
        int[] A = new int[N * 2]; // 내구도
        for (int i = 0; i < N * 2; i++) {
            A[i] = Integer.parseInt(tokens[i]);
        }

        int step = 0; // 현재 단계
        int on = 0, off = N - 1; // 올리는 위치, 내리는 위치
        int zeroCount = 0; // 내구도가 0인 칸의 수
        boolean[] isOnRobot = new boolean[N * 2]; // 로봇들이 위치해있는지 여부

        while (zeroCount < K) { // 내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료
            step++;

            // 벨트가 회전한다.
            on = (on + (N * 2) - 1) % (N * 2);
            off = (off + (N * 2) - 1) % (N * 2);

            // 회전한 뒤 내리는 위치에 도착한 로봇은 내린다
            isOnRobot[off] = false;

            // 로봇들이 먼저 올라간 순으로 시계방향으로 한 칸 이동
            // 반시계방향 순 = 먼저 올라간 순
            int now = off, next;
            while (now != on) {
                now = (now + (N * 2) - 1) % (N * 2);
                if (!isOnRobot[now]) {
                    continue;
                }

                next = (now + 1) % (N * 2);

                // 이동하려는 칸이 비어있고 내구도가 1 이상일때만 이동가능
                if (!isOnRobot[next] && A[next] >= 1) {
                    isOnRobot[now] = false;
                    if (--A[next] == 0) {
                        zeroCount++;
                    }

                    if (next != off) { // 다음에 갈 곳이 내리는 위치가 아니면
                        isOnRobot[next] = true;
                    }
                }
            }

            // 올리는 위치에 로봇을 올린다
            if (A[on] >= 1) {
                isOnRobot[on] = true;
                if (--A[on] == 0) {
                    zeroCount++;
                }
            }
        }

        System.out.println(step);
    }
}
