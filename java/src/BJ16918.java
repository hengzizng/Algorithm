// 19972KB, 168ms

import java.io.*;
import java.util.StringTokenizer;

public class BJ16918 {

	public static int R, C;
	public static int[][] drdc = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

	public static void main(String[] args) throws Exception {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(in.readLine());
		R = Integer.parseInt(st.nextToken()); // 격자판 세로 길이
		C = Integer.parseInt(st.nextToken()); // 격자판 가로 길이
		int N = Integer.parseInt(st.nextToken()); // N초 후의 상태를 구한다.

		int[][] map = new int[R][C]; // 폭탄이 설치된 시간을 저장한다. (폭탄이 없는 칸이라면 -1)
		for (int r = 0; r < R; r++) {
			char[] temp = in.readLine().toCharArray();
			for (int c = 0; c < C; c++) {
				if (temp[c] == '.') {
					map[r][c] = -1;
				}
			}
		}

		if (N % 2 == 0) { // 짝수 초면 모든 칸에 폭탄이 설치되어있다
			for (int r = 0; r < R; r++) {
				for (int c = 0; c < C; c++) {
					sb.append("O");
				}
				sb.append("\n");
			}
		} else {
			for (int time = 2; time <= N; time++) {
				if (time % 2 == 0) { // 짝수 초에는 나머지 모든 칸에 폭탄을 설치
					setBomb(time, map);
				} else { // 홀수 초에는 3초 전에 설치한 폭탄이 폭발
					exploidByTime(time - 3, map);
				}
			}

			for (int r = 0; r < R; r++) {
				for (int c = 0; c < C; c++) {
					if (map[r][c] == -1) {
						sb.append(".");
					} else {
						sb.append("O");
					}
				}
				sb.append("\n");
			}
		}

		System.out.println(sb.toString());

	}

	// 폭탄이 설치되어있지 않은 모든 칸에 폭탄을 설치하는 함수
	public static void setBomb(int time, int[][] map) {
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				if (map[r][c] == -1) {
					map[r][c] = time;
				}
			}
		}
	}

	// targetTime에 설치된 폭탄을 터뜨리는 함수
	public static void exploidByTime(int targetTime, int[][] map) {
		int[][] original = getCopiedMap(map);

		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				if (original[r][c] == targetTime) {
					exploidOne(r, c, map);
				}
			}
		}
	}

	// 해당 위치의 폭탄을 터뜨리는 함수
	public static void exploidOne(int row, int col, int[][] map) {
		map[row][col] = -1;

		for (int i = 0; i < 4; i++) {
			int nr = row + drdc[i][0], nc = col + drdc[i][1];
			if (nr >= 0 && nr < R && nc >= 0 && nc < C) {
				map[nr][nc] = -1;
			}
		}
	}

	// map을 복사해서 리턴하는 함수
	public static int[][] getCopiedMap(int[][] map) {
		int[][] copied = new int[R][C];

		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				copied[r][c] = map[r][c];
			}
		}

		return copied;
	}

}
