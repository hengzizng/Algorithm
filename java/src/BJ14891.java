import java.io.*;
import java.util.LinkedList;
import java.util.List;

public class BJ14891 {
    public static int gears[][];

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        ////// test
        String test
                = "10010011\n" + "01010011\n" + "11100011\n" + "01010101\n" + "8\n" + "1 1\n" + "2 1\n" + "3 1\n" + "4 1\n" + "1 -1\n" + "2 -1\n" + "3 -1\n" + "4 -1";
        in = new BufferedReader(new StringReader(test));
        ////// test

        String[] input;
        gears = new int[4][8];
        for (int i = 0; i < 4; i++) {
            input = in.readLine().split("");
            for (int j = 0; j < 8; j++) {
                gears[i][j] = Integer.parseInt(input[j]);
            }
        }

        int K = Integer.parseInt(in.readLine()); // 회전 횟수
        for (int k = 0; k < K; k++) {
            input = in.readLine().split(" ");
            int gear = Integer.parseInt(input[0]) - 1; // 톱니바퀴 0 ~ 3번
            int direction = Integer.parseInt(input[1]); // 1: 시계 방향, -1: 반시계 방향
            rotate(gear, direction);
        }

        System.out.println(getScore());
    }

    public static void rotate(int target, int direction) {
        List<int[]> rotateList = new LinkedList<>();
        rotateList.add(new int[]{target, direction});

        // 현재 톱니바퀴의 왼쪽 톱니바퀴들
        int dirFlag = direction;
        for (int gear = target - 1; gear >= 0; gear--) {
            dirFlag *= -1;
            if (gears[gear + 1][6] == gears[gear][2]) {
                break;
            } else {
                rotateList.add(new int[]{gear, dirFlag});
            }
        }

        // 현재 톱니바퀴의 오른쪽 톱니바퀴들
        dirFlag = direction;
        for (int gear = target + 1; gear < 4; gear++) {
            dirFlag *= -1;
            if (gears[gear - 1][2] == gears[gear][6]) {
                break;
            } else {
                rotateList.add(new int[]{gear, dirFlag});
            }
        }

        // 톱니바퀴들 회전
        for (int[] gear : rotateList) {
            int[] temp = new int[8];
            for (int i = 0; i < 8; i++) {
                temp[i] = gears[gear[0]][i];
            }

            if (gear[1] == 1) { // 시계 방향 회전
                for (int i = 0; i < 8; i++) {
                    gears[gear[0]][i] = temp[(i + 7) % 8];
                }
            } else { // 반시계 방향 회전
                for (int i = 0; i < 8; i++) {
                    gears[gear[0]][i] = temp[(i + 1) % 8];
                }
            }
        }
    }

    public static int getScore() {
        int score = 0;

        for (int i = 0; i < 4; i++) {
            score += (1 << i) * gears[i][0];
        }

        return score;
    }
}
