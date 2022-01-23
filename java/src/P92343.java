import java.util.*;

public class P92343 {

    public static int nodeCount, maxSheepCount;
    public static int[] parents;
    public static ArrayList<Integer>[] childs;

    public static int[] depth = new int[2];

    public static void main(String[] args) {
        int answer = solution(new int[]{0, 1, 1, 0, 0, 1, 1, 0}, new int[][]{{0, 1}, {0, 2}, {1, 3}, {1, 4}, {2, 5}, {2, 6}, {3, 7}});
        int answer2 = solution(new int[]{0, 0, 1, 0, 1, 1, 0, 0}, new int[][]{{0, 1}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}});

        System.out.println(depth[0] + " " + depth[1] );
    }

    public static int solution(int[] info, int[][] edges) {
        // info: 각 노드(인덱스)에 위치한 동물 (0: 양, 1: 늑대)
        // edges: [[부모 노드, 자식 노드], ...]

        // 양의 수 > 늑대의 수 이어야한다
        // 양을 최대한 많이 모은다

        nodeCount = info.length;

        // parents: 각 노드의 부모 노드 번호를 저장
        // childs: 각 노드의 자식 노드 번호들을 저장
        parents = new int[nodeCount];
        childs = new ArrayList[nodeCount];

        for (int[] link : edges) {
            int parent = link[0];
            int child = link[1];

            if (childs[parent] == null) {
                childs[parent] = new ArrayList<>();
            }

            parents[child] = parent;
            childs[parent].add(child);
        }

        // 방문체크하기 위한 배열 (visited[x][y] : x node에 sheepCount가 y일 때 방문 여부)
        boolean[][] visited = new boolean[nodeCount][nodeCount + 1];
        getAnimal(1, 0, 0, info, visited);
        System.out.println(maxSheepCount);


        maxSheepCount = 0;
        List<Integer> nextNodes = new ArrayList<>();
        nextNodes.add(0);
        getAnimal2(0, 0, 0, nextNodes, info);
        System.out.println(maxSheepCount);

        return maxSheepCount;
    }

    // sheepCount: 양의 수, wolfCount: 늑대의 수, node: 현재 노드
    // animal: 동물들의 현재 상태(0: 양, 1: 늑대, -1: 이미 모아서 자리에 없음)
    public static void getAnimal(int sheepCount, int wolfCount, int node, int[] animal, boolean[][] visited) {
        depth[0]++;
        if (sheepCount <= wolfCount || visited[node][sheepCount]) {
            return;
        }

        int[] copied = getCopied(animal);

        visited[node][sheepCount] = true;
        copied[node] = -1;
        maxSheepCount = Math.max(maxSheepCount, sheepCount);

        // 부모 노드로 다시 돌아간다
        getAnimal(sheepCount, wolfCount, parents[node], copied, visited);

        if (childs[node] == null) {
            return;
        }

        for (int nextNode : childs[node]) { // 다음에 방문할 노드
            if (copied[nextNode] == 0) { // 양
                getAnimal(sheepCount + 1, wolfCount, nextNode, copied, visited);
            } else if (copied[nextNode] == 1) { // 늑대
                getAnimal(sheepCount, wolfCount + 1, nextNode, copied, visited);
            } else { // 이미 모아서 자리에 없음
                getAnimal(sheepCount, wolfCount, nextNode, copied, visited);
            }
        }
    }

    public static int[] getCopied(int[] target) {
        int[] copied = new int[target.length];

        for (int i = 0; i < target.length; i++) {
            copied[i] = target[i];
        }

        return copied;
    }


    public static void getAnimal2(int sheepCount, int wolfCount, int node, List nextNodes, int[] info) {
        depth[1]++;
        sheepCount += info[node] ^ 1;
        wolfCount += info[node];
        maxSheepCount = Math.max(maxSheepCount, sheepCount);

        if (sheepCount <= wolfCount) {
            return;
        }

        List<Integer> copied = new ArrayList<>();
        copied.addAll(nextNodes);
        if (childs[node] != null) {
            copied.addAll(childs[node]);
        }
        copied.remove(Integer.valueOf(node));

        for (int nextNode : copied) { // 다음에 방문할 노드
            getAnimal2(sheepCount, wolfCount, nextNode, copied, info);
        }
    }

}
