"""
样式模板配置
定义各类文档的样式规范
"""
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH


# 基础样式配置
BASE_STYLES = {
    'font_family': '微软雅黑',
    'default_font_size': 12,
    'line_spacing': 1.5,
    'page_margins': {
        'top': 1.0,
        'bottom': 1.0,
        'left': 1.2,
        'right': 1.2
    }
}


class StyleTemplate:
    """样式模板基类"""
    
    def __init__(self):
        self.name = "base"
        self.styles = {}
        
    def get_title_style(self):
        """获取标题样式"""
        raise NotImplementedError
    
    def get_heading_styles(self):
        """获取各级标题样式"""
        raise NotImplementedError
    
    def get_normal_style(self):
        """获取正文样式"""
        raise NotImplementedError
    
    def get_table_style(self):
        """获取表格样式"""
        raise NotImplementedError


class ContractStyleTemplate(StyleTemplate):
    """合同样式模板"""
    
    def __init__(self):
        super().__init__()
        self.name = "contract"
        
    def get_title_style(self):
        """合同标题样式 - 居中、加粗、大号字体"""
        return {
            'font_name': '黑体',
            'font_size': Pt(22),
            'bold': True,
            'alignment': WD_ALIGN_PARAGRAPH.CENTER,
            'space_before': Pt(24),
            'space_after': Pt(18),
            'color': RGBColor(0, 0, 0)
        }
    
    def get_heading_styles(self):
        """合同章节标题样式"""
        return {
            'heading1': {
                'font_name': '黑体',
                'font_size': Pt(16),
                'bold': True,
                'alignment': WD_ALIGN_PARAGRAPH.LEFT,
                'space_before': Pt(18),
                'space_after': Pt(12),
                'color': RGBColor(0, 0, 0)
            },
            'heading2': {
                'font_name': '宋体',
                'font_size': Pt(14),
                'bold': True,
                'alignment': WD_ALIGN_PARAGRAPH.LEFT,
                'space_before': Pt(12),
                'space_after': Pt(8),
                'color': RGBColor(0, 0, 0)
            },
            'heading3': {
                'font_name': '宋体',
                'font_size': Pt(12),
                'bold': True,
                'alignment': WD_ALIGN_PARAGRAPH.LEFT,
                'space_before': Pt(8),
                'space_after': Pt(6),
                'color': RGBColor(0, 0, 0)
            }
        }
    
    def get_normal_style(self):
        """合同正文样式 - 首行缩进2字符"""
        return {
            'font_name': '宋体',
            'font_size': Pt(12),
            'bold': False,
            'alignment': WD_ALIGN_PARAGRAPH.JUSTIFY,
            'first_line_indent': Inches(0.4),  # 首行缩进
            'line_spacing': 1.5,
            'space_before': Pt(6),
            'space_after': Pt(6),
            'color': RGBColor(0, 0, 0)
        }
    
    def get_table_style(self):
        """合同表格样式"""
        return {
            'border_width': Pt(1),
            'header_bg_color': RGBColor(230, 230, 230),
            'cell_padding': Inches(0.08),
            'font_size': Pt(10),
            'alignment': WD_ALIGN_PARAGRAPH.CENTER
        }


class ManualStyleTemplate(StyleTemplate):
    """说明书样式模板"""
    
    def __init__(self):
        super().__init__()
        self.name = "manual"
        
    def get_title_style(self):
        """说明书标题样式"""
        return {
            'font_name': '微软雅黑',
            'font_size': Pt(24),
            'bold': True,
            'alignment': WD_ALIGN_PARAGRAPH.CENTER,
            'space_before': Pt(30),
            'space_after': Pt(24),
            'color': RGBColor(0, 51, 102)
        }
    
    def get_heading_styles(self):
        """说明书章节标题样式"""
        return {
            'heading1': {
                'font_name': '微软雅黑',
                'font_size': Pt(18),
                'bold': True,
                'alignment': WD_ALIGN_PARAGRAPH.LEFT,
                'space_before': Pt(20),
                'space_after': Pt(12),
                'color': RGBColor(0, 51, 102)
            },
            'heading2': {
                'font_name': '微软雅黑',
                'font_size': Pt(15),
                'bold': True,
                'alignment': WD_ALIGN_PARAGRAPH.LEFT,
                'space_before': Pt(14),
                'space_after': Pt(10),
                'color': RGBColor(0, 102, 153)
            },
            'heading3': {
                'font_name': '微软雅黑',
                'font_size': Pt(13),
                'bold': True,
                'alignment': WD_ALIGN_PARAGRAPH.LEFT,
                'space_before': Pt(10),
                'space_after': Pt(6),
                'color': RGBColor(0, 102, 153)
            }
        }
    
    def get_normal_style(self):
        """说明书正文样式"""
        return {
            'font_name': '微软雅黑',
            'font_size': Pt(11),
            'bold': False,
            'alignment': WD_ALIGN_PARAGRAPH.LEFT,
            'first_line_indent': Inches(0),
            'line_spacing': 1.6,
            'space_before': Pt(4),
            'space_after': Pt(4),
            'color': RGBColor(51, 51, 51)
        }
    
    def get_table_style(self):
        """说明书表格样式"""
        return {
            'border_width': Pt(0.75),
            'header_bg_color': RGBColor(220, 230, 240),
            'cell_padding': Inches(0.1),
            'font_size': Pt(10),
            'alignment': WD_ALIGN_PARAGRAPH.LEFT
        }


class ReportStyleTemplate(StyleTemplate):
    """报告样式模板"""
    
    def __init__(self):
        super().__init__()
        self.name = "report"
        
    def get_title_style(self):
        """报告标题样式"""
        return {
            'font_name': '黑体',
            'font_size': Pt(20),
            'bold': True,
            'alignment': WD_ALIGN_PARAGRAPH.CENTER,
            'space_before': Pt(24),
            'space_after': Pt(18),
            'color': RGBColor(0, 0, 0)
        }
    
    def get_heading_styles(self):
        """报告章节标题样式"""
        return {
            'heading1': {
                'font_name': '黑体',
                'font_size': Pt(16),
                'bold': True,
                'alignment': WD_ALIGN_PARAGRAPH.LEFT,
                'space_before': Pt(18),
                'space_after': Pt(12),
                'color': RGBColor(0, 0, 0)
            },
            'heading2': {
                'font_name': '宋体',
                'font_size': Pt(14),
                'bold': True,
                'alignment': WD_ALIGN_PARAGRAPH.LEFT,
                'space_before': Pt(12),
                'space_after': Pt(8),
                'color': RGBColor(0, 0, 0)
            },
            'heading3': {
                'font_name': '宋体',
                'font_size': Pt(12),
                'bold': True,
                'alignment': WD_ALIGN_PARAGRAPH.LEFT,
                'space_before': Pt(8),
                'space_after': Pt(6),
                'color': RGBColor(0, 0, 0)
            }
        }
    
    def get_normal_style(self):
        """报告正文样式"""
        return {
            'font_name': '宋体',
            'font_size': Pt(12),
            'bold': False,
            'alignment': WD_ALIGN_PARAGRAPH.JUSTIFY,
            'first_line_indent': Inches(0.4),
            'line_spacing': 1.75,
            'space_before': Pt(6),
            'space_after': Pt(6),
            'color': RGBColor(0, 0, 0)
        }
    
    def get_table_style(self):
        """报告表格样式"""
        return {
            'border_width': Pt(1),
            'header_bg_color': RGBColor(240, 240, 240),
            'cell_padding': Inches(0.08),
            'font_size': Pt(10),
            'alignment': WD_ALIGN_PARAGRAPH.CENTER
        }


class ProposalStyleTemplate(StyleTemplate):
    """方案书样式模板"""
    
    def __init__(self):
        super().__init__()
        self.name = "proposal"
        
    def get_title_style(self):
        """方案书标题样式"""
        return {
            'font_name': '微软雅黑',
            'font_size': Pt(22),
            'bold': True,
            'alignment': WD_ALIGN_PARAGRAPH.CENTER,
            'space_before': Pt(24),
            'space_after': Pt(20),
            'color': RGBColor(0, 51, 102)
        }
    
    def get_heading_styles(self):
        """方案书章节标题样式"""
        return {
            'heading1': {
                'font_name': '微软雅黑',
                'font_size': Pt(16),
                'bold': True,
                'alignment': WD_ALIGN_PARAGRAPH.LEFT,
                'space_before': Pt(18),
                'space_after': Pt(12),
                'color': RGBColor(0, 51, 102)
            },
            'heading2': {
                'font_name': '微软雅黑',
                'font_size': Pt(14),
                'bold': True,
                'alignment': WD_ALIGN_PARAGRAPH.LEFT,
                'space_before': Pt(12),
                'space_after': Pt(8),
                'color': RGBColor(0, 102, 153)
            },
            'heading3': {
                'font_name': '微软雅黑',
                'font_size': Pt(12),
                'bold': True,
                'alignment': WD_ALIGN_PARAGRAPH.LEFT,
                'space_before': Pt(8),
                'space_after': Pt(6),
                'color': RGBColor(0, 102, 153)
            }
        }
    
    def get_normal_style(self):
        """方案书正文样式"""
        return {
            'font_name': '微软雅黑',
            'font_size': Pt(12),
            'bold': False,
            'alignment': WD_ALIGN_PARAGRAPH.JUSTIFY,
            'first_line_indent': Inches(0.4),
            'line_spacing': 1.6,
            'space_before': Pt(6),
            'space_after': Pt(6),
            'color': RGBColor(51, 51, 51)
        }
    
    def get_table_style(self):
        """方案书表格样式"""
        return {
            'border_width': Pt(1),
            'header_bg_color': RGBColor(220, 230, 240),
            'cell_padding': Inches(0.1),
            'font_size': Pt(10),
            'alignment': WD_ALIGN_PARAGRAPH.CENTER
        }


# 样式模板映射
STYLE_TEMPLATES = {
    'contract': ContractStyleTemplate,
    'manual': ManualStyleTemplate,
    'report': ReportStyleTemplate,
    'proposal': ProposalStyleTemplate
}


def get_style_template(doc_type: str) -> StyleTemplate:
    """
    获取指定类型的样式模板
    
    Args:
        doc_type: 文档类型
        
    Returns:
        样式模板实例
    """
    template_class = STYLE_TEMPLATES.get(doc_type)
    if template_class:
        return template_class()
    
    # 默认返回合同样式
    return ContractStyleTemplate()
