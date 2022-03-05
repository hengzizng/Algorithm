import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BJ14499 {
    public static void main(String[] args) throws Exception {
        // 칸 숫자 0: 주사위 바닥면 -> 칸
        // 칸 숫자 1 이상: 칸 -> 주사위 바닥면, 칸 = 0
        // 매번 이동 후 주사위의 상단에 있는 값 출력
        // 주사위가 바깥으로 이동하려 하면 아예 무시 (출력도 하지 않음)
        // 1: 동, 2: 서, 3: 북, 4: 남
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int[][] dxdy = {{0, 0}, {0, 1}, {0, -1}, {-1, 0}, {1, 0}};

        String[] input = in.readLine().split(" ");
        int N = Integer.parseInt(input[0]); // 지도의 행 수
        int M = Integer.parseInt(input[1]); // 지도의 열 수
        int x = Integer.parseInt(input[2]); // 주사위의 행 위치
        int y = Integer.parseInt(input[3]); // 주사위의 열 위치
        int K = Integer.parseInt(input[4]); // 명령의 개수

        int[][] map = new int[N][M]; // 지도 상태
        for (int n = 0; n < N; n++) {
            input = in.readLine().split(" ");
            for (int m = 0; m < M; m++) {
                map[n][m] = Integer.parseInt(input[m]);
            }
        }

        int[] dice = new int[6]; // {윗면, 앞면, 바닥면, 뒷면, 왼쪽면, 오른쪽면}
        int command, nx, ny;

        input = in.readLine().split(" ");
        for (int k = 0; k < K; k++) {
            command = Integer.parseInt(input[k]);

            nx = x + dxdy[command][0];
            ny = y + dxdy[command][1];

            if (nx < 0 || nx >= N || ny < 0 || ny >= M) { // 지도 바깥으로 벗어나면
                continue;
            }

            int temp = dice[2]; // 바닥면 값 임시 저장
            if (command == 1) { // 동
                dice[2] = dice[5]; // 오른쪽면은 바닥면으로
                dice[5] = dice[0]; // 윗면은 오른쪽면으로
                dice[0] = dice[4]; // 왼쪽면은 윗면으로
                dice[4] = temp; // 바닥면은 왼쪽면으로
            } else if (command == 2) { // 서
                dice[2] = dice[4]; // 왼쪽면은 바닥면으로
                dice[4] = dice[0]; // 윗면은 왼쪽면으로
                dice[0] = dice[5]; // 오른쪽면은 윗면으로
                dice[5] = temp; // 바닥면은 오른쪽면으로
            } else if (command == 3) { // 북
                dice[2] = dice[3]; // 뒷면은 바닥면으로
                dice[3] = dice[0]; // 윗면은 뒷면으로
                dice[0] = dice[1]; // 앞면은 윗면으로
                dice[1] = temp; // 바닥면은 앞면으로
            } else { // 남
                dice[2] = dice[1]; // 앞면은 바닥면으로
                dice[1] = dice[0]; // 윗면은 앞면으로
                dice[0] = dice[3]; // 뒷면은 윗면으로
                dice[3] = temp; // 바닥면은 뒷면으로
            }

            if (map[nx][ny] == 0) {
                map[nx][ny] = dice[2];
            } else {
                dice[2] = map[nx][ny];
                map[nx][ny] = 0;
            }

            x = nx;
            y = ny;
            sb.append(dice[0]).append("\n");
        }

        System.out.println(sb.toString());
    }
}
