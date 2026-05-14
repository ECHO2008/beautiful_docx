"""
文档类型分类器
根据文档内容和结构特征，识别文档类型
"""
import re
from typing import Dict, List, Tuple


class DocumentTypeClassifier:
    """文档类型分类器"""
    
    # 文档类型枚举
    CONTRACT = "contract"      # 合同
    MANUAL = "manual"          # 说明书
    REPORT = "report"          # 报告
    PROPOSAL = "proposal"      # 方案书
    UNKNOWN = "unknown"        # 未知类型
    
    # 各类文档的关键词特征
    KEYWORD_PATTERNS = {
        CONTRACT: [
            r'合同', r'协议', r'甲方', r'乙方', r'签署', r'生效',
            r'违约责任', r'争议解决', r'保密条款', r'付款方式',
            r'交货日期', r'质量标准', r'验收标准', r'不可抗力',
            r'contract', r'agreement', r'party A', r'party B'
        ],
        MANUAL: [
            r'使用说明', r'操作指南', r'安装步骤', r'注意事项',
            r'技术参数', r'产品规格', r'维护保养', r'故障排除',
            r'安全警告', r'功能介绍', r'快速入门', r'目录',
            r'manual', r'instruction', r'guide', r'specification'
        ],
        REPORT: [
            r'摘要', r'引言', r'结论', r'建议', r'数据分析',
            r'研究方法', r'调查结果', r'统计分析', r'图表',
            r'参考文献', r'附录', r'背景', r'目标',
            r'report', r'analysis', r'summary', r'conclusion'
        ],
        PROPOSAL: [
            r'项目方案', r'实施方案', r'技术方案', r'预算',
            r'进度计划', r'资源配置', r'风险评估', r'预期效果',
            r'项目背景', r'需求分析', r'解决方案',
            r'proposal', r'plan', r'solution', r'budget'
        ]
    }
    
    # 结构特征权重
    STRUCTURE_WEIGHTS = {
        CONTRACT: {
            'has_signature_section': 0.3,      # 有签署区域
            'has_party_info': 0.3,             # 有甲乙双方信息
            'has_clauses': 0.2,                # 有条款编号
            'formal_language': 0.2             # 正式语言
        },
        MANUAL: {
            'has_steps': 0.3,                  # 有步骤说明
            'has_warnings': 0.2,               # 有警告提示
            'has_specifications': 0.2,         # 有技术规格
            'has_toc': 0.3                     # 有目录
        },
        REPORT: {
            'has_abstract': 0.25,              # 有摘要
            'has_sections': 0.25,              # 有章节
            'has_references': 0.25,            # 有参考文献
            'has_charts': 0.25                 # 有图表
        },
        PROPOSAL: {
            'has_background': 0.2,             # 有背景介绍
            'has_plan': 0.3,                   # 有方案内容
            'has_budget': 0.25,                # 有预算
            'has_timeline': 0.25               # 有时间计划
        }
    }
    
    def __init__(self):
        self.confidence_threshold = 0.6  # 置信度阈值
    
    def classify(self, text_content: str, structure_info: Dict = None) -> Tuple[str, float]:
        """
        分类文档类型
        
        Args:
            text_content: 文档文本内容
            structure_info: 文档结构信息（可选）
            
        Returns:
            (文档类型, 置信度)
        """
        if not text_content:
            return self.UNKNOWN, 0.0
        
        # 基于关键词评分
        keyword_scores = self._calculate_keyword_scores(text_content)
        
        # 基于结构特征评分（如果提供）
        structure_scores = {}
        if structure_info:
            structure_scores = self._calculate_structure_scores(structure_info)
        
        # 综合评分
        final_scores = {}
        for doc_type in self.KEYWORD_PATTERNS.keys():
            keyword_score = keyword_scores.get(doc_type, 0)
            struct_score = structure_scores.get(doc_type, 0)
            
            # 关键词权重 0.7，结构权重 0.3
            if structure_info:
                final_scores[doc_type] = keyword_score * 0.7 + struct_score * 0.3
            else:
                final_scores[doc_type] = keyword_score
        
        # 找出最高分
        best_type = max(final_scores, key=final_scores.get)
        confidence = final_scores[best_type]
        
        # 如果置信度低于阈值，返回未知
        if confidence < self.confidence_threshold:
            return self.UNKNOWN, confidence
        
        return best_type, confidence
    
    def _calculate_keyword_scores(self, text: str) -> Dict[str, float]:
        """计算关键词匹配得分"""
        scores = {}
        text_lower = text.lower()
        
        for doc_type, patterns in self.KEYWORD_PATTERNS.items():
            match_count = 0
            for pattern in patterns:
                if re.search(pattern, text_lower):
                    match_count += 1
            
            # 归一化得分（0-1之间）
            scores[doc_type] = min(match_count / 5.0, 1.0)
        
        return scores
    
    def _calculate_structure_scores(self, structure_info: Dict) -> Dict[str, float]:
        """计算结构特征得分"""
        scores = {}
        
        for doc_type, weights in self.STRUCTURE_WEIGHTS.items():
            score = 0
            for feature, weight in weights.items():
                if structure_info.get(feature, False):
                    score += weight
            scores[doc_type] = score
        
        return scores
    
    def get_supported_types(self) -> List[str]:
        """获取支持的文档类型列表"""
        return list(self.KEYWORD_PATTERNS.keys())
