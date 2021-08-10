import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.util.StringTokenizer;

public class Problem2578 {
	
	public static String str = "11 12 2 24 10\n"
			+ "16 1 13 3 25\n"
			+ "6 20 5 21 17\n"
			+ "19 4 8 14 9\n"
			+ "22 15 7 23 18\n"
			+ "5 10 7 16 2\n"
			+ "4 22 8 17 13\n"
			+ "3 18 1 6 25\n"
			+ "12 19 23 14 21\n"
			+ "11 24 9 20 15";
	
	public static int LEN = 5;
	public static int[][] board = new int[LEN][LEN];
	// 현재 보드에서 지워진 숫자의 수 {행, 열, 좌우대각선, 우좌대각선}
	public static int[][] state = new int[4][LEN];

	public static void main(String[] args) throws IOException {
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		in = new BufferedReader(new StringReader(str));
		StringTokenizer st;
		
		// 빙고판
		for (int i = 0; i < LEN; i++) {
			st = new StringTokenizer(in.readLine());
			for (int j = 0; j < LEN; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 사회자가 부르는 수
		int count = 0;
		outer: for (int i = 0; i < LEN; i++) {
			st = new StringTokenizer(in.readLine());
			for (int j = 0; j < LEN; j++) {
				count++;
				int nowNum = Integer.parseInt(st.nextToken());
				deleteNum(nowNum);
				if (getBingoCount() >= 3) {
					System.out.println(count);
					break outer;
				}
			}
		}		

	}
	
	public static void deleteNum(int target) {
		for (int i = 0; i < LEN; i++) {
			for (int j = 0; j < LEN; j++)  {
				if (board[i][j] == target) {
					state[0][i]++;
					state[1][j]++;
					if (i == j) {
						state[2][0]++;
					}
					if (i == 4 - j) {
						state[3][0]++;
					}
					
					return;
				}
			}
		}
	}
	
	public static int getBingoCount() {
		int count = 0;
		for (int i = 0; i < state.length; i++) {
			for (int j = 0; j < state[i].length; j++) {
				if (state[i][j] == 5) {
					count++;
				}
			}
		}
		
		return count;
	}

}
