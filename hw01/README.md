# hw01 — N-Queens Solver（八皇后问题求解器）

> 本项目使用 **回溯算法（Backtracking）** 求解 N 皇后问题，由 AI（Claude）辅助完成代码编写、Bug 修复与单元测试。

---

## 📁 项目结构
```
hw01/
├── src/
│   ├── __init__.py
│   └── queens.py          # N 皇后求解器核心逻辑
├── tests/
│   └── test_queens.py     # 单元测试（pytest）
├── prompt_log.md          # AI 交互日志（本项目重点）
├── requirements.txt       # 依赖列表
└── README.md              # 本文件
```

---

## 🧠 实现思路

### 算法：回溯法（Backtracking）

逐行放置皇后，每放一个皇后前先检查是否与已放置的皇后冲突，若冲突则跳过，若所有列均冲突则回退到上一行重新选择。

**冲突检测（`is_safe` 函数）**：
- **同列冲突**：`board[prev_row] == col`
- **对角线冲突**：`abs(board[prev_row] - col) == abs(prev_row - row)`

---

## 🚀 运行方式

### 安装依赖
```bash
pip install -r requirements.txt
```

### 直接运行求解器
```bash
python src/queens.py
```

### 运行单元测试
```bash
pytest tests/ -v
```

---

## ✅ 已验证结果

| N | 解的数量 |
|---|---------|
| 1 | 1       |
| 2 | 0       |
| 3 | 0       |
| 4 | **2**   |
| 5 | 10      |
| 6 | 4       |
| 7 | 40      |
| 8 | **92**  |

---

## 🐛 Bug 修复记录

开发过程中 AI 生成的初始代码存在对角线冲突检测的 Bug，详见 `prompt_log.md`。

- **Bug 位置**：`src/queens.py` → `is_safe()` 函数
- **Bug 原因**：对角线条件多写了 `+1`，导致 N=4 返回 4 个解而非 2 个
- **修复方法**：将 `== abs(prev_row - row) + 1` 改为 `== abs(prev_row - row)`
