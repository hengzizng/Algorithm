import java.io.*;
import java.util.*;

public class BJ14466 {

	public static int N;
	public static int[][] drdc = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

	public static void main(String[] args) throws Exception {
		// 길을 건너지 않으면 만날 수 없는 소의 쌍은
		// 길을 건너지 않고 갈 수 있는 모든 구역을 구해서
		// 각 구역에 속한 소의 수들을 곱한것과 같다
		// 구역이 3개고 각 구역에 속한 소의 수가 [1, 2, 3] 라면
		// 길을 건너지 않으면 만날 수 없는 소의 쌍은 1*2 + 1*3 + 2*3 이다.

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		//////
		String test = "4 10 8\r\n" + "1 2 1 3\r\n" + "2 2 2 3\r\n" + "2 1 3 1\r\n" + "2 2 3 2\r\n" + "2 3 3 3\r\n"
				+ "2 4 3 4\r\n" + "3 2 3 3\r\n" + "4 2 4 3\r\n" + "1 1\r\n" + "1 2\r\n" + "2 1\r\n" + "2 2\r\n"
				+ "1 3\r\n" + "1 4\r\n" + "2 3\r\n" + "3 1\r\n" + "3 2\r\n" + "4 4";
		in = new BufferedReader(new StringReader(test));
		//////

		StringTokenizer st = new StringTokenizer(in.readLine(), " ");
		N = Integer.parseInt(st.nextToken()); // 목초지 가로, 세로 크기
		int K = Integer.parseInt(st.nextToken()); // 소의 수
		int R = Integer.parseInt(st.nextToken()); // 길의 수

		Set<String> roads = new HashSet<>(); // 길을 String 상태로 저장하는 집합
		for (int r = 0; r < R; r++) {
			st = new StringTokenizer(in.readLine(), " ");

			StringBuilder sb = new StringBuilder();
			while (st.hasMoreTokens()) {
				sb.append(Integer.parseInt(st.nextToken()) - 1).append(" ");
			}
			sb.setLength(sb.length() - 1);

			roads.add(sb.toString());
		}

		// farm: 농장의 상태를 나타낸다. (0: 목초지, 1: 소)
		int[][] farm = new int[N][N];
		for (int k = 0; k < K; k++) {
			st = new StringTokenizer(in.readLine(), " ");

			int r = Integer.parseInt(st.nextToken()) - 1;
			int c = Integer.parseInt(st.nextToken()) - 1;

			farm[r][c] = 1;
		}

		// 구역별로 소의 수를 구한다.
		List<Integer> cowCount = new ArrayList<Integer>(); // 구역별로 위치한 소의 수
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				if (farm[r][c] < 2) {
					cowCount.add(getCowCountInArea(r, c, farm, roads));
				}
			}
		}

		int answer = 0; // 길을 건너지 않으면 만날 수 없는 소의 쌍의 수
		for (int i = 0; i < cowCount.size() - 1; i++) {
			for (int j = i + 1; j < cowCount.size(); j++) {
				answer += cowCount.get(i) * cowCount.get(j);
			}
		}

		System.out.println(answer);
	}

	// 한 구역에 위치한 소의 수를 구하는 함수
	private static int getCowCountInArea(int r, int c, int[][] farm, Set<String> roads) {
		int cowCount = 0;

		Queue<int[]> queue = new LinkedList<int[]>();
		if (farm[r][c] == 1) {
			cowCount++;
		}
		farm[r][c] = 2;
		queue.offer(new int[] { r, c });

		while (!queue.isEmpty()) {
			int[] now = queue.poll();

			for (int i = 0; i < 4; i++) {
				int nr = now[0] + drdc[i][0], nc = now[1] + drdc[i][1];

				if (nr >= 0 && nr < N && nc >= 0 && nc < N && farm[nr][nc] != 2) {
					String temp1 = now[0] + " " + now[1] + " " + nr + " " + nc;
					String temp2 = nr + " " + nc + " " + now[0] + " " + now[1];

					if (roads.contains(temp1) || roads.contains(temp2)) {
						continue;
					}

					if (farm[nr][nc] == 1) {
						cowCount++;
					}
					farm[nr][nc] = 2;
					queue.offer(new int[] { nr, nc });
				}
			}
		}

		return cowCount;
	}

}
