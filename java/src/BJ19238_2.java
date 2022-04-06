// 90 min

import java.io.*;
import java.util.*;

public class BJ19238_2 {
    public static int N, M, map[][], destinations[][];
    public static int[][] drdc = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public static void main(String[] args) throws IOException {
        // 태울 승객: 현재 택시에서 최단거리가 가장 짧은, 가장 위, 가장 왼쪽
        // 택시가 한 칸 움직일 때마다 연료 -1
        // 승객을 목적지로 이동시키면 승객의 (출발지 -> 도착지) 거리 * 2 만큼 연료 충전
        // 이동 도중 연료가 바닥나면 종료

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

//        ////// test
//        String test
//                = "2 1 5\n" + "0 1\n" + "1 0\n" + "1 1\n" + "1 1 2 2";
//        in = new BufferedReader(new StringReader(test));
//        ////// test

        int[] taxi = new int[3]; // 택시의 {행, 열, 남은 연료}
        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        N = Integer.parseInt(st.nextToken()); // 영역의 크기
        M = Integer.parseInt(st.nextToken()); // 승객의 수

        taxi[2] = Integer.parseInt(st.nextToken()); // 초기 연료
        map = new int[N][N]; // 영역 (0: 빈 칸, 1: 벽)
        destinations = new int[M + 2][2]; // 각 승객의 목적지

        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(in.readLine(), " ");
            for (int c = 0; c < N; c++) {
                map[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(in.readLine(), " ");
        taxi[0] = Integer.parseInt(st.nextToken()) - 1; // 택시의 행 위치
        taxi[1] = Integer.parseInt(st.nextToken()) - 1; // 택시의 열 위치

        for (int m = 2; m < M + 2; m++) { // 손님 고유 번호
            st = new StringTokenizer(in.readLine(), " ");

            int departR = Integer.parseInt(st.nextToken()) - 1; // 손님의 출발지 행 위치
            int departC = Integer.parseInt(st.nextToken()) - 1; // 손님의 출발지 열 위치
            int destR = Integer.parseInt(st.nextToken()) - 1; // 손님의 출발지 행 위치
            int destC = Integer.parseInt(st.nextToken()) - 1; // 손님의 출발지 열 위치

            // 각 손님은 모두 다른 위치에서 출발하기 때문에 map에 저장 가능
            map[departR][departC] = m; // 2, 3, 4, ...
            // 한 승객과 다른 승객의 목적지가 같을 수도 있기 때문에 목적지는 따로 저장
            destinations[m][0] = destR;
            destinations[m][1] = destC;
        }

        for (int m = 0; m < M; m++) { // 고객 수만큼 반복
            int passengerNo = pickUp(taxi);
            if (passengerNo == -1) {
                taxi[2] = -1;
                break;
            }

            dropOff(passengerNo, taxi);
            if (taxi[2] == -1) {
                break;
            }
        }

        System.out.println(taxi[2]);
    }

    // 태울 승객을 찾아서 새로운 택시 정보와 승객 번호를 반환 (승객 번호가 -1이면 종료)
    public static int pickUp(int[] taxi) {
        // 태울 승객: 현재 택시에서 최단거리가 가장 짧은, 가장 위, 가장 왼쪽
        // 태울 승객 정보 {행, 열, 거리, 승객 번호}
        int[] target = {N, N, N * N, 0};

        Queue<int[]> queue = new LinkedList<>();
        boolean[][] isVisit = new boolean[N][N];

        queue.offer(new int[]{taxi[0], taxi[1], 0});
        isVisit[taxi[0]][taxi[1]] = true;

        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            // 이번 위치에 승객이 있다면
            int no = map[now[0]][now[1]];
            if (no >= 2) {
                // 이미 찾은 승객과 비교
                // 이번 승객과의 거리가 더 짧거나
                // 거리가 같은데 이번 승객이 더 위에 있거나
                // 행까지 같은데 이번 승객이 더 왼쪽에 있으면
                if (now[2] < target[2] || (now[2] == target[2] && (now[0] < target[0] || (now[0] == target[0] && now[1] < target[1])))) {
                    target[0] = now[0];
                    target[1] = now[1];
                    target[2] = now[2];
                    target[3] = no;
                }
            }

            for (int i = 0; i < 4; i++) {
                int nr = now[0] + drdc[i][0], nc = now[1] + drdc[i][1];
                if (isValid(nr, nc) && !isVisit[nr][nc] && map[nr][nc] != 1 && now[2] + 1 <= taxi[2] && now[2] + 1 <= target[2]) {
                    queue.offer(new int[]{nr, nc, now[2] + 1});
                    isVisit[nr][nc] = true;
                }
            }
        }

        if (target[3] == 0) { // 승객을 태우지 못했다면 -1 반환
            taxi[2] = -1;
            return -1;
        } else { // 승객을 태웠다면 승객 번호 반환
            // 택시 정보 재설정
            taxi[0] = target[0]; // 행
            taxi[1] = target[1]; // 열
            taxi[2] -= target[2]; // 연료
            map[target[0]][target[1]] = 0; // 태운 승객을 map에서 없애준다.
            return target[3];
        }
    }

    // 승객을 태우고 목적지까지 이동 후의 새로운 택시 정보를 반환 (taxi[2] 가 -1이면 종료)
    public static void dropOff(int passengerNo, int[] taxi) {
        int destR = destinations[passengerNo][0], destC = destinations[passengerNo][1];

        Queue<int[]> queue = new LinkedList<>();
        boolean[][] isVisit = new boolean[N][N];

        queue.offer(new int[]{taxi[0], taxi[1], 0});
        isVisit[taxi[0]][taxi[1]] = true;

        while (!queue.isEmpty()) {
            int[] now = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nr = now[0] + drdc[i][0], nc = now[1] + drdc[i][1];

                if (!isValid(nr, nc) || isVisit[nr][nc] || map[nr][nc] == 1 || now[2] + 1 > taxi[2]) {
                    continue;
                }

                // 목적지에 도착하면
                if (nr == destR && nc == destC) {
                    taxi[0] = nr; // 행
                    taxi[1] = nc; // 열
                    taxi[2] = taxi[2] - (now[2] + 1) + (now[2] + 1) * 2; // 연료

                    return;
                }

                queue.offer(new int[]{nr, nc, now[2] + 1});
                isVisit[nr][nc] = true;
            }

        }

        // while문 안에서 반환되지 않았으면 목적지까지 도달 실패
        taxi[2] = -1;
        return;
    }

    public static boolean isValid(int r, int c) {
        if (r < 0 || r >= N || c < 0 || c >= N) {
            return false;
        } else {
            return true;
        }
    }
}
