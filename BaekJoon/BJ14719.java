import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class BJ14719 {

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		////// 테스트용
		String test1 = "4 4\n" + "3 0 1 4";
		String test2 = "4 8\n" + "3 1 2 3 4 1 1 2";
		String test3 = "3 5\n" + "0 0 0 2 0";
		in = new BufferedReader(new StringReader(test3));
		////// 테스트용

		StringTokenizer st = new StringTokenizer(in.readLine(), " ");
		int H = Integer.parseInt(st.nextToken());
		int W = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(in.readLine(), " ");
		int[] heights = new int[W];
		for (int w = 0; w < W; w++) {
			heights[w] = Integer.parseInt(st.nextToken());
		}
		// 입력 완료

		int total = 0;
		Stack<int[]> stack = new Stack<int[]>();

		for (int i = 0; i < W; i++) {
			int nowHeight = heights[i];
			while (!stack.isEmpty() && stack.peek()[0] <= nowHeight) {
				int[] top = stack.pop();

				if (stack.isEmpty()) {
					break;
				}

				total += (Math.min(stack.peek()[0], nowHeight) - top[0]) * (i - stack.peek()[1] - 1);
			}

			stack.add(new int[] { nowHeight, i });
		}

		System.out.println(total);

	}

}
