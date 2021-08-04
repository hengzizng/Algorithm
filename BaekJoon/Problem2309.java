import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Problem2309 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		int overHeight = -100;
		int[] heights = new int[9];
		boolean[] isReal = new boolean[9];
		for (int i = 0; i < 9; i++) {
			heights[i] = Integer.parseInt(in.readLine());
			overHeight += heights[i];
			isReal[i] = true;
		}
		Arrays.sort(heights);
		
		outer: for (int i = 0; i < 8; i++) {
			int fakeHeight = heights[i];			
			for (int j = i; j < 9; j++) {
				if (heights[j] == overHeight - fakeHeight) {
					isReal[i] = false;
					isReal[j] = false;
					break outer;
				}
			}
		}

		for (int i = 0; i < 9; i++) {
			if (isReal[i]) {
				System.out.println(heights[i]);
			}
		}

	}

}
