import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.util.StringTokenizer;

public class SWEA2001 {
	public static String input = "1\r\n" + 
			"5 2\r\n" + 
			"1 3 3 6 7\r\n" + 
			"8 13 9 12 8\r\n" + 
			"4 16 11 12 6\r\n" + 
			"2 4 1 23 2\r\n" + 
			"9 13 4 7 3";

	public static void main(String[] args) throws NumberFormatException, IOException {
//		System.setIn(new FileInputStream("TestCase/SWExpertAcademy/2001input.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
//		in = new BufferedReader(new StringReader(input));

		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(in.readLine()); // 테스트케이스 수
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#").append(tc).append(" ");
			st = new StringTokenizer(in.readLine(), " ");
			int N = Integer.parseInt(st.nextToken()); // 전체 영역의 가로/세로 크기
			int M = Integer.parseInt(st.nextToken()); // 파리채의 가로/세로 크기
			
			int[][] area = new int[N][N]; // 전체 영역
			for (int row = 0; row < N; row++) {
				st = new StringTokenizer(in.readLine(), " ");
				for (int col = 0; col < N; col++) {
					area[row][col] = Integer.parseInt(st.nextToken());
				}
			}
			
			int maxSum = 0;
			for (int row = 0; row < N - M + 1; row++) {
				for (int col = 0; col < N - M + 1; col++) {
					int nowSum = 0;
					for (int i = 0; i < M; i++) {
						for (int j = 0; j < M; j++) {
							nowSum += area[row + i][col + j];
						}
					}
					maxSum = maxSum < nowSum ? nowSum : maxSum;
				}
			}
			
			sb.append(maxSum).append("\n");
		}
		
		System.out.println(sb.toString());
		
	}

}
