# Algorithm Study

- [Visual Studio Code markdown preview](https://code.visualstudio.com/docs/languages/markdown)

  - Ctrl + Shift + V

- `다시 풀어볼 문제들`

---

## BaekJoon

> ### - BFS & DFS

- [1260 (DFS와 BFS)](https://www.acmicpc.net/problem/1260)  
  : dfs와 bfs를 구현하는 기본 문제

- [2178 (미로 탐색)](https://www.acmicpc.net/problem/2178)  
  : bfs를 이용한 미로찾기

- [2606 (바이러스)](https://www.acmicpc.net/problem/2606)  
  : dfs를 이용해 연결된 노드의 수 구하기

- [2667 (단지번호붙이기)](https://www.acmicpc.net/problem/2667)  
  : dfs를 이용해 2차원 행렬 내 1로 연결된 단지의 수, 각 단지 내의 1 개수 구하기

- [2644 (촌수계산)](https://www.acmicpc.net/problem/2644)  
  : bfs를 이용해 노드 간 최단거리 구하기

- [`7569 (토마토)`](https://www.acmicpc.net/problem/7569)  
  : bfs를 이용한 탐색 최소 시간 구하기  
  -> 메모리 제한 주의

- [7576 (토마토)](https://www.acmicpc.net/problem/7576)  
  : bfs를 이용한 탐색 최소 시간 구하기

- [`1697 (숨바꼭질)`](https://www.acmicpc.net/problem/1697)  
  : bfs를 이용한 탐색 최소 시간 구하기  
  -> 메모리, 시간 줄이는 방법 생각

- [5014 (스타트링크)](https://www.acmicpc.net/problem/5014)  
  : bfs를 이용한 탐색 최소 시간 구하기

- [2468 (안전 영역)](https://www.acmicpc.net/problem/2468)  
  : dfs를 이용해 행렬에서 섬 영역이 가장 많아질 때의 섬 영역 개수 구하기

- [10451 (순열 사이클)](https://www.acmicpc.net/problem/10451)  
  : dfs를 이용해 사이클의 개수 구하기

- [9466 (텀 프로젝트)](https://www.acmicpc.net/problem/9466)  
  : dfs를 이용해 팀에 속하지 않는 학생 수 구하기  
  -> 시간초과 주의

- [4963 (섬의 개수)](https://www.acmicpc.net/problem/4963)  
  : dfs를 이용해 섬의 개수 구하기

- [7576 (토마토)](https://www.acmicpc.net/problem/7576)  
  : bfs를 이용한 탐색 최소 시간 구하기  
  -> 시간초과 주의  
  -> 2021-05-19 재채점 결과 런타임 에러 발생으로 2021-05-20 재풀이

- [2146 (다리 만들기)](https://www.acmicpc.net/problem/2146)  
  : bfs를 이용한 섬과 섬을 잇는 최단 경로 구하기

- [5427 (불)](https://www.acmicpc.net/problem/5427)  
  : bfs를 이용해 불과 만나지 않는 탈출 경로 구하기  
  -> 다양한 테스트 케이스 실행 필요

- [1068 (트리)](https://www.acmicpc.net/problem/1068)  
  : dfs를 이용해 리프 노드 개수 구하기

- [`5719 (거의 최단 경로)`](https://www.acmicpc.net/problem/5719)  
  : 다익스트라 알고리즘과 bfs를 사용해 두 번째 최단 경로 구하기

- [`9205 (맥주 마시면서 걸어가기)`](https://www.acmicpc.net/problem/9205)  
  : bfs를 사용해 목적지까지 도착 가능 여부 찾기

- [`2573 (빙산)`](https://www.acmicpc.net/problem/2573)  
  : 빙산이 녹아서 분리되는 최초의 시간 구하기  
  -> 현재 python 시간초과로 pypy3 으로 제출

- [1012 (유기농 배추)](https://www.acmicpc.net/problem/1012)  
  : bfs나 dfs를 사용해 영역의 개수 구하기

- [11724 (연결 요소의 개수)](https://www.acmicpc.net/problem/11724)  
  : dfs를 사용해 연결된 요소 집합의 수 구하기  
  -> 간선에 연결되지 않은 노드도 하나의 집합으로 여긴다.

- [2583 (영역 구하기)](https://www.acmicpc.net/problem/2583)  
  : bfs를 사용해 영역의 수 구하기

- [`7562 (나이트의 이동)`](https://www.acmicpc.net/problem/7562)  
  : bfs를 이용해 목적지로 이동할 수 있는 최소 시간 구하기  
  `-> 목적지를 현재 위치의 가까이로 변경해 풀이 시간 단축 가능`

- [`9019 (DSLR)`](https://www.acmicpc.net/problem/9019)  
  : bfs를 이용해 4개의 연산을 통해 목적 숫자까지의 최소 연산 구하기  
  `-> pypy3로 제출, python3 시간초과`

- [10026 (적록색약)](https://www.acmicpc.net/problem/10026)  
  : dfs를 이용해 적록색약인 사람과 정상인이 구별한 색의 개수 구하기

- [1325 (효율적인 해킹)](https://www.acmicpc.net/problem/1325)  
  : bfs를 이용해 가장 많이 탐색 가능한 번호 구하기
  `-> pypy3로 제출, python3 시간초과, 비슷한 코드임에도 불구하고 시간초과 발생 원인 찾아보기`

- [`1967 (트리의 지름)`](https://www.acmicpc.net/problem/1967)  
  : dfs를 이용해 트리의 지름 구하기  
  `-> 아이디어 스스로 다시 생각해보기`
- [11725 (트리의 부모 찾기)](https://www.acmicpc.net/problem/11725)  
  : bfs를 이용해 연결된 노드들 중 부모 노드 찾기
- [2206 (벽 부수고 이동하기)](https://www.acmicpc.net/problem/2206)  
  : bfs를 이용해 최단 경로 구하기

- [`19238 (스타트 택시)`](https://www.acmicpc.net/problem/19238)  
  : bfs를 이용해 최단 경로 구하기
  -> 예외사항, 조건 제대로 확인 (첫 풀이 1시간 40분)
  -> 두번째 풀이 2시간

- [14466 (소가 길을 건너간 이유 6)](https://www.acmicpc.net/problem/14466)
- [20950 (미술가 미미)](https://www.acmicpc.net/problem/20950)
- [14503 (로봇 청소기)](https://www.acmicpc.net/problem/14503)
- [1726 (로봇)](https://www.acmicpc.net/problem/1726)
- [1707 (이분 그래프)](https://www.acmicpc.net/problem/1707)
- [`16234 (인구 이동)`](https://www.acmicpc.net/problem/16234)
  `-> 시간 최적화 스스로 다시 생각해보기`

> ### - Union Find

- [16562 (친구비)](https://www.acmicpc.net/problem/16562)  
  : union find를 이용해 최소 친구 비용 구하기

> ### - MST(Minimum Spanning Tree, 최소 신장 트리)

- [1922 (네트워크 연결)](https://www.acmicpc.net/problem/1922)  
  : 크루스칼(& Union Find)을 이용해 컴퓨터들을 연결하는 데 드는 최소 비용 구하기

- [6497 (전력난)](https://www.acmicpc.net/problem/6497)  
  : 프림 알고리즘을 이용해 도시들을 연결하는 최소 거리 구하기

> ### - Dijkstra

- [1753 (최단경로)](https://www.acmicpc.net/problem/1753)  
  : 기본 다익스트라 알고리즘

- [1916 (최소비용 구하기)](https://www.acmicpc.net/problem/1916)  
  : 기본 다익스트라 알고리즘

- [1238 (파티)](https://www.acmicpc.net/problem/1238)  
  : 다익스트라 알고리즘을 사용해 왕복 최단거리 중 가장 큰 값 찾기

- [`11779 (최소비용 구하기 2)`](https://www.acmicpc.net/problem/11779)  
  : 다익스트라 알고리즘을 사용해 최소 비용 경로 구하기

- [2211 (네트워크 복구)](https://www.acmicpc.net/problem/2211)  
  : 다익스트라 알고리즘을 사용해 1번 노드와 모든 노드와의 최소 비용 연결 경로 구하기

- [`5719 (거의 최단 경로)`](https://www.acmicpc.net/problem/5719)  
  : 다익스트라 알고리즘과 bfs를 사용해 두 번째 최단 경로 구하기

> ### - Floyd-Warshall

- [11404 (플로이드)](https://www.acmicpc.net/problem/11404)  
  : 모든 도시의 쌍에 대해 버스 비용의 최솟값 구하기

- [1956 (운동)](https://www.acmicpc.net/problem/1956)  
  : 최소 사이클의 길이의 합 구하기

> ### - Dynamic Programming

- [2839 (설탕 배달)](https://www.acmicpc.net/problem/2839)
- [1463 (1로 만들기)](https://www.acmicpc.net/problem/1463)
- [9095 (1, 2, 3 더하기)](https://www.acmicpc.net/problem/9095)
- [1003 (피보나치 함수)](https://www.acmicpc.net/problem/1003)
- [11726 (2xn 타일링)](https://www.acmicpc.net/problem/11726)
- [11053 (가장 긴 증가하는 부분 수열)](https://www.acmicpc.net/problem/11053)
- [3687 (성냥개비)](https://www.acmicpc.net/problem/3687)
- [2579 (계단 오르기)](https://www.acmicpc.net/problem/2579)
- [1904 (01타일)](https://www.acmicpc.net/problem/1904)
- [1932 (정수 삼각형)](https://www.acmicpc.net/problem/1932)
- [1912 (연속합)](https://www.acmicpc.net/problem/1912)
- [2156 (포도주 시식)](https://www.acmicpc.net/problem/2156)
- [`9251 (LCS)`](https://www.acmicpc.net/problem/9251)
- [1446 (지름길)](https://www.acmicpc.net/problem/1446)
- [2193 (이친수)](https://www.acmicpc.net/problem/2193)
- [10844 (쉬운 계단 수)](https://www.acmicpc.net/problem/10844)
- [`12865 (평범한 배낭)`](https://www.acmicpc.net/problem/12865)
- [11727 (2xn타일링2)](https://www.acmicpc.net/problem/11727)

> ### - Simulation

- [1244 (스위치 켜고 끄기)](https://www.acmicpc.net/problem/1244)

- [`19237 (어른 상어)`](https://www.acmicpc.net/problem/19237)  
  -> 첫 풀이 3:30

- [`19236 (청소년 상어)`](https://www.acmicpc.net/problem/19236)  
  -> `상어가 물고기가 없는 칸을 만났을 때 탐색을 멈추는 것이 아니라, 그 칸을 넘어서 만약 물고기가 있는 칸이 있다면 그 칸으로 넘어가면 된다`

- [16918 (봄버맨)](https://www.acmicpc.net/problem/16918)
- [`22860 (폴더 정리 (small))`](https://www.acmicpc.net/problem/22860)
- [`20055 (컨베이어 벨트 위의 로봇)`](https://www.acmicpc.net/problem/20055)
- [18442 (우체국 1)](https://www.acmicpc.net/problem/18442)
- [3190 (뱀)](https://www.acmicpc.net/problem/3190)
- [17135 (캐슬 디펜스)](https://www.acmicpc.net/problem/17135)
- [14499 (주사위 굴리기)](https://www.acmicpc.net/problem/14499)
- [12100 (2048 (Easy))](https://www.acmicpc.net/problem/12100)
- [15683 (감시)](https://www.acmicpc.net/problem/15683)
- [1966 (프린터 큐)](https://www.acmicpc.net/problem/1966)
- [14891 (톱니바퀴)](https://www.acmicpc.net/problem/14891)
- [`15685 (드래곤 커브)`](https://www.acmicpc.net/problem/15685)
- [1547 (공)](https://www.acmicpc.net/problem/1547)
- [13460 (구슬 탈출 2)](https://www.acmicpc.net/problem/13460)
- [15653 (구슬 탈출 4)](https://www.acmicpc.net/problem/15653)

> ### - Else

- [2331 (반복수열)](https://www.acmicpc.net/problem/2331)  
  : 특정 연산을 통해 반복되는 수를 제외한 나머지 수들 구하기

- [1000 (A+B)](https://www.acmicpc.net/problem/1000)  
  : 기본 입출력

- [1026 (보물)](https://www.acmicpc.net/problem/1026)  
  : 리스트 정렬로 두 리스트의 곱 중 최솟값 구하기

- [17478 (재귀함수가 뭔가요?)](https://www.acmicpc.net/problem/17478)  
  : 재귀함수를 이용한 문자열 출력

- [2493 (탑)](https://www.acmicpc.net/problem/2493)  
  : 스택

- [1158 (요세푸스 문제)](https://www.acmicpc.net/problem/1158)

- [`2491 (수열)`](https://www.acmicpc.net/problem/2491)  
  : DP로 다시 풀어볼 것

- [5430 (AC)](https://www.acmicpc.net/problem/5430)  
  : 스택

- [14719 (빗물)](https://www.acmicpc.net/problem/14719)  
  : 스택

- [11050 (이항 계수 1)](https://www.acmicpc.net/problem/11050)
- [2075 (N번째 큰 수)](https://www.acmicpc.net/problem/2075)
- [1662 (압축)](https://www.acmicpc.net/problem/1662)  
  : 스택

- [`14400 (편의점 2)`](https://www.acmicpc.net/problem/14400)
