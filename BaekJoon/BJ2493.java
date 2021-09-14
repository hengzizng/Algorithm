import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class BJ2493 {
	
	static String str = "5\n"
			+ "6 9 5 7 4";

	public static void main(String[] args) throws IOException {
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		in = new BufferedReader(new StringReader(str));
		
		int N = Integer.parseInt(in.readLine()); // 탑의 수
		int[] towers = new int[N + 1];
		towers[0] = 100000000;
		StringTokenizer st = new StringTokenizer(in.readLine());
		for (int i = 1; i <= N; i++) {
			towers[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] receive = new int[N + 1];
		Stack<Integer> stack = new Stack<Integer>();
		for (int i = N; i > 0; i--) {
			while (!stack.isEmpty() && towers[stack.peek()] <= towers[i]) {
				receive[stack.pop()] = i;
			}
			stack.push(i);
		}
		
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i <= N; i++) {
			sb.append(receive[i]).append(" ");
		}
		
		System.out.println(sb.toString());
		
	}

}
