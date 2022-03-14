import java.io.*;

public class BJ15684 {
    public static int N, M, H;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        ///// test
        String test = "5 8 6\n" + "1 1\n" + "2 2\n" + "3 3\n" + "4 4\n" + "3 1\n" + "4 2\n" + "5 3\n" + "6 4";
        in = new BufferedReader(new StringReader(test));
        ///// test

        String[] input = in.readLine().split(" ");
        N = Integer.parseInt(input[0]); // 열 수
        M = Integer.parseInt(input[1]); // 가로선(연결된 선)의 개수
        H = Integer.parseInt(input[2]); // 행 수

        int a, b;
        boolean[][] bridge = new boolean[H][N]; // 가로선 연결 여부
        for (int m = 0; m < M; m++) {
            input = in.readLine().split(" ");
            a = Integer.parseInt(input[0]) - 1; // a행
            b = Integer.parseInt(input[1]) - 1; // b열과 b+1열을 연결
            bridge[a][b] = true; // 가로선 연결
        }

        // 추가할 사다리의 개수를 0~3개까지 늘려가며 확인
        int bridgeCount = 0;
        for (; bridgeCount <= 3; bridgeCount++) {
            // bridgeCount만큼 추가해서 조건이 만족되는 경우가 있다면 바로 종료
            if (setBridge(bridgeCount, 0, 0, bridge)) {
                break;
            }
        }

        System.out.println(bridgeCount == 4 ? -1 : bridgeCount);
    }

    // 조합으로 targetCount만큼 연결선을 추가
    public static boolean setBridge(int targetCount, int count, int index, boolean[][] bridge) {
        if (count == targetCount) {
            return isValid(bridge);
        }

        for (int i = index; i < H * N; i++) {
            int r = i / N, c = i % N;

            // 이번 위치에 사다리를 놓을 수 없다.
            if (c == N - 1 || bridge[r][c] || (c > 0 && bridge[r][c - 1])) {
                continue;
            }

            // 이번 위치에 사다리를 놓는다.
            bridge[r][c] = true;
            // 이번 위치에 사다리를 두었을 때 조건이 만족하는 경우를 발견했다면 종료
            if (setBridge(targetCount, count + 1, i + 1, bridge)) {
                return true;
            }
            bridge[r][c] = false;
        }

        return false;
    }


    // 모든 i번 세로선의 결과가 i번이 나오는지 확인
    public static boolean isValid(boolean[][] bridge) {
        for (int i = 0; i < N; i++) { // 각 열마다 사다리를 탄다.
            int r = 0, c = i;

            while (r < H) {
                if (c > 0 && bridge[r][c - 1]) { // 왼쪽으로 연결됨
                    c--;
                } else if (bridge[r][c]) { // 오른쪽으로 연결됨
                    c++;
                }
                r++;
            }

            if (c != i) { // i번 세로선의 결과가 i번이 아니라면 더 이상 다른 열 확인할 필요 X
                return false;
            }
        }

        return true;
    }
}