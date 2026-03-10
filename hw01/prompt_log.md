# AI 交互日志 (Prompt Log)

> **工具**：Claude (claude.ai)  
> **任务**：用 AI 辅助实现 N 皇后问题求解器，包括工程初始化、逻辑实现、单元测试与 Bug 修复

---

## 第一轮 — 工程初始化

### 我的 Prompt
```
我完全零基础，请帮我初始化一个标准 Python 工程，要求：
1. 包含 src/ 源码目录与 tests/ 测试目录
2. 项目名称是 hw01，用来解决八皇后问题
3. 告诉我需要哪些文件
```

### Claude 的回复
规划了工程结构：src/queens.py 放主逻辑，tests/test_queens.py 放测试，
requirements.txt 记录依赖 pytest，并解释了 __init__.py 的作用。

---

## 第二轮 — 实现八皇后算法

### 我的 Prompt
```
请用回溯算法实现 N 皇后问题的求解函数 solve_n_queens(n)，
要求返回所有解，每个解用列表表示（solution[row]=col），请加中文注释。
```

### Claude 生成的初始代码（含 Bug）

is_safe 函数中对角线检测写错了：
```python
# ⚠️ 错误版本
if abs(prev_col - col) == abs(prev_row - row) + 1:
```

---

## 第三轮 — 编写单元测试

### 我的 Prompt
```
请为 solve_n_queens 编写完整的 pytest 单元测试，要求：
1. 测试 N=4 时解的数量是否为 2
2. 测试 N=8 时解的数量是否为 92
3. 测试每个解是否真正合法（没有皇后互相攻击）
```

---

## 第四轮 — 发现并修复 Bug

### 测试失败日志
```
FAILED tests/test_queens.py::TestSolutionCount::test_n4
AssertionError: assert 4 == 2
```

### 我发给 Claude 的 Prompt
```
运行测试出现错误，N=4 应该只有 2 个解，但代码返回了 4 个。
说明有些本应冲突的皇后摆放没有被正确排除，请检查 is_safe 函数。
```

### Claude 的诊断
> 对角线冲突条件多了 +1，正确条件是行差**等于**列差，去掉 +1 即可。

### 修复对比
```python
# ❌ Bug 版本
if abs(prev_col - col) == abs(prev_row - row) + 1:

# ✅ 修复版本
if abs(prev_col - col) == abs(prev_row - row):
```

修复后全部 16 个测试通过 ✅

---

## 第五轮 — 代码重构

### 我的 Prompt
```
代码能正确运行了，请帮我：
1. 添加完整的 docstring 注释（含 Args、Returns、Example）
2. 添加 format_board 函数用于可视化棋盘
3. 添加 if __name__ == "__main__" 演示入口
```

Claude 将代码重构为专业风格，加入类型注解、标准文档字符串和可视化函数。

---

## 总结：AI 辅助编程的关键经验

| 阶段 | 有效的 Prompt 策略 |
|------|-----------------|
| 需求描述 | 说清楚输入输出格式 |
| Bug 修复 | 把完整错误日志发给 AI |
| 代码质量 | 明确要求具体改进点 |
| 测试用例 | 提供已知正确答案作为验证基准 |

> 核心体会：AI 生成的代码必须配合测试用例验证，测试失败时把错误日志直接给 AI，它能快速定位 Bug。
```

---

## 文件 6：`hw01/requirements.txt`
```
pytest>=7.0.0
