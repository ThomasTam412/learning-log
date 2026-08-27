# Python vs C++ / PHP — 給有底子的人

> **建議存放：** `learning-log/python/notes/2026-08-27-python-vs-cpp-php.md`
> **日期：** 2026-08-27（Q1 Day 1）
> **前提：** 已識 C++ / PHP，只記差異，唔重複講變數迴圈函數

---

## 一、語法對照速查

| 概念 | C++ / PHP | Python |
|---|---|---|
| 區塊 | `{ }` | **縮排**（4 空格，語法一部分） |
| 語句結尾 | `;` | 冇 |
| 變數宣告 | `int x = 5;` / `$x = 5;` | `x = 5` |
| 註解 | `//` `/* */` | `#` `""" """` |
| 字串連接 | `.` / `+` | `+` 或 **f-string** |
| null | `nullptr` / `null` | `None` |
| bool | `true` / `false` | **`True` / `False`**（大寫） |
| 嚴格相等 | `===` | `==`（Python 冇型別雜耍） |
| 身分比較 | 比較 pointer | `is` |
| 陣列 | `vector` / PHP array | `list` `[]` |
| 不可變陣列 | `const array` | `tuple` `()` |
| 關聯陣列 | `map` / PHP array | `dict` `{}` |
| 集合 | `set` | `set` `{}` |
| this | `this` / `$this` | **`self`（要明寫做參數）** |
| 私有 | `private` | `_name`（**約定，唔強制**） |
| 邏輯運算 | `&&` `\|\|` `!` | `and` `or` `not` |
| 三元 | `a ? b : c` | `b if a else c`（順序唔同！） |
| 自增 | `i++` | `i += 1`（**冇 `++`**） |
| 印嘢 | `cout` / `echo` | `print()` |

---

## 二、⚠️ 三個一定會咬你嘅陷阱

### 陷阱 1：縮排係語法

```python
if x > 0:
    print("正")
    print("數")      # 同一個 block
print("完")          # block 外
```

**冇 `{}`。打錯一格 = 邏輯錯，而且唔一定報錯。**

⚠️ **絕對唔好撈亂 Tab 同空格。**
```json
// VS Code settings
"editor.insertSpaces": true,
"editor.tabSize": 4
```

### 陷阱 2：`self` 要明寫

```python
class Todo:
    def __init__(self, title):      # ← self 要寫
        self.title = title

    def toggle(self):                # ← 每個 method 都要
        self.done = not self.done

t = Todo("買嘢")
t.toggle()                           # ← 但 call 唔使傳
```

PHP 嘅 `$this` 隱形，Python 嘅 `self` 要明寫做第一個參數。

### 陷阱 3：冇 `===`，但有 `is`

```python
"1" == 1          # False  ← Python 唔做型別雜耍，== 已經夠嚴格
```

**你 PHP 嘅 `===` 鐵律喺 Python 唔適用。**

但要分清：
```python
a = [1, 2]
b = [1, 2]
a == b            # True   內容一樣
a is b            # False  唔係同一個 object（比較記憶體位置）
```

> **`is` 只用喺 `x is None`。** 其他情況一律 `==`。

---

## 三、五個必練 Pythonic 寫法

### 1. f-string

```python
name = "Thomas"
print(f"Hello, {name}")
print(f"平均 {avg:.2f}")           # 保留 2 位小數
print(f"{x:>10}")                   # 右對齊寬度 10
print(f"{n:,}")                     # 千分位 1,234,567
print(f"{val=}")                    # debug 神器：印出 val=5
```

### 2. List Comprehension

```python
squares = [x * x for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
scores = [s["score"] for s in students]      # ← PHP 嘅 array_column
```

**取代 90% 嘅簡單 for loop。**

**Generator expression**（冇 `[]`）—— 唔建立 list，逐個計逐個掉，省記憶體：
```python
total = sum(s["score"] for s in students)
```

### 3. 解包

```python
a, b = 1, 2
a, b = b, a                # 交換，唔使 temp

first, *rest = [1, 2, 3, 4]   # first=1, rest=[2,3,4]

for i, item in enumerate(items):     # index + 值
    ...

for name, score in zip(names, scores):   # 兩個 list 併行
    ...
```

### 4. `dict.get()`

```python
d.get("email")                # 冇就 None
d.get("email", "冇填")         # ← PHP 嘅 $d["email"] ?? "冇填"
```

⚠️ `d["email"]` 唔存在會 **KeyError**（唔似 PHP 只出 warning）。

### 5. `with` — Context Manager

```python
with open("data.csv") as f:
    content = f.read()
# 自動閂檔案，就算中途出 exception 都會閂
```

**取代 PHP 嘅 `fopen` / `fclose` 手動配對。**

---

## 四、Truthy / Falsy（同 PHP 唔同！）

```python
# Falsy
False, None, 0, 0.0, "", [], {}, (), set()

# 其他全部 Truthy
```

⚠️ **同 PHP 嘅重大差異：**

| 值 | PHP | Python |
|---|---|---|
| `"0"` | **false** | **True**（非空字串） |
| `"false"` | true | True |
| `[]` | false | False |
| `"0.0"` | true | True |

**PHP 嘅 `"0"` 係 falsy，Python 唔係。** 呢個係轉語言時最易中招嘅位。

慣用寫法：
```python
if not students:        # 空 list → 進入
if students:            # 有嘢 → 進入
```

Python 社群傾向用呢個，唔似你 PHP 寫 `count($x) === 0`。**語言慣例唔同，唔係對錯。**

---

## 五、PEP 8 命名規範

**PSR-12 之於 PHP = PEP 8 之於 Python**

| 類型 | 風格 | 例 |
|---|---|---|
| 函數 / 變數 | `snake_case` | `print_students` `avg_score` |
| 類別 | `PascalCase` | `Student` `TodoList` |
| 常數 | `UPPER_CASE` | `MAX_SCORE` |
| 私有（約定） | `_leading_underscore` | `_internal_helper` |

**其他規則：**
- 縮排 4 空格
- 頂層 function / class 之間**空兩行**
- Class 內 method 之間空一行
- `->` 前後有空格：`def f() -> int:`
- 行長度上限 79（PEP 8）或 88（Black formatter，業界較常用）

⚠️ **唔好用 camelCase**（`printStudents`）—— 一睇就知係 Java/JS 轉過嚟。

---

## 六、Type Hints

```python
def get_avg(students: list[dict]) -> float:
    ...

def find(id: int) -> Todo | None:      # PHP 嘅 ?Todo
    ...

name: str = "Thomas"
scores: list[int] = [90, 85]
config: dict[str, int] = {"a": 1}
```

| PHP | Python |
|---|---|
| `?Todo` | `Todo \| None`（3.10+） |
| `void` | `-> None` |
| `array` | `list` / `dict` / `tuple` |
| `mixed` | `Any`（`from typing import Any`） |

⚠️ **Python 唔會執行期強制檢查**（純提示）。想真檢查要裝 `mypy`。

**但照樣要寫** —— IDE autocomplete、其他人睇得明、你自己一個月後睇得明。

---

## 七、⚠️ 唔好覆蓋內建名

```python
sum = 0          # ❌ 覆蓋咗內建 sum()
list = [1,2]     # ❌
```

**常見要避開：**
`sum` `list` `dict` `str` `int` `type` `id` `max` `min` `input` `next` `filter` `map` `object` `bytes` `range`

💡 **VS Code 會將內建名顯示成特別顏色** —— 見到變數名有色 = 撞咗。

---

## 八、常用內建函數

```python
len(x)                    # 長度
sum(iterable)             # 加總
max(x) / min(x)           # ⚠️ 空 list 會 ValueError
sorted(x)                 # 回傳新 list（唔改原本）
x.sort()                  # 改原本（回傳 None）
reversed(x)
any(...) / all(...)       # 任一真 / 全部真
range(n) / range(a, b)
enumerate(x)
zip(a, b)
isinstance(x, int)
```

⚠️ **`sorted()` vs `.sort()`** —— 同你 PHP 學嘅「改嘢 vs 計嘢」一樣：
```python
new = sorted(old)      # 計一個新嘅出嚟
old.sort()             # 改原本，回傳 None
x = old.sort()         # ❌ x 會係 None
```

---

## 九、今日練習成果

`day01_students.py`

```python
students = [
    {"name": "thomas", "score": 100},
    {"name": "alice", "score": 99},
    {"name": "bob", "score": 98},
    {"name": "tom", "score": 97},
    {"name": "timi", "score": 100},
]


def print_students(students: list[dict]) -> None:
    if not students:
        print("暫無學生資料")
        return                          # ← guard clause 要早退

    for student in students:
        name = student["name"]
        score = student["score"]
        print(f"Student: {name}, {score}分")


def get_avg(students: list[dict]) -> float | None:
    if not students:
        return None                     # ← 唔好回傳 0（magic number）

    scores = [s["score"] for s in students]
    return sum(scores) / len(scores)


print_students(students)

avg = get_avg(students)
print(f"平均分: {avg:.2f}")

above_avg = [s for s in students if s["score"] > avg]
print_students(above_avg)
```

### 今日撞過嘅問題

| 問題 | 教訓 |
|---|---|
| `sum = 0` 覆蓋內建 | 唔好用內建名做變數 |
| 用 for loop 加總 | `sum([...])` 一行搞掂 |
| `printStudents` | PEP 8 用 snake_case |
| Guard 冇 `return` | Guard clause = 早退 |
| `f"冇 placeholder"` | 冇 `{}` 就唔使 `f` |
| `)->float` | `->` 前後要空格 |
| 空 list 回傳 `0` | `0` ≠「唔存在」，用 `None` |

### 一個未解決嘅設計問題

`get_avg([])` 應該點？

1. `return None` — caller 要處理
2. **`raise ValueError("學生名單為空")`** — caller 用錯咗，應該即刻知
3. `return 0` — ❌ 誤導

**真實 project 傾向 2。** 呢個同 PHP 嘅 `?int $id` 係同一個概念：唔好用正常值扮「唔存在」。

---

## 十、環境備忘

```bash
# 建 venv
python -m venv .venv

# 啟動（Git Bash）
source .venv/Scripts/activate

# 確認
pip list                        # 應該只有 pip
python --version                # 3.14.3
where python                    # CMD；Git Bash 用 which python
```

⚠️ **概念：** `.venv` 唔係「資料夾範圍」，係「一個獨立嘅 python.exe + 佢自己嘅套件庫」。
`.py` 檔冇歸屬，係**「用邊個 python 執行」**決定。

只有**第三方套件**跟 venv 走；標準庫（`csv` `json` `os`）每個 Python 都有。

驗證用邊個 python：
```python
import sys
print(sys.executable)
```

⚠️ **Code Runner extension 唔會用你揀嘅 venv interpreter** —— 用 VS Code 內建嘅 `Run Python File`。

---

## 📌 Exit Code

```
exited with code=0     成功（Unix 慣例：0 = 冇錯）
exited with code=1     一般錯誤（未捕捉嘅 exception）
```

Shell 可以用：
```bash
python script.py && echo "成功"     # 只有 exit 0 先行右邊
```

CI/CD 就係靠呢個判斷測試過唔過。

---

## 🔜 下一步（Day 2）

- MIT Missing Semester Lecture 1-2（Shell）
- 每個指令喺 Git Bash 真係打一次

## 之後要學（Q1 內）

```
class / OOP（對比 PHP 嘅 class）
exception（try / except / raise）
模組同 import
標準庫：pathlib / json / csv / datetime / collections
decorator（@ 語法）
generator（yield）
```
