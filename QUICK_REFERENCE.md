# DOCX文档美化系统 - 快速参考

## 📌 核心命令

### 单文件处理
```bash
# 覆盖原文件
python main.py -f document.docx

# 保存到输出目录（文件名不变）
python main.py -f document.docx -o ./output_dir
```

### 批量处理
```bash
# 必须指定输出目录
python main.py -d ./input_dir -o ./output_dir

# 递归处理子目录
python main.py -d ./input_dir -o ./output_dir -r
```

### 其他命令
```bash
# 查看支持的类型
python main.py --types

# 创建测试文档
python test_create_sample.py
```

## 🎯 关键特性

### ✅ 文件名保持不变
- 输入：`合同.docx`
- 输出：`合同.docx`（不是 `合同_beautified.docx`）

### ✅ 原文件保护
- **单文件模式**：不指定 `-o` 时覆盖原文件
- **批量模式**：原文件始终保留，必须指定 `-o`

### ✅ 断点续传
```bash
# 第一次运行：处理100个文件
python main.py -d ./docs -o ./output

# 中断后继续：自动跳过已处理的
python main.py -d ./docs -o ./output
```

## 📋 参数说明

| 参数 | 说明 | 单文件 | 批量 |
|------|------|--------|------|
| `-f` | 输入文件 | ✅ 必填 | ❌ |
| `-d` | 输入目录 | ❌ | ✅ 必填 |
| `-o` | 输出目录 | ⚠️ 可选 | ✅ 必填 |
| `-r` | 递归查找 | ❌ | ✅ 可选 |
| `--types` | 显示类型 | ✅ | ✅ |

## 💡 使用场景

### 场景1：快速美化单个文档
```bash
python main.py -f contract.docx
# 结果：contract.docx 被美化（覆盖原文件）
```

### 场景2：保留原文件
```bash
python main.py -f contract.docx -o ./beautified
# 结果：
#   - 原文件：contract.docx（未修改）
#   - 美化文件：./beautified/contract.docx
```

### 场景3：批量处理
```bash
python main.py -d ./contracts -o ./beautified_contracts
# 结果：
#   - 原文件保留在：./contracts/
#   - 美化文件保存到：./beautified_contracts/
```

### 场景4：大批量+断点续传
```bash
# 处理1000个文档（可能耗时较长）
python main.py -d ./all_docs -o ./output

# 如果中断，再次运行即可继续
python main.py -d ./all_docs -o ./output
# 自动跳过已处理的文件
```

## 🔍 输出示例

### 单文件成功
```
美化成功！
输入文件: contract.docx
输出文件: ./output/contract.docx
保存位置: 输出目录 (./output)
文档类型: contract
置信度: 94.00%
```

### 批量处理完成
```
处理完成！
  新处理: 80 个文件
  已跳过: 20 个文件（已存在）
  失败: 0 个文件
```

## ⚠️ 注意事项

1. **批量处理必须指定 `-o`**
   ```bash
   # ❌ 错误
   python main.py -d ./docs
   
   # ✅ 正确
   python main.py -d ./docs -o ./output
   ```

2. **文件名保持不变**
   - 不会有 `_beautified` 后缀
   - 输出目录中的文件名与输入完全相同

3. **断点续传自动生效**
   - 无需额外参数
   - 系统自动检测已存在的文件

4. **原文件安全**
   - 批量模式：原文件始终保留
   - 单文件模式：不指定 `-o` 会覆盖原文件

## 🎨 支持的文档类型

| 类型 | 关键词示例 | 样式特点 |
|------|-----------|----------|
| contract | 甲方、乙方、合同、协议 | 宋体、首行缩进、正式 |
| manual | 步骤、注意、参数、说明 | 微软雅黑、清晰、现代 |
| report | 摘要、结论、分析、报告 | 宋体、学术规范 |
| proposal | 方案、预算、计划、实施 | 微软雅黑、商务风格 |

## 🚀 Python API

```python
from core.beautifier import beautify_document, batch_beautify_documents

# 单文件
result = beautify_document('input.docx')
result = beautify_document('input.docx', './output_dir')

# 批量
files = ['doc1.docx', 'doc2.docx']
results = batch_beautify_documents(files, './output_dir')

# 检查结果
if result['success']:
    print(f"类型: {result['doc_type']}")
    print(f"文件: {result['output_path']}")
```

## 📞 常见问题

**Q: 如何恢复原文件？**
A: 批量模式下原文件始终保留。单文件模式如覆盖了原文件，需要手动备份。

**Q: 可以自定义输出文件名吗？**
A: 当前版本保持文件名不变。如需自定义，可在处理后手动重命名。

**Q: 断点续传如何工作？**
A: 系统检查输出目录中是否存在同名文件，存在则跳过。

**Q: 如何处理新增的文档？**
A: 直接再次运行批量命令，系统会自动跳过已处理的文件。

---

**提示**：更多详细信息请查看 [README.md](README.md) 和 [CHANGELOG.md](CHANGELOG.md)
