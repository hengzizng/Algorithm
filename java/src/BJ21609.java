import java.io.*;
import java.util.*;

public class BJ21609 {
    public static int[][] drdc = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    public static int totalScore, N, M, groupInfo[], board[][];
    public static Set<Integer> blocks;

    public static void main(String[] args) throws IOException {
        // N: 격자 크기, M: 색상 수

        // -1: 검은색 블록, 0: 무지개 블록, 1~M: 일반 블록

        // 블록 그룹 (2개 이상)
        // - 일반 블록 최소 1개
        // - 일반 블록의 색은 모두 같아야 함
        // - 검은색 포함 X
        // - 무지개 블록 0~개 (상관없음)

        // 블록 그룹의 기준 블록: 일반 블록 중 가장 위, 가장 왼쪽

        // 블록 그룹이 존재하는 동안 반복
        // 크기가 가장 큰 그룹, 무지개 블록이 많은 그룹, 기준 블록이 가장 아래, 기준 블록이 가장 오른쪽
        // 찾은 그룹의 모든 블록을 제거 -> 제거개수^2 점 획득
        // 중력 작용 (검은색 블록을 제외한 모든 블록이 가능한 맨 아래로 이동)
        // 90도 반시계 방향으로 회전
        // 중력 작용

        // visited 초기화, groupSize, rainbowCount, standard, blocks
        // 블록 그룹을 찾는다.
        // 시작점: 일반 블록
        // 일반 블록에는 visited 표시 후 방문, 무지개 블록은 그냥 방문

        // 점수 획득
        // blocks 제거

        // 중력 작용

        // 회전

        // 중력 작용

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        ////// test
        String test = "4 3\n" + "1 1 1 3\n" + "3 2 3 3\n" + "1 2 -1 3\n" + "-1 -1 1 1";
        in = new BufferedReader(new StringReader(test));
        ////// test

        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(in.readLine(), " ");
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        while (true) {
            boolean[][] visited = new boolean[N][N];
            groupInfo = new int[4]; // {그룹 크기, 무지개블록 수, 기준블록 행, 기준블록 열}

            // 처리할 블록 그룹을 찾는다.
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    if (board[r][c] > 0 && !visited[r][c]) {
                        findGroup(r, c, visited);
                    }
                }
            }

            // 찾은 블록 그룹의 크기가 1 이하라면 종료
            if (groupInfo[0] <= 1) {
                break;
            }

            // 점수 획득
            totalScore += groupInfo[0] * groupInfo[0];
            // 블록 제거
            for (int block : blocks) {
                board[block / N][block % N] = -2;
            }

            down();
            rotate();
            down();
        }

        System.out.println(totalScore);
    }

    // 블록 그룹을 찾는다.
    public static void findGroup(int r, int c, boolean[][] visited) {
        Queue<int[]> queue = new LinkedList<>();
        Set<Integer> nowBlocks = new HashSet<>(); // 블록 목록
        int[] nowGroupInfo = new int[4]; // {그룹 크기, 무지개블록 수, 기준블록 행, 기준블록 열}
        int color = board[r][c];

        // 시작점 설정
        queue.offer(new int[] {r, c});
        visited[r][c] = true;
        nowBlocks.add(r * N + c);
        // 기준블록 위치 설정 (r, c가 0 ~ N-1 순서로 진행되기 때문에 한번 설정해주면 끝)
        nowGroupInfo[2] = r;
        nowGroupInfo[3] = c;

        while (!queue.isEmpty()) {
            int[] now = queue.poll();

            for (int i = 0; i < 4; i++) { // 인접한 네 방향 확인
                int nr = now[0] + drdc[i][0], nc = now[1] + drdc[i][1];

                if (!isValid(nr, nc) || nowBlocks.contains(nr * N + nc) || board[nr][nc] <= -1) {
                    continue;
                }

                if (board[nr][nc] == color) { // 일반 블록
                    visited[nr][nc] = true;
                } else if (board[nr][nc] == 0) { // 무지개 블록
                    nowGroupInfo[1]++;
                } else { // 색이 다른 일반 블록
                    continue;
                }

                queue.offer(new int[] {nr, nc});
                nowBlocks.add(nr * N + nc);
            }
        }

        nowGroupInfo[0] = nowBlocks.size();

        // 크기가 가장 큰 그룹, 무지개 블록이 많은 그룹, 기준 블록이 가장 아래, 기준 블록이 가장 오른쪽
        for (int i = 0; i < 4; i++) {
            if (nowGroupInfo[i] == groupInfo[i]) {
                continue;
            }

            if (nowGroupInfo[i] > groupInfo[i]) { // 이번에 찾은 그룹이 우선순위가 더 높다면
                groupInfo = nowGroupInfo;
                blocks = nowBlocks;
            }
            break;
        }
    }

    // 격자가 반시계 방향으로 회전
    public static void rotate() {
        int[][] newBoard = new int[N][N];

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                newBoard[r][c] = board[c][N - 1 - r];
            }
        }

        board = newBoard;
    }

    // 중력 작용
    public static void down() {
        for (int c = 0; c < N; c++) { // 각 열별로 확인
            for (int r = N - 1; r >= 0; r--) { // 가장 아래 블록부터 아래로 내려감
                int block = board[r][c];

                // 내려가지 않는 블록이라면
                if (block <= -1) {
                    continue;
                }
                // 내려가는 블록이라면
                board[r][c] = -2;
                int nr = r;
                while (nr < N && board[nr][c] == -2) {
                    nr++;
                }
                board[nr - 1][c] = block;
            }
        }
    }

    public static boolean isValid(int r, int c) {
        if (r < 0 || r >= N || c < 0 || c >= N) {
            return false;
        }
        return true;
    }
}
