# Algorithm Study

알고리즘 문제 풀이입니다.

- 사용 언어
  - Python 3
  - Java 1.8
- 문제 출처
  - [BaekJoon](https://www.acmicpc.net)
  - [Programmers](https://programmers.co.kr/learn/challenges)
  - [SW Expert Academy](https://swexpertacademy.com/main/main.do)
  - [LeetCode](https://leetcode.com/problemset/all)

---

## Java Run

```
javac -encoding UTF-8 -d . [path\filename.java]
java [filename]
```

example

```
javac -encoding UTF-8 -d . .\SWExpertAcademy\SWEA1204.java
java SWEA1204
```

---

## [Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)

> ### List

|  Operation  |           Example            |    Big-O     |
| :---------: | :--------------------------: | :----------: |
|    Index    |             l[i]             |     O(1)     |
|    Store    |           l[i] = 0           |     O(1)     |
|   Length    |            len(l)            |     O(1)     |
|   Append    |         l.append(5)          |     O(1)     |
|     Pop     |           l.pop()            |     O(1)     |
|    Slice    |       list[start:end]        | O(end-start) |
|   Extend    |        l.extend(...)         | O(len(...))  |
|   Compare   |        list1 == list2        |     O(N)     |
|   Insert    | list.insert(location, value) |     O(N)     |
|   Delete    |       del list[index]        |     O(N)     |
|   Remove    |      list.remove(value)      |     O(N)     |
| Containment |        target in list        |     O(N)     |
|    Copy     |         list.copy()          |     O(N)     |
|    value    |    min(list) / max(list)     |     O(N)     |
|   Reverse   |        list.reverse()        |     O(N)     |
|    Sort     |         list.sort()          |   O(NlogN)   |

> ### Set

|   Operation    |    Example    |      Big-O       |
| :------------: | :-----------: | :--------------: |
|     Length     |    len(s)     |       O(1)       |
|      Add       |   s.add(5)    |       O(1)       |
|  Containment   | x in/not in s |       O(1)       |
|     Remove     | s.remove(..)  |       O(1)       |
|    Discard     | s.discard(..) |       O(1)       |
|      Pop       |    s.pop()    |       O(1)       |
|     Clear      |   s.clear()   |       O(1)       |
|  Construction  |   set(...)    |   O(len(...))    |
|  check ==, !=  |    s != t     |    O(len(s))     |
|      <=/<      |    s <= t     |    O(len(s))     |
|      >=/>      |    s >= t     |    O(len(t))     |
|     Union      |     s | t     | O(len(s)+len(t)) |
|  Intersection  |     s & t     | O(len(s)+len(t)) |
|   Difference   |     s - t     | O(len(s)+len(t)) |
| Symmetric Diff |     s ^ t     | O(len(s)+len(t)) |
|      Copy      |   s.copy()    |       O(N)       |

> ### Dictionary

|   Operation    |   Example   |    Big-O    |
| :------------: | :---------: | :---------: |
|     Index      |    d[k]     |    O(1)     |
|     Store      |  d[k] = v   |    O(1)     |
|     Length     |   len(d)    |    O(1)     |
|     Delete     |  del d[k]   |    O(1)     |
| get/setdefault |  d.get(k)   |    O(1)     |
|      Pop       |  d.pop(k)   |    O(1)     |
|    Pop item    | d.popitem() |    O(1)     |
|     Clear      |  d.clear()  |    O(1)     |
|      View      |  d.keys()   |    O(1)     |
|  Construction  |  dict(...)  | O(len(...)) |
