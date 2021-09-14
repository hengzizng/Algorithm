import java.io.*;
import java.util.StringTokenizer;

public class SWEA1208 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		System.setIn(new FileInputStream("TestCase/SWExpertAcademy/1208input.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		StringBuilder sb = new StringBuilder();
		for (int tc = 1; tc <= 10; tc++) {
			sb.append("#").append(tc).append(" ");
			int dumpCnt = Integer.parseInt(in.readLine()); // 덤프 가능 횟수.
			
			// index: 높이, value: 해당 높이를 가진 위치의 수.
			// 높이가 1 ~ 100까지이므로 101
			int[] heightCount = new int[101];
			StringTokenizer st = new StringTokenizer(in.readLine(), " ");
			for (int i = 0; i < 100; i++) {
				heightCount[Integer.parseInt(st.nextToken())]++;
			}
			
			// 현재 최소 높이를 찾는다.
			int minHeight = 1;
			for (int i = 1; i <= 100; i++) {
				if (heightCount[i] > 0) {
					minHeight = i;
					break;
				}
			}
			
			// 현재 최대 높이를 찾는다.
			int maxHeight = 1;
			for (int i = 100; i >= 1; i--) {
				if (heightCount[i] > 0) {
					maxHeight = i;
					break;
				}
			}
			
			while (--dumpCnt >= 0) {
				if (minHeight >= maxHeight) {
					break;
				}
				
				heightCount[minHeight]--;
				heightCount[minHeight + 1]++;
				heightCount[maxHeight]--;
				heightCount[maxHeight - 1]++;
				
				if (heightCount[minHeight] == 0) {
					minHeight++;
				}
				if (heightCount[maxHeight] == 0) {
					maxHeight--;
				}
			}
			
			sb.append(maxHeight - minHeight);
			sb.append("\n");
			
		}
		
		System.out.println(sb.toString());

	}

}
