public class P60059 {
	
	public static void main(String[] args) {
		
		int[][] key = {{0, 0, 0}, {1, 0, 0}, {0, 1, 1}};
		int[][] lock = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}};
		
		System.out.println(solution(key, lock));
		
	}
	
	static public boolean solution(int[][] key, int[][] lock) {
        if (open(key, lock)) { // 회전 없이 체크했을 때 키를 열 수 있으면 바로 true 반환
        	return true;
        }
        
        for (int i = 0; i < 3; i++) { // 키를 3번 회전한다.
        	key = rotateKey(key);
        	if (open(key, lock)) {
        		return true;
        	}
        }
        
        // 끝까지 리턴되지 않았으면 열 수 없다.
        return false;
    }
	
	static public int[][] rotateKey(int[][] key) { // key를 시계 방향으로 90도 회전
		int M = key.length;
		int[][] rotatedKey = new int[M][M];
		
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < M; j++) {
				rotatedKey[j][M - 1 - i] = key[i][j];
			}
		}
		
		return rotatedKey;
	}
	
	static public boolean open(int[][] key, int[][] lock) {
		int N = lock.length, M = key.length;
		
		int[][] extendedLock = new int[N + M + M][N + M + M];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				extendedLock[i + M][j + M] = lock[i][j];
			}
		}
		
		int[] start = {0, 0}; // extendedLock 내부에서의 key의 시작 지점
		int[] end = {M - 1, M - 1}; // extendedLock 내부에서의 key의 종료 지점
		
		boolean canOpen = true;
		while (start[0] < N + M + M && start[1] < N + M + M) {
			canOpen = true; // 키가 움직이면 열 수 있다고 가정
			
			keyMove: for (int i = 0; i < N + M + M; i++) {
				for (int j = 0; j < N + M + M; j++) {
					int sum = extendedLock[i][j];
					if (i >= start[0] && i <= end[0] && j >= start[1] && j <= end[1]) {
						sum += key[i - start[0]][j - start[1]];
					}
					
					if (i >= M && i < M + N && j >= M && j < M + N && sum != 1) {
						canOpen = false; // 이 문장에 걸린적이 없으면 열 수 있다.
						break keyMove;
					}
				}
			}
			
			if (canOpen) {
				return true;
			}
			
			if (end[1] == N + M + M - 1) { // 이번 열의 끝까지 다 탐색했으면
				start[1] = 0; // 한 행 밑으로 내려서 확인
				end[1] = M - 1;
				start[0]++;
				end[0]++;
			} else {
				start[1]++;
				end[1]++;
			}
 		}
		
		return false;
	}

}
