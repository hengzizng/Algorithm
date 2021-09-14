# Algorithm Study

-   [Visual Studio Code markdown preview](https://code.visualstudio.com/docs/languages/markdown)

    -   Ctrl + Shift + V

-   `다시 풀어볼 문제들`

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

-   [reference blog](https://wayhome25.github.io/python/2017/06/14/time-complexity/)

> ### List

|   Operation   |    Big-O     |           Example            |
| :-----------: | :----------: | :--------------------------: |
|     Slice     | O(end-start) |       list[start:end]        |
|    Compare    |     O(N)     |        list1 == list2        |
|    Insert     |     O(N)     | list.insert(location, value) |
|    Delete     |     O(N)     |       del list[index]        |
|    Remove     |     O(N)     |      list.remove(value)      |
|  Containment  |     O(N)     |        target in list        |
|     Copy      |     O(N)     |         list.copy()          |
| Extreme value |     O(N)     |    min(list) / max(list)     |
|    Reverse    |     O(N)     |        list.reverse()        |
|     Sort      |   O(NlogN)   |         list.sort()          |

---
