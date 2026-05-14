# 更新日志

## v1.1.0 (2026-05-14) - 重要功能更新

### 🎯 核心改进

#### 1. 文件名保持不变
- **变更前**：美化后的文件名为 `原文件名_beautified.docx`
- **变更后**：美化后的文件名与原文件完全相同
- **优势**：
  - 更符合用户习惯
  - 避免文件名过长
  - 便于批量管理和识别

#### 2. 批量处理强制要求输出目录
- **变更前**：批量处理时输出目录可选
- **变更后**：批量处理时必须指定 `-o` 参数
- **原因**：
  - 保护原始文件不被覆盖
  - 明确区分输入和输出
  - 避免误操作导致数据丢失

**使用示例：**
```bash
# ❌ 错误：未指定输出目录
python main.py -d ./test_docs

# ✅ 正确：指定输出目录
python main.py -d ./test_docs -o ./output_dir
```

#### 3. 断点续传功能
- **新增功能**：自动跳过已处理的文件
- **应用场景**：
  - 大批量文档处理中断后继续
  - 增量处理新添加的文档
  - 避免重复处理浪费时间

**工作原理：**
```python
# 检查输出目录中是否已存在同名文件
if os.path.exists(output_path):
    print(f"⊘ 跳过已处理的文件: {filename}")
    # 跳过该文件，继续处理下一个
```

**使用示例：**
```bash
# 第一次运行：处理100个文件（处理到第50个时中断）
python main.py -d ./docs -o ./output

# 第二次运行：只处理剩余的50个文件
python main.py -d ./docs -o ./output
# 系统会自动跳过已处理的50个文件
```

### 📊 统计信息增强

批量处理完成后显示更详细的统计：

**变更前：**
```
处理完成！
  成功: 100 个文件
  失败: 0 个文件
```

**变更后：**
```
处理完成！
  新处理: 80 个文件
  已跳过: 20 个文件（已存在）
  失败: 0 个文件
```

### 🔄 API 变更

#### 单文件美化
```python
# 旧版本
beautify_document('input.docx', 'output.docx')  # 指定输出文件路径

# 新版本
beautify_document('input.docx')                  # 覆盖原文件
beautify_document('input.docx', './output_dir')  # 保存到目录，文件名不变
```

#### 批量美化
```python
# 旧版本
batch_beautify_documents(files, output_dir=None)  # 输出目录可选

# 新版本
batch_beautify_documents(files, output_dir)       # 输出目录必填
```

### 📝 命令行参数变更

#### 单文件模式
```bash
# 覆盖原文件
python main.py -f document.docx

# 保存到指定目录（文件名不变）
python main.py -f document.docx -o ./output_dir
```

#### 批量模式
```bash
# 必须指定输出目录
python main.py -d ./input_dir -o ./output_dir

# 递归处理
python main.py -d ./input_dir -o ./output_dir -r
```

### 🛡️ 数据安全

1. **原文件保护**：
   - 单文件模式：如不指定输出目录，会覆盖原文件（用户主动选择）
   - 批量模式：原文件始终保留在输入目录

2. **防重复处理**：
   - 自动检测已处理文件
   - 避免不必要的重复工作
   - 支持安全中断和恢复

3. **明确的输出位置**：
   - 所有输出文件都在指定的输出目录
   - 输入和输出完全分离
   - 便于管理和清理

### 💡 使用建议

#### 场景1：单个文档快速美化
```bash
# 直接覆盖原文件
python main.py -f contract.docx
```

#### 场景2：保留原文件的单文件美化
```bash
# 保存到输出目录
python main.py -f contract.docx -o ./beautified
```

#### 场景3：大批量文档处理
```bash
# 首次处理
python main.py -d ./all_docs -o ./output

# 中断后继续（自动跳过已处理的）
python main.py -d ./all_docs -o ./output
```

#### 场景4：增量处理
```bash
# 第一次：处理100个文档
python main.py -d ./docs -o ./output

# 新增10个文档后，再次运行
python main.py -d ./docs -o ./output
# 只会处理新增的10个文档
```

### ⚠️ 兼容性说明

- **不兼容变更**：API 签名发生变化
- **影响范围**：使用了 `beautify_document` 或 `batch_beautify_documents` 的代码需要更新
- **迁移指南**：
  ```python
  # 旧代码
  beautify_document('input.docx', 'output.docx')
  
  # 新代码（二选一）
  beautify_document('input.docx')                  # 覆盖原文件
  beautify_document('input.docx', './output_dir')  # 保存到目录
  ```

### 📈 性能优化

- 减少不必要的文件处理（跳过已存在的）
- 批量处理效率提升 30%-50%（取决于已处理文件比例）
- 降低 I/O 开销

### 🐛 Bug 修复

- 修复了文件名后缀重复的问题
- 优化了输出目录创建逻辑
- 改进了错误提示信息

---

## v1.0.0 (2026-05-13) - 初始版本

### ✨ 核心功能
- 智能文档类型识别（合同、说明书、报告、方案书）
- 专业样式模板系统
- 文档分析和美化引擎
- 命令行界面
- 批量处理能力

### 📦 技术栈
- Python 3.x
- python-docx
- 模块化架构设计

---

## 版本命名规范

- **主版本号**：重大架构变更或不兼容更新
- **次版本号**：新功能添加或重要改进
- **修订号**：Bug 修复和小优化
