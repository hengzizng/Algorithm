import java.io.*;
import java.util.LinkedList;
import java.util.Queue;

public class BJ20056 {
    static class Fireball {
        int m, s, d; // 질량, 속력, 방향

        Fireball(int m, int s, int d) {
            this.m = m;
            this.s = s;
            this.d = d;
        }
    }

    static int N, totalM;
    // ↑, ↗, →, ↘, ↓, ↙, ←, ↖
    static int[] dr = {-1, -1, 0, 1, 1, 1, 0, -1}, dc = {0, 1, 1, 1, 0, -1, -1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        String[] input = in.readLine().split(" ");
        N = Integer.parseInt(input[0]); // 격자 크기
        int M = Integer.parseInt(input[1]); // 파이어볼 개수
        int K = Integer.parseInt(input[2]); // 이동(명령) 수

        Queue<Fireball>[][] fireballs = new LinkedList[N][N]; // 각 위치의 파이어볼 리스트
        for (int i = 0; i < M; i++) {
            input = in.readLine().split(" ");
            int r = Integer.parseInt(input[0]) - 1;
            int c = Integer.parseInt(input[1]) - 1;
            int m = Integer.parseInt(input[2]);
            int s = Integer.parseInt(input[3]);
            int d = Integer.parseInt(input[4]);

            fireballs[r][c] = new LinkedList<>();
            fireballs[r][c].offer(new Fireball(m, s, d));
            totalM += m;
        }

        for (int k = 0; k < K; k++) { // K번 이동(명령)
            fireballs = move(fireballs);
            mix(fireballs);
        }

        System.out.println(totalM);
    }

    public static Queue<Fireball>[][] move(Queue<Fireball>[][] fireballs) {
        // 이동한 파이어볼이 뒤에 있어서 또 다시 이동하는 것을 방지하기 위해 새로 만들어서 사용
        Queue<Fireball>[][] newFireballs = new LinkedList[N][N];

        // 각 위치별로 반복
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (fireballs[r][c] == null || fireballs[r][c].size() == 0) {
                    continue;
                }

                while (!fireballs[r][c].isEmpty()) { // 같은 위치의 모든 파이어볼을 확인
                    Fireball fireball = fireballs[r][c].poll();

                    int nr = (r + fireball.s * (dr[fireball.d] + (dr[fireball.d] < 0 ? N : 0))) % N;
                    int nc = (c + fireball.s * (dc[fireball.d] + (dc[fireball.d] < 0 ? N : 0))) % N;

                    if (newFireballs[nr][nc] == null) {
                        newFireballs[nr][nc] = new LinkedList<>();
                    }
                    newFireballs[nr][nc].offer(new Fireball(fireball.m, fireball.s, fireball.d));
                }
            }
        }

        return newFireballs;
    }

    public static void mix(Queue<Fireball>[][] fireballs) {
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (fireballs[r][c] == null || fireballs[r][c].size() < 2) {
                    continue;
                }

                // dFlag: 파이어볼이 합쳐질 때 짝수이면 0, 홀수이면 1을 더해준다
                int count = fireballs[r][c].size(), mSum = 0, sSum = 0, dFlag = 0;
                while (!fireballs[r][c].isEmpty()) {
                    Fireball fireball = fireballs[r][c].poll();
                    totalM -= fireball.m;

                    mSum += fireball.m;
                    sSum += fireball.s;
                    dFlag += fireball.d % 2 == 0 ? 0 : 1;
                }

                mSum = mSum / 5;
                if (mSum == 0) { // 질량이 0인 파이어볼은 소멸
                    continue;
                }

                sSum = sSum / count;
                int d = dFlag == 0 || dFlag == count ? 0 : 1; // 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면 0, 2, 4, 6
                for (; d < 8; d += 2) {
                    fireballs[r][c].offer(new Fireball(mSum, sSum, d));
                    totalM += mSum;
                }
            }
        }
    }
}
