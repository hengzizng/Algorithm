import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.util.StringTokenizer;

public class SWEA1873 {
	public static String str = "1\r\n" + "3 7\r\n" + "***....\r\n" + "*-..#**\r\n" + "#<.****\r\n" + "23\r\n"
			+ "SURSSSSUSLSRSSSURRDSRDS";
	public static int[][] dxdy = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } }; // U, D, L, R
	public static char[] directSign = { '^', 'v', '<', '>' };

	public static void main(String[] args) throws NumberFormatException, IOException {
		System.setIn(new FileInputStream("TestCase/SWExpertAcademy/1873input.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
//		in = new BufferedReader(new StringReader(str));

		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(in.readLine());

		for (int tc = 1; tc <= T; tc++) {
			sb.append("#").append(tc).append(" ");

			// 맵의 높이와 너비
			st = new StringTokenizer(in.readLine(), " ");
			int H = Integer.parseInt(st.nextToken());
			int W = Integer.parseInt(st.nextToken());

			// 맵 구성
			char[][] map = new char[H][W];
			int[] tank = new int[2]; // 전차의 위치
			int nowDir = 0; // 현재 전차가 바라보는 방향
			for (int row = 0; row < H; row++) {
				map[row] = in.readLine().toCharArray();
			}
			outer: for (int row = 0; row < H; row++) {
				for (int col = 0; col < W; col++) {
					if (map[row][col] == '^' || map[row][col] == 'v' || map[row][col] == '<' || map[row][col] == '>') {
						tank[0] = row;
						tank[1] = col;
						if (map[row][col] == '^') {
							nowDir = 0;
						} else if (map[row][col] == 'v') {
							nowDir = 1;
						} else if (map[row][col] == '<') {
							nowDir = 2;
						} else if (map[row][col] == '>') {
							nowDir = 3;
						}
						break outer;
					}
				}
			}

			// 사용자 명령어
			int N = Integer.parseInt(in.readLine());
			char[] commands = in.readLine().toCharArray();
			for (char command : commands) {
				if (command == 'U') {
					nowDir = 0;
					move(map, tank, nowDir);
				} else if (command == 'D') {
					nowDir = 1;
					move(map, tank, nowDir);
				} else if (command == 'L') {
					nowDir = 2;
					move(map, tank, nowDir);
				} else if (command == 'R') {
					nowDir = 3;
					move(map, tank, nowDir);
				} else if (command == 'S') {
					shoot(map, tank, nowDir);
				}
			}

			for (int row = 0; row < H; row++) {
				for (int col = 0; col < W; col++) {
					sb.append(map[row][col]);
				}
				sb.append("\n");
			}
		}

		System.out.println(sb.toString());

	}

	private static void move(char[][] map, int[] tank, int nowDir) {
		map[tank[0]][tank[1]] = directSign[nowDir];

		int row = tank[0] + dxdy[nowDir][0];
		int col = tank[1] + dxdy[nowDir][1];

		if (row >= 0 && row < map.length && col >= 0 && col < map[0].length && map[row][col] == '.') {
			map[tank[0]][tank[1]] = '.';
			tank[0] = row;
			tank[1] = col;
			map[row][col] = directSign[nowDir];
		}
	}

	private static void shoot(char[][] map, int[] tank, int nowDir) {
		int row = tank[0];
		int col = tank[1];
		boolean isWall = false;

		while (row >= 0 && row < map.length && col >= 0 && col < map[0].length) {
			if (map[row][col] == '*' || map[row][col] == '#') {
				isWall = true;
				break;
			}
			row += dxdy[nowDir][0];
			col += dxdy[nowDir][1];
		}

		if (isWall && map[row][col] == '*') {
			map[row][col] = '.';
		}
	}

}
