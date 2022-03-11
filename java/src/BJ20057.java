import java.io.*;

public class BJ20057 {
    public static int N;
    public static int[] dr = {0, 1, 0, -1}, dc = {-1, 0, 1, 0}; // 좌, 하, 우, 상

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        ////// test
        String test = "9\n" + "193 483 223 482 858 274 847 283 748\n" + "484 273 585 868 271 444 584 293 858\n" + "828 384 382 818 347 858 293 999 727\n" + "818 384 727 373 636 141 234 589 991\n" + "913 564 555 827 0 999 123 123 123\n" + "321 321 321 983 982 981 983 980 990\n" + "908 105 270 173 147 148 850 992 113\n" + "943 923 982 981 223 131 222 913 562\n" + "752 572 719 590 551 179 141 137 731\n";
        in = new BufferedReader(new StringReader(test));
        ////// test

        N = Integer.parseInt(in.readLine()); // 격자의 크기
        int[][] map = new int[N][N]; // 격자 (각 칸의 모래의 양)
        for (int r = 0; r < N; r++) {
            String[] input = in.readLine().split(" ");
            for (int c = 0; c < N; c++) {
                map[r][c] = Integer.parseInt(input[c]);
            }
        }

        int r = N / 2, c = N / 2, d = 0; // 토네이도의 행, 열 위치, 방향
        int nr = r, nc = c; // 토네이도가 다음에 갈 위치
        int size = 0, outSum = 0;

        // 토네이도의 이동
        while (++size < N) {
            for (int i = 0; i < 2; i++) {
                for (int j = 0; j < size; j++) {
                    nr = r + dr[d];
                    nc = c + dc[d];
                    outSum += move(nr, nc, d, map);
                    r = nr;
                    c = nc;
                }
                d = (d + 1) % 4;
            }
        }
        while (c > 0) {
            nc = c - 1;
            outSum += move(nr, nc, d, map);
            c = nc;
        }

        System.out.println(outSum);
    }

    // 모래의 이동
    public static int move(int nr, int nc, int d, int[][] map) {
        int outSum = 0, total = map[nr][nc]; // 격자 밖으로 나간 모래의 양, 옮겨질 총 모래의 양

        int[] moveVal = new int[6]; // 1%, 2%, 5%, 7%, 10%, alpha 에 옮겨지는 모래의 양
        moveVal[0] = (int) (total * 0.01);
        moveVal[1] = (int) (total * 0.02);
        moveVal[2] = (int) (total * 0.05);
        moveVal[3] = (int) (total * 0.07);
        moveVal[4] = (int) (total * 0.1);
        moveVal[5] = total;
        for (int i = 0; i < 5; i++) {
            moveVal[5] -= moveVal[i] * (i == 2 ? 1 : 2);
        }

        int r, c;

        // 원래 위치에서 왼쪽으로 한칸 (7%)
        d = (d + 1) % 4;
        r = nr + dr[d];
        c = nc + dc[d];
        if (isValid(r, c)) {
            map[r][c] += moveVal[3];
        } else {
            outSum += moveVal[3];
        }

        // 원래 위치에서 왼쪽에 있는 10%, 2%, 1% 순서대로 처리
        d = (d + 3) % 4; // 10%
        if (isValid(r + dr[d], c + dc[d])) {
            map[r + dr[d]][c + dc[d]] += moveVal[4];
        } else {
            outSum += moveVal[4];
        }
        d = (d + 1) % 4; // 2%
        if (isValid(r + dr[d], c + dc[d])) {
            map[r + dr[d]][c + dc[d]] += moveVal[1];
        } else {
            outSum += moveVal[1];
        }
        d = (d + 1) % 4; // 1%
        if (isValid(r + dr[d], c + dc[d])) {
            map[r + dr[d]][c + dc[d]] += moveVal[0];
        } else {
            outSum += moveVal[0];
        }

        // 원래 위치에서 오른쪽으로 한칸 (7%)
        d = (d + 1) % 4;
        r = nr + dr[d];
        c = nc + dc[d];
        if (isValid(r, c)) {
            map[r][c] += moveVal[3];
        } else {
            outSum += moveVal[3];
        }

        // 원래 위치에서 오른쪽에 있는 1%, 2%, 10% 순서대로 처리
        d = (d + 3) % 4; // 1%
        if (isValid(r + dr[d], c + dc[d])) {
            map[r + dr[d]][c + dc[d]] += moveVal[0];
        } else {
            outSum += moveVal[0];
        }
        d = (d + 1) % 4; // 2%
        if (isValid(r + dr[d], c + dc[d])) {
            map[r + dr[d]][c + dc[d]] += moveVal[1];
        } else {
            outSum += moveVal[1];
        }
        d = (d + 1) % 4; // 10%
        if (isValid(r + dr[d], c + dc[d])) {
            map[r + dr[d]][c + dc[d]] += moveVal[4];
        } else {
            outSum += moveVal[4];
        }

        // 원래 위치에서 위로 한칸 (alpha)
        r = nr + dr[d];
        c = nc + dc[d];
        if (isValid(r, c)) {
            map[r][c] += moveVal[5];
        } else {
            outSum += moveVal[5];
        }

        // 원래 위치에서 위로 두칸 (5%)
        r += dr[d];
        c += dc[d];
        if (isValid(r, c)) {
            map[r][c] += moveVal[2];
        } else {
            outSum += moveVal[2];
        }

        map[nr][nc] = 0;

        return outSum;
    }

    public static boolean isValid(int r, int c) {
        if (r >= 0 && r < N && c >= 0 && c < N) {
            return true;
        }
        return false;
    }
}
