// 19808 KB 148 ms


import java.io.*;
import java.util.*;

public class BJ19238 {

	public static int N; // 지도의 가로,세로 크기
	public static int[][] drdc = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

	public static void main(String[] args) throws Exception {

		// M: 승객 수
		// N: 격자 크기

		// 택시는 상하좌우로 이동가능

		// [태울 승객 선택]
		// 현재 위치에서 최단거리의 승객 (거리가 같으면 행, 열이 작은 순)
		// 택시와 승객이 같은 위치에 있을 수도 있는데 이 때 둘 사이 거리는 0

		// [연료]
		// 한 칸에 1씩 소모
		// 한 승객을 목적지로 이동시키면, 그 승객을 태워 이동하는 동안 소모한 연료 양의 두 배 충전
		// 이동하는 도중 연료가 바닥나면(연료 < 0) 이동 실패 후 업무 종료 => -1 출력
		// 모든 손님을 이동시킴 => 남은 연료의 양 출력

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		//////
		String test1 = "6 3 15\r\n" + "0 0 1 0 0 0\r\n" + "0 0 1 0 0 0\r\n" + "0 0 0 0 0 0\r\n" + "0 0 0 0 0 0\r\n"
				+ "0 0 0 0 1 0\r\n" + "0 0 0 1 0 0\r\n" + "6 5\r\n" + "2 2 5 6\r\n" + "5 4 1 6\r\n" + "4 2 3 5";
		String test2 = "6 3 13\r\n" + "0 0 1 0 0 0\r\n" + "0 0 1 0 0 0\r\n" + "0 0 0 0 0 0\r\n" + "0 0 0 0 0 0\r\n"
				+ "0 0 0 0 1 0\r\n" + "0 0 0 1 0 0\r\n" + "6 5\r\n" + "2 2 5 6\r\n" + "5 4 1 6\r\n" + "4 2 3 5";
		String test3 = "6 3 100\r\n" + "0 0 1 0 0 0\r\n" + "0 0 1 0 0 0\r\n" + "0 0 0 1 0 0\r\n" + "0 0 0 1 0 0\r\n"
				+ "0 0 0 0 1 0\r\n" + "0 0 0 1 0 0\r\n" + "6 5\r\n" + "2 2 5 6\r\n" + "5 4 1 6\r\n" + "4 2 3 5";
		in = new BufferedReader(new StringReader(test1));
		//////

		StringTokenizer st = new StringTokenizer(in.readLine(), " ");
		N = Integer.parseInt(st.nextToken()); // 지도의 가로, 세로 크기
		int M = Integer.parseInt(st.nextToken()); // 승객 수

		// 택시의 현재 정보 {행, 열, 남은 연료}
		int[] taxi = new int[3];
		taxi[2] = Integer.parseInt(st.nextToken()); // 연료의 양

		int[][] map = new int[N][N]; // 현재 지도 상태 (0: 빈칸, 1: 벽, 2 ~ (M + 1): 승객의 출발지(승객번호))
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(in.readLine(), " ");
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		st = new StringTokenizer(in.readLine(), " ");
		taxi[0] = Integer.parseInt(st.nextToken()) - 1;
		taxi[1] = Integer.parseInt(st.nextToken()) - 1;

		// 승객 정보 입력
		// 한 승객의 출발지와 또다른 승객의 목적지가 같을 수도 있기 때문에 목적지는 따로 저장해둔다
		int[][] destinations = new int[M + 2][2];
		for (int m = 2; m <= M + 1; m++) {
			st = new StringTokenizer(in.readLine(), " ");

			// 출발지
			int row = Integer.parseInt(st.nextToken()) - 1;
			int col = Integer.parseInt(st.nextToken()) - 1;
			map[row][col] = m;

			// 도착지
			destinations[m][0] = Integer.parseInt(st.nextToken()) - 1;
			destinations[m][1] = Integer.parseInt(st.nextToken()) - 1;
		}

		int passenger = 0; // 태울 승객 번호
		for (int m = 0; m < M; m++) {
			passenger = getPassenger(taxi, map);

			if (passenger == 0 || !toDestination(taxi, destinations[passenger], map)) {
				taxi[2] = -1;
				break;
			}
		}

		System.out.println(taxi[2]);
	}

	// 태울 승객의 번호를 찾아 리턴하는 함수
	public static int getPassenger(int[] taxi, int[][] map) {
		// 태울 승객 정보 {행, 열, 승객 번호, 최단거리}
		int[] passenger = new int[] { N, N, map[taxi[0]][taxi[1]], 0 };

		if (passenger[2] >= 2) { // 현재 택시의 위치가 승객이 있는 곳이면
			map[taxi[0]][taxi[1]] = 0;
			return passenger[2];
		}

		Queue<int[]> queue = new LinkedList<int[]>();
		boolean[][] isVisited = new boolean[N][N];

		queue.offer(new int[] { taxi[0], taxi[1], 0 });
		isVisited[taxi[0]][taxi[1]] = true;

		while (!queue.isEmpty()) {
			int[] now = queue.poll();

			for (int i = 0; i < 4; i++) {
				int nr = now[0] + drdc[i][0], nc = now[1] + drdc[i][1], ndist = now[2] + 1;

				if (nr < 0 || nr >= N || nc < 0 || nc >= N || map[nr][nc] == 1 || isVisited[nr][nc]) {
					continue;
				}

				// 승객을 발견한 적이 있는데 현재 탐색하려는 곳이 더 멀거나 연료가 부족하면 탐색 종료
				if ((passenger[3] > 0 && passenger[3] < ndist) || (taxi[2] < ndist)) {
					queue.clear();
					break;
				}

				isVisited[nr][nc] = true;
				queue.offer(new int[] { nr, nc, ndist });

				// 이번에 승객을 발견하지 못했다면
				if (map[nr][nc] == 0) {
					continue;
				}

				// 이번에 승객을 발견했다면
				passenger[3] = ndist;
				// 이번에 발견한 승객의 조건이 더 우선이라면
				if ((passenger[0] > nr) || (passenger[0] == nr && passenger[1] > nc)) {
					passenger[0] = nr;
					passenger[1] = nc;
					passenger[2] = map[nr][nc];
				}
			}
		}

		if (passenger[0] < N) { // 승객을 못찾아서 초깃값 그대로일 경우를 대비
			taxi[0] = passenger[0];
			taxi[1] = passenger[1];
			taxi[2] -= passenger[3];
			map[taxi[0]][taxi[1]] = 0;
		}

		return passenger[2];
	}

	// 태운 승객을 목적지까지 이동시킨다
	public static boolean toDestination(int[] taxi, int[] destination, int[][] map) {
		Queue<int[]> queue = new LinkedList<int[]>();
		boolean[][] isVisited = new boolean[N][N];

		queue.offer(new int[] { taxi[0], taxi[1], 0 });
		isVisited[taxi[0]][taxi[1]] = true;

		while (!queue.isEmpty()) {
			int[] now = queue.poll();

			for (int i = 0; i < 4; i++) {
				int nr = now[0] + drdc[i][0], nc = now[1] + drdc[i][1], ndist = now[2] + 1;

				if (nr < 0 || nr >= N || nc < 0 || nc >= N || map[nr][nc] == 1 || isVisited[nr][nc]) {
					continue;
				}

				// 연료가 없으면
				if (ndist > taxi[2]) {
					break;
				}

				// 도착지를 찾았으면
				if (nr == destination[0] && nc == destination[1]) {
					queue.clear();
					taxi[0] = nr;
					taxi[1] = nc;
					// 한 승객을 목적지로 이동시키면, 그 승객을 태워 이동하는 동안
					// 소모한 연료 양의 두 배를 충전하기 때문에 연료를 더해준다
					taxi[2] += ndist;
					return true;
				}

				queue.offer(new int[] { nr, nc, ndist });
				isVisited[nr][nc] = true;
			}
		}

		return false;
	}

}
