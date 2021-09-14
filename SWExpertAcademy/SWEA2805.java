import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringReader;

public class SWEA2805 {
	public static String str = "1\r\n" + 
			"5\r\n" + 
			"14054\r\n" + 
			"44250\r\n" + 
			"02032\r\n" + 
			"51204\r\n" + 
			"52212";

	public static void main(String[] args) throws NumberFormatException, IOException {
		System.setIn(new FileInputStream("TestCase/SWExpertAcademy/2805input.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
//		in = new BufferedReader(new StringReader(str));
		
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(in.readLine()); // 테스트케이스 수
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#").append(tc).append(" ");
			int N = Integer.parseInt(in.readLine()); // 농장 크기
			
			int[][] farm = new int[N][N];
			for (int row = 0; row < N; row++) {
				String rowStr = in.readLine();
				for (int col = 0; col < N; col++) {
					farm[row][col] = rowStr.charAt(col) - '0';
				}
			}
			
			int profit = 0;
			int half = N / 2;
			for (int row = 0; row < half; row++) {
				for (int col = half - row; col <= half + row; col++) {
					profit += farm[row][col];
				}
			}
			for (int row = half; row < N; row++) {
				for (int col = 0 + row - half; col < N - row + half; col++) {
					profit += farm[row][col];
				}
			}
			
			sb.append(profit).append("\n");
		}
		
		System.out.println(sb.toString());
		
	}

}
