import java.util.HashSet;


class Solution {
    static int[] networks;
    
    public int find(int target) {
        while(target != networks[target]) {
            networks[target] = networks[networks[target]];
            target = networks[target];
        }
        
        return target;
    }
    
    public void union(int computer1, int computer2) {
        computer1 = find(computer1);
        computer2 = find(computer2);
        
        if(computer1 < computer2) {
            networks[computer2] = computer1;
        } else {
            networks[computer1] = computer2;
        }
    }
    
    public int solution(int n, int[][] computers) {
        HashSet<Integer> set = new HashSet<>();
        networks = new int[n];
        
        for(int i=0; i<n; i++) {
            networks[i] = i;
        }
        
        for(int row=0; row<n; row++) {
            for(int col=row+1; col<n; col++) {
                if(computers[row][col] == 1) {
                    union(row, col);
                }
            }
        }
        
        for(int i=0; i<n; i++) {
            networks[i] = find(i);
            set.add(networks[i]);
        }
        
        return set.size();
    }
}