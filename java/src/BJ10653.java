import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ10653 {
    public static int N, K;
    public static int[][] checkPoints;

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        /////// test
        String test = "5 2\n" + "0 0\n" + "8 3\n" + "1 1\n" + "10 -5\n" + "2 2";
        in = new BufferedReader(new StringReader(test));
        /////// test

        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        N = Integer.parseInt(st.nextToken()); // 체크포인트 수
        K = Integer.parseInt(st.nextToken()); // 건너뛸 체크포인트 수
        checkPoints = new int[N][2]; // 체크포인트의 위치
        for (int n = 0; n < N; n++) {
            st = new StringTokenizer(in.readLine(), " ");
            checkPoints[n][0] = Integer.parseInt(st.nextToken());
            checkPoints[n][1] = Integer.parseInt(st.nextToken());
        }

        // distanceSum[i][j]: i개의 체크포인트를 건너뛰었을 때 체크포인트 j까지의 최소거리 (체크포인트 j는 방문)
        int[][] distanceSum = new int[K + 1][N];
        // 체크포인트를 하나도 건너뛰지 않았을 때의 거리
        for (int point = 1; point < N; point++) {
            distanceSum[0][point] = distanceSum[0][point - 1] + getDistance(point - 1, point);
        }
        // 체크포인트를 한 개 이상 건너뛰었을 때의 거리
        for (int passCount = 1; passCount <= K; passCount++) {
            for (int point = 1; point < N; point++) {
                // 0 ~ point 까지 passCount개 건너뛰었을 떄의 최솟값은 아래 값들 중 최솟값!!
                // (0 ~ point-1 까지 passCount개 건너뛰었을 때의 최솟값) + (point-1 <-> point 거리)
                // (0 ~ point-2 까지 passCount-1개 건너뛰었을 때의 최솟값) + (point-2 <-> point 거리)
                // ...

                distanceSum[passCount][point] = distanceSum[passCount][point - 1] + getDistance(point - 1, point);
                for (int i = 2; i < N; i++) {
                    if (passCount - i + 1 < 0 || point - i < 0) {
                        break;
                    }
                    distanceSum[passCount][point] = Math.min(distanceSum[passCount][point], distanceSum[passCount - i + 1][point - i] + getDistance(point - i, point));
                }
            }
        }

        System.out.println(distanceSum[K][N - 1]);
    }

    public static int getDistance(int i, int j) {
        return Math.abs(checkPoints[i][0] - checkPoints[j][0]) + Math.abs(checkPoints[i][1] - checkPoints[j][1]);
    }

}
