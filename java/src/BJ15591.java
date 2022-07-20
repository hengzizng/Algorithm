import java.io.*;
import java.util.*;

public class BJ15591 {
    public static int N, Q;
    public static List<int[]>[] graph;

    public static void main(String[] args) throws Exception {
        // USADO: 두 동영상 사이의 값들 중 최솟값
        // K 이상의 동영상의 개수

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        ////// test
        String test = "4 3\n" + "1 2 3\n" + "2 3 2\n" + "2 4 4\n" + "1 2\n" + "4 1\n" + "3 1";
        in = new BufferedReader(new StringReader(test));
        ////// test

        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        N = Integer.parseInt(st.nextToken()); // 동영상 수
        Q = Integer.parseInt(st.nextToken()); // 농부의 질문 수 (출력 개수)

        graph = new List[N]; // graph[동영상][0]: 연결된 동영상, graph[동영상][1]: USADO
        int[][] usado = new int[N][N];
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(in.readLine(), " ");
            // 동영상 p, q가 USADO r로 서로 연결되어 있다.
            int p = Integer.parseInt(st.nextToken()) - 1;
            int q = Integer.parseInt(st.nextToken()) - 1;
            int r = Integer.parseInt(st.nextToken());

            if (graph[p] == null) {
                graph[p] = new ArrayList();
            }
            if (graph[q] == null) {
                graph[q] = new ArrayList();
            }
            graph[p].add(new int[]{q, r});
            graph[q].add(new int[]{p, r});
        }

        for (int video = 0; video < N; video++) {
            usado[video] = getUsado(video);
//            for (int i = 0; i < N; i++) {
//                System.out.print(usado[video][i] + " ");
//            }
//            System.out.println();
        }

        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(in.readLine(), " ");

            int k = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken()) - 1;

            int count = 0;
            for (int video = 0; video < N; video++) {
                if (usado[v][video] >= k) {
                    count++;
                }
            }
            System.out.println(count);
        }
    }

    public static int[] getUsado(int target) {
        Queue<int[]> queue = new LinkedList<>(); // BFS를 위한 큐 [동영상 번호, 경로 중 최솟값]
        int[] usado = new int[N]; // targeet에 대한 USADO

        queue.offer(new int[]{target, 1000000000});

        while (!queue.isEmpty()) {
            int[] nowVideo = queue.poll();

            for (int[] nextVideo : graph[nowVideo[0]]) {
                // nextVideo: {연결된 동영상, USADO}
                if (usado[nextVideo[0]] == 0 && nextVideo[0] != target) {
                    int minValue = Math.min(nowVideo[1], nextVideo[1]);
                    queue.offer(new int[]{nextVideo[0], minValue});
                    usado[nextVideo[0]] = minValue;
                }
            }
        }

        return usado;
    }
}
