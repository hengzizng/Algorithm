import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SWEA1954 {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int[][] dxdy = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };

		StringBuilder sb = new StringBuilder();
		int TC = Integer.parseInt(in.readLine());
		for (int tc = 1; tc <= TC; tc++) {
			sb.append("#").append(tc).append("\n");
			int dx = 0, dy = 0;
			int N = Integer.parseInt(in.readLine());
			int[][] snail = new int[N][N];

			int addNum = 0;
			for (int i = N - 1; i > 0; i -= 2) {
				for (int j = 0; j < 4; j++) {
					for (int k = 0; k < i; k++) {
						snail[dx][dy] = k + 1 + addNum;
						dx += dxdy[j][0];
						dy += dxdy[j][1];
					}

					if (j == 3) {
						dx -= dxdy[j][0];
						dy -= dxdy[j][0];
					}

					addNum += i;
				}
			}

			if (N % 2 == 1) {
				snail[N / 2][N / 2] = N * N;
			}

			for (int row = 0; row < N; row++) {
				for (int col = 0; col < N; col++) {
					sb.append(snail[row][col] + " ");
				}
				sb.append("\n");
			}

		}
		System.out.println(sb.toString());

	}

}
