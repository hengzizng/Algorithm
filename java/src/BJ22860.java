import java.io.*;
import java.util.*;

public class BJ22860 {
    public static int N, M;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        //////
        String test = "4 1\n" +
                "main FolderA 1\n" +
                "FolderA FolderB 1\n" +
                "FolderB FolderC 1\n" +
                "FolderC FolderD 1\n" +
                "FolderD File1 0\n" +
                "3\n" +
                "main\n" +
                "main/FolderA\n" +
                "main/FolderA/FolderB/FolderC/FolderD";
        in = new BufferedReader(new StringReader(test));
        //////

        String[] tokens = in.readLine().split(" ");
        N = Integer.parseInt(tokens[0]) + 1; // main을 포함한 폴더의 총 개수
        M = Integer.parseInt(tokens[1]); // 파일의 총 개수

        List<Integer>[] children = new ArrayList[N]; // 각 폴더의 하위 폴더들을 저장
        Map<String, Integer> folderToInt = new HashMap<>(); // 폴더명 -> 고유 번호(0 ~ N) 변환 map
        Map<String, Integer> fileToInt = new HashMap<>(); // 파일명 -> 고유 번호(0 ~ M-1) 변환 map
        int folderNo = 0; // 폴더 고유 번호 (0 ~ N)
        int fileNo = 0; // 파일 고유 번호 (0 ~ M-1)

        int[][] fileCount = new int[N][M]; // fileCount[n][m]: n폴더 하위에 위치한 m파일의 개수

        for (int i = 0; i < N + M - 1; i++) { // N = N + 1로 두었기 때문에 1 뺴준다
            tokens = in.readLine().split(" ");
            String parent = tokens[0]; // 상위 폴더
            String child = tokens[1]; // 폴더 or 파일

            // folderToInt와 fileToInt에 넣어준다
            if (!folderToInt.containsKey(parent)) {
                folderToInt.put(parent, folderNo++);
            }

            if ("0".equals(tokens[2])) { // 파일
                if (!fileToInt.containsKey(child)) {
                    fileToInt.put(child, fileNo++);
                }

                fileCount[folderToInt.get(parent)][fileToInt.get(child)]++;
            } else { // 폴더
                if (!folderToInt.containsKey(child)) {
                    folderToInt.put(child, folderNo++);
                }

                if (children[folderToInt.get(parent)] == null) {
                    children[folderToInt.get(parent)] = new ArrayList<>();
                }
                children[folderToInt.get(parent)].add(folderToInt.get(child));
            }
        }

        // 출력 : 파일종류수 파일개수
        StringBuilder sb = new StringBuilder();
        int Q = Integer.parseInt(in.readLine()); // 쿼리의 개수
        for (int q = 0; q < Q; q++) {
            tokens = in.readLine().split("/");
            // 폴더는 중복값이 없는 유일값이기 때문에 경로 없이 가장 마지막 폴더만 알고 있어도 된다
            int targetFolder = folderToInt.get(tokens[tokens.length - 1]);

            // totalCountByFolder[m]: targetFolder 하위에 있는 m파일의 총 개수
            int[] totalCountByFolder = new int[M];
            // 현재 targetFolder 내에 있는 파일의 개수를 더해준다
            for (int j = 0; j < M; j++) {
                totalCountByFolder[j] = fileCount[targetFolder][j];
            }
            // targetFolder 하위에 있는 폴더 내에 있는 파일의 개수를 더해준다
            getFileCount(targetFolder, children, totalCountByFolder, fileCount);

            // kindCount: 종류의 수, allCount: 모든 파일 개수
            int kindCount = 0, allCount = 0;
            for (int j = 0; j < M; j++) {
                if (totalCountByFolder[j] > 0) {
                    kindCount++;
                    allCount += totalCountByFolder[j];
                }
            }

            sb.append(kindCount).append(" ").append(allCount).append("\n");
        }

        System.out.println(sb.toString());
    }

    public static void getFileCount(int nowFolder, List<Integer>[] children, int[] fileCountSum, int[][] fileCount) {
        if (children[nowFolder] == null) {
            return;
        }

        for (int childFolder : children[nowFolder]) {
            for (int file = 0; file < M; file++) {
                fileCountSum[file] += fileCount[childFolder][file];
            }
            getFileCount(childFolder, children, fileCountSum, fileCount);
        }
    }

}
