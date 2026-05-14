"""
文档美化引擎
整合分析、分类和样式应用，实现完整的文档美化流程
"""
from docx import Document
from typing import Tuple
import os

from core.document_analyzer import DocumentAnalyzer
from core.type_classifier import DocumentTypeClassifier
from core.style_applier import StyleApplier
from config.style_templates import get_style_template


class DocumentBeautifier:
    """文档美化引擎"""
    
    def __init__(self):
        self.classifier = DocumentTypeClassifier()
        
    def beautify(self, input_path: str, output_dir: str = None) -> dict:
        """
        美化文档
        
        Args:
            input_path: 输入文档路径
            output_dir: 输出目录（可选，如果指定则保存到该目录，文件名不变；否则覆盖原文件）
            
        Returns:
            美化结果信息
        """
        # 验证输入文件
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"文件不存在: {input_path}")
        
        if not input_path.endswith('.docx'):
            raise ValueError("仅支持 .docx 格式文件")
        
        # 生成输出路径：保持原文件名不变
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            base_name = os.path.basename(input_path)
            output_path = os.path.join(output_dir, base_name)
        else:
            # 如果没有指定输出目录，则覆盖原文件
            output_path = input_path
        
        print(f"开始处理文档: {input_path}")
        
        # 步骤1: 分析文档
        print("步骤1: 分析文档结构和内容...")
        analyzer = DocumentAnalyzer(input_path)
        analysis_result = analyzer.analyze()
        
        text_content = analysis_result['text_content']
        structure_info = analysis_result['structure_info']
        
        print(f"  - 段落数: {analysis_result['total_paragraphs']}")
        print(f"  - 表格数: {analysis_result['total_tables']}")
        print(f"  - 标题数: {analysis_result['heading_count']}")
        
        # 步骤2: 识别文档类型
        print("步骤2: 识别文档类型...")
        doc_type, confidence = self.classifier.classify(text_content, structure_info)
        
        print(f"  - 文档类型: {doc_type}")
        print(f"  - 置信度: {confidence:.2%}")
        
        if doc_type == self.classifier.UNKNOWN:
            print("  - 警告: 无法明确识别文档类型，使用默认样式")
            doc_type = 'contract'  # 默认使用合同样式
        
        # 步骤3: 获取样式模板
        print(f"步骤3: 加载 [{doc_type}] 样式模板...")
        style_template = get_style_template(doc_type)
        
        # 步骤4: 应用样式
        print("步骤4: 应用样式美化文档...")
        document = Document(input_path)
        style_applier = StyleApplier(document, style_template)
        style_applier.apply_all_styles()
        
        # 步骤5: 保存文档
        print(f"步骤5: 保存美化后的文档...")
        document.save(output_path)
        
        result = {
            'success': True,
            'input_path': input_path,
            'output_path': output_path,
            'doc_type': doc_type,
            'confidence': confidence,
            'stats': {
                'paragraphs': analysis_result['total_paragraphs'],
                'tables': analysis_result['total_tables'],
                'headings': analysis_result['heading_count']
            }
        }
        
        print(f"\n✓ 文档美化完成！")
        print(f"  输出文件: {output_path}")
        print(f"  文档类型: {doc_type} (置信度: {confidence:.2%})")
        
        return result
    
    def batch_beautify(self, input_paths: list, output_dir: str) -> list:
        """
        批量美化文档
        
        Args:
            input_paths: 输入文件路径列表
            output_dir: 输出目录（必须指定）
            
        Returns:
            美化结果列表
        """
        if not output_dir:
            raise ValueError("批量处理时必须指定输出目录")
        
        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)
        
        results = []
        
        for input_path in input_paths:
            try:
                # 检查是否已经处理过（断点续传）
                base_name = os.path.basename(input_path)
                output_path = os.path.join(output_dir, base_name)
                
                if os.path.exists(output_path):
                    print(f"⊘ 跳过已处理的文件: {base_name}")
                    result = {
                        'success': True,
                        'input_path': input_path,
                        'output_path': output_path,
                        'skipped': True,
                        'message': '文件已存在，跳过处理'
                    }
                    results.append(result)
                    continue
                
                result = self.beautify(input_path, output_dir)
                results.append(result)
                
            except Exception as e:
                error_result = {
                    'success': False,
                    'input_path': input_path,
                    'error': str(e)
                }
                results.append(error_result)
                print(f"✗ 处理失败: {input_path} - {str(e)}")
        
        return results
    
    def get_supported_types(self) -> list:
        """获取支持的文档类型"""
        return self.classifier.get_supported_types()


def beautify_document(input_path: str, output_dir: str = None) -> dict:
    """
    便捷函数：美化单个文档
    
    Args:
        input_path: 输入文档路径
        output_dir: 输出目录（可选，如果指定则保存到该目录，文件名不变；否则覆盖原文件）
        
    Returns:
        美化结果
    """
    beautifier = DocumentBeautifier()
    return beautifier.beautify(input_path, output_dir)


def batch_beautify_documents(input_paths: list, output_dir: str) -> list:
    """
    便捷函数：批量美化文档
    
    Args:
        input_paths: 输入文件路径列表
        output_dir: 输出目录（必须指定）
        
    Returns:
        美化结果列表
    """
    beautifier = DocumentBeautifier()
    return beautifier.batch_beautify(input_paths, output_dir)
