import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Problem1225 {

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("1225input.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		for (int tc = 1; tc <= 10; tc++) {
			int t = Integer.parseInt(in.readLine());
			sb.append("#").append(t).append(" ");
			
			StringTokenizer st = new StringTokenizer(in.readLine(), " ");
			
			Queue<Integer> numbers = new LinkedList<Integer>();
			while (st.hasMoreTokens()) {
				numbers.offer(Integer.parseInt(st.nextToken()));
			}
			
			int nowNum = numbers.peek(), cycle = 1;
			while (nowNum > 0) {
				nowNum = numbers.poll();
				nowNum = nowNum < cycle ? 0 : nowNum - cycle;
				numbers.offer(nowNum);
				
				cycle = cycle == 5 ? 1 : cycle + 1;
			}
			
			while (!numbers.isEmpty()) {
				sb.append(numbers.poll());
				sb.append(" ");
			}
			sb.setLength(sb.length() - 1);
			sb.append("\n");
		}
		
		System.out.println(sb.toString());

	}

}
