import java.io.*;
import java.util.*;

// 오른쪽 아래 -> 왼쪽 위 까지 오른쪽에서 왼쪽으로 확인한다면
// 이 학생의 자리를 바로바로 갱신해줄 수 있다.
// 맨 왼쪽 위까지 다 확인헀으면 classroom에 실제로 학생 번호 배치

// 1. 인접한 칸에 좋아하는 학생이 많은 자리
// 2. 인접한 칸에 빈 칸이 많은 자리
// 3. 가장 위쪽, 가장 왼쪽

// 자리 배치가 모두 끝나면 만족도 계산
// 각 학생별로 satisfactionMap[인접한 좋아하는 학생 수]
public class BJ21608 {
    public static int N, classroom[][], drdc[][] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    public static int[] satisfactionMap = {0, 1, 10, 100, 1000}; // 인접한 좋아하는 학생 수에 따른 만족도
    public static Set<Integer>[] preferences; // 각 학생별로 선호하는 학생 집합

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

//        ///// test
//        String test = "3\n" + "4 2 5 1 7\n" + "3 1 9 4 5\n" + "9 8 1 2 3\n" + "8 1 9 3 4\n" + "7 2 3 4 8\n" + "1 9 2 5 7\n" + "6 5 2 3 4\n" + "5 1 9 2 8\n" + "2 9 3 1 4";
//        in = new BufferedReader(new StringReader(test));
//        ///// test

        N = Integer.parseInt(in.readLine()); // 교실의 가로/세로 크기
        classroom = new int[N][N]; // 학생 배치도
        preferences = new HashSet[N * N + 1]; // 각 학생별로 선호하는 학생 집합

        for (int i = 0; i < N * N; i++) {
            StringTokenizer st = new StringTokenizer(in.readLine(), " ");

            int studentNo = Integer.parseInt(st.nextToken());
            preferences[studentNo] = new HashSet();
            for (int j = 0; j < 4; j++) {
                preferences[studentNo].add(Integer.parseInt(st.nextToken()));
            }

            // 이번 학생의 자리를 구한다.
            setStudent(studentNo, preferences[studentNo]);
        }

        // 모든 학생들의 만족도의 합을 구한다.
        int totalSatisfaction = 0;
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                totalSatisfaction += getSatisfaction(r, c, preferences[classroom[r][c]]);
            }
        }

        System.out.println(totalSatisfaction);
    }

    // 한 학생의 만족도를 반환
    public static int  getSatisfaction(int r, int c, Set<Integer> preference) {
        int preferenceCount = 0;

        for (int i = 0; i < 4; i++) {
            int nr = r + drdc[i][0], nc = c + drdc[i][1];

            if (nr < 0 || nr >= N || nc < 0 || nc >= N || classroom[nc][nc] == 0) {
                continue;
            }

            if (preference.contains(classroom[nr][nc])) {
                preferenceCount++;
            }
        }

        return satisfactionMap[preferenceCount];
    }

    // 한 학생의 자리를 구해서 배치
    public static void setStudent(int studentNo, Set<Integer> preference) {
        int[] seat = new int[4]; // {인접한 선호하는 학생 수, 인접한 빈 칸 수, 자리의 행, 자리의 열}

        for (int r = N - 1; r >= 0; r--) { // 행
            for (int c = N - 1; c >= 0; c--) { // 열
                if (classroom[r][c] > 0) { // 이미 자리가 있는 곳이라면
                    continue;
                }

                int preferenceCount = 0, blankCount = 0;

                for (int i = 0; i < 4; i++) { // 인접한 방향
                    int nr = r + drdc[i][0], nc = c + drdc[i][1];

                    if (nr < 0 || nr >= N || nc < 0 || nc >= N) {
                        continue;
                    }

                    int adjNo = classroom[nr][nc];
                    if (adjNo == 0) { // 인접한 칸이 빈칸이라면
                        blankCount++;
                    } else if (preference.contains(adjNo)) { // 인접한 칸에 좋아하는 학생이 있다면
                        preferenceCount++;
                    }
                }

                // 이미 구해둔 자리가 인접한 선호하는 학생 수가 더 많다면
                if (preferenceCount < seat[0]) {
                    continue;
                }

                // 현재 위치가 인접한 선호하는 학생 수가 더 많거나, 인접한 빈 칸이 더 많거나 같다면
                if (preferenceCount > seat[0] || (preferenceCount == seat[0] && blankCount >= seat[1])) {
                    seat[0] = preferenceCount;
                    seat[1] = blankCount;
                    seat[2] = r;
                    seat[3] = c;
                }
            }
        }

        classroom[seat[2]][seat[3]] = studentNo;
    }
}
