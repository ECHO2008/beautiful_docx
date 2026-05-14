# DOCX文档智能美化系统

一个基于Python的智能DOCX文档美化工具，能够自动识别文档类型并应用专业的排版样式。

## 功能特点

- 🎯 **智能文档分类**：自动识别合同、说明书、报告、方案书等文档类型
- 🎨 **专业样式模板**：为每种文档类型预设专业的排版格式
- 📊 **结构分析**：深度分析文档结构和内容特征
- 🔄 **批量处理**：支持单个或批量文档美化
- 🔧 **高度可扩展**：易于添加新的文档类型和样式模板

## 支持的文档类型

| 类型 | 说明 | 样式特点 |
|------|------|----------|
| contract | 合同/协议 | 宋体正文、首行缩进、正式严谨 |
| manual | 说明书/指南 | 微软雅黑、清晰易读、步骤明确 |
| report | 报告/分析 | 宋体、 justified对齐、学术规范 |
| proposal | 方案书/计划 | 微软雅黑、层次分明、专业商务 |

## 安装依赖

```bash
pip install -r requirements.txt
```

## 快速开始

### 1. 创建测试文档（可选）

```bash
python test_create_sample.py
```

这将在 `test_docs` 目录下创建示例文档用于测试。

### 2. 美化单个文档（覆盖原文件）

```bash
python main.py -f test_docs/示例合同.docx
```

美化后的文件将覆盖原文件，文件名保持不变。

### 3. 美化并保存到指定目录（文件名不变）

```bash
python main.py -f document.docx -o ./output_dir
```

美化后的文件将保存到 `output_dir` 目录，文件名与原文件相同。

### 4. 批量美化目录下的所有文档（必须指定输出目录）

```bash
python main.py -d ./test_docs -o ./output_dir
```

**重要：** 批量处理时必须指定输出目录 (`-o` 参数)，原文件会被保留。

### 5. 递归处理子目录

```bash
python main.py -d ./documents -o ./output_dir -r
```

### 6. 断点续传功能

系统会自动跳过已处理的文件，支持中断后继续处理：

```bash
# 第一次运行：处理所有文件
python main.py -d ./test_docs -o ./output_dir

# 中断后再次运行：只处理未完成的文件
python main.py -d ./test_docs -o ./output_dir
```

### 7. 查看支持的文档类型

```bash
python main.py --types
```

## 项目结构

```
builtiful_dcox/
├── config/                 # 配置模块
│   ├── __init__.py
│   └── style_templates.py  # 样式模板定义
├── core/                   # 核心模块
│   ├── __init__.py
│   ├── document_analyzer.py    # 文档分析器
│   ├── type_classifier.py      # 类型分类器
│   ├── style_applier.py        # 样式应用器
│   └── beautifier.py           # 美化引擎
├── templates/              # 模板模块（预留扩展）
│   └── __init__.py
├── utils/                  # 工具模块
│   ├── __init__.py
│   └── helpers.py          # 辅助函数
├── main.py                 # 主入口程序
├── test_create_sample.py   # 测试文档生成器
├── requirements.txt        # 依赖包列表
└── README.md              # 说明文档
```

## 核心模块说明

### 1. DocumentAnalyzer（文档分析器）
- 提取文档文本内容
- 分析段落结构和样式
- 检测文档特征（标题、表格、签署区等）

### 2. DocumentTypeClassifier（类型分类器）
- 基于关键词匹配
- 基于结构特征分析
- 计算置信度评分

### 3. StyleTemplate（样式模板）
- ContractStyleTemplate：合同样式
- ManualStyleTemplate：说明书样式
- ReportStyleTemplate：报告样式
- ProposalStyleTemplate：方案书样式

每个模板定义：
- 标题样式（字体、大小、颜色、间距）
- 各级标题样式
- 正文样式（缩进、行距、对齐）
- 表格样式

### 4. StyleApplier（样式应用器）
- 应用页面边距
- 格式化标题和正文
- 美化表格边框和样式

### 5. DocumentBeautifier（美化引擎）
- 整合分析、分类、样式应用流程
- 提供单文件和批量处理接口

## 扩展开发

### 添加新的文档类型

1. 在 `config/style_templates.py` 中创建新的样式类：

```python
class NewTypeStyleTemplate(StyleTemplate):
    def get_title_style(self):
        return {...}
    
    def get_heading_styles(self):
        return {...}
    
    def get_normal_style(self):
        return {...}
```

2. 在 `STYLE_TEMPLATES` 字典中注册：

```python
STYLE_TEMPLATES = {
    'new_type': NewTypeStyleTemplate,
    ...
}
```

3. 在 `core/type_classifier.py` 中添加关键词模式：

```python
KEYWORD_PATTERNS = {
    NEW_TYPE: [关键词1, 关键词2, ...],
    ...
}
```

### 自定义样式参数

修改 `config/style_templates.py` 中的样式配置：

```python
{
    'font_name': '微软雅黑',      # 字体
    'font_size': Pt(12),          # 字号
    'bold': True,                 # 加粗
    'alignment': WD_ALIGN_PARAGRAPH.CENTER,  # 对齐
    'color': RGBColor(0, 0, 0),   # 颜色
    'line_spacing': 1.5,          # 行距
    'space_before': Pt(6),        # 段前距
    'space_after': Pt(6),         # 段后距
}
```

## 使用示例代码

```python
from core.beautifier import beautify_document

# 美化单个文档（覆盖原文件）
result = beautify_document('input.docx')

# 美化并保存到指定目录（文件名不变）
result = beautify_document('input.docx', './output_dir')

if result['success']:
    print(f"文档类型: {result['doc_type']}")
    print(f"置信度: {result['confidence']}")
    print(f"输出文件: {result['output_path']}")
```

```python
from core.beautifier import batch_beautify_documents

# 批量美化
files = ['doc1.docx', 'doc2.docx', 'doc3.docx']
results = batch_beautify_documents(files, './output_dir')
```

## 技术栈

- **python-docx**: DOCX文件处理
- **re**: 正则表达式（文档分析）
- **argparse**: 命令行参数解析

## 注意事项

1. 仅支持 `.docx` 格式（不支持旧版 `.doc`）
2. 文档类型识别基于关键词和结构特征，置信度可能因文档质量而异
3. **单文件模式**：如果不指定输出目录，将覆盖原文件；如果指定输出目录，则保存到该目录
4. **批量模式**：必须指定输出目录，原文件会被保留
5. **断点续传**：批量处理时会自动跳过已存在的文件，支持中断后继续处理
6. 中文字体需要系统已安装相应字体（如宋体、黑体、微软雅黑）

## 未来改进方向

- [ ] 支持更多文档类型（论文、简历、新闻稿等）
- [ ] 集成AI模型提高分类准确度
- [ ] 支持用户自定义样式模板
- [ ] 添加GUI界面
- [ ] 支持PDF输出
- [ ] 图片处理和优化
- [ ] 目录自动生成

## 许可证

MIT License

## 作者

资产系统设计师 & 架构师

---

**享受优雅的文档排版！** ✨
