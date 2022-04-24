import java.io.*;
import java.util.StringTokenizer;

public class SWEA4014 {
    public static int N, X;

    public static void main(String[] args) throws Exception {
        ////// test
        System.setIn(new FileInputStream("testcase/4014input.txt"));
        ////// test

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int T = Integer.parseInt(in.readLine()); // 테스트케이스 수
        for (int t = 1; t <= T; t++) {
            st = new StringTokenizer(in.readLine(), " ");
            N = Integer.parseInt(st.nextToken()); // 지도 한 변 크기
            X = Integer.parseInt(st.nextToken()); // 경사로의 길이
            int[][] mapByRow = new int[N][N]; // 지형 정보
            int[][] mapByCol = new int[N][N]; // 지형 정보

            for (int r = 0; r < N; r++) {
                st = new StringTokenizer(in.readLine(), " ");
                for (int c = 0; c < N; c++) {
                    mapByRow[r][c] = Integer.parseInt(st.nextToken());
                    mapByCol[c][r] = mapByRow[r][c];
                }
            }

            int installCount = 0;

            for (int i = 0; i < N; i++) {
                if (check(mapByRow[i])) { // i번째 행 체크
                    installCount++;
                }
                if (check(mapByCol[i])) { // i번째 열 체크
                    installCount++;
                }
            }

            sb.append("#").append(t).append(" ").append(installCount).append("\n");
        }

        System.out.println(sb.toString());
    }

    public static boolean check(int[] target) {
        // sameLen: 같은 높이가 지속되는 길이 (경사로 설치한 곳 제외)
        // 각 열, 각 행별로 0 ~ N-1 순으로 확인
        // 이전 높이와 달라진다면
        //   높이차가 2 이상이면 바로 해당 행/열은 활주로 설치 불가
        //   road[i - 1] - road[i] 가 1이라면 내리막 경사로 설치 (지금이 더 낮음)
        //   -> i ~ i+X-1 가 모두 같은 높이인지 확인 / i = i+X-1, sameLen = 0
        //   road[i - 1] - road[i] 가 -1이라면 오르막 경사로 설치 (지금이 더 높음)
        //   -> sameLen < X 이면 활주로 설치 불가 / sameLen = 1
        int sameLen = 1, i = 0;

        while (++i < N) {
            int diff = target[i - 1] - target[i];

            if (Math.abs(diff) >= 2) {
                return false;
            }

            if (diff == 1) {
                for (int j = 1; j < X; j++) {
                    if (i + j == N || target[i] != target[i + j]) {
                        return false;
                    }
                }

                i = i + X - 1;
                sameLen = 0;
            } else if (diff == -1) {
                if (sameLen < X) {
                    return false;
                }

                sameLen = 1;
            } else { // 이전과 높이가 같다면
                sameLen++;
            }
        }

        return true;
    }
}
