"""
辅助工具函数
"""
import os
from typing import List


def find_docx_files(directory: str, recursive: bool = False) -> List[str]:
    """
    查找目录下的所有DOCX文件
    
    Args:
        directory: 目录路径
        recursive: 是否递归查找
        
    Returns:
        DOCX文件路径列表
    """
    docx_files = []
    
    if recursive:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.docx'):
                    docx_files.append(os.path.join(root, file))
    else:
        for file in os.listdir(directory):
            if file.endswith('.docx'):
                docx_files.append(os.path.join(directory, file))
    
    return sorted(docx_files)


def validate_docx_file(file_path: str) -> bool:
    """
    验证DOCX文件是否有效
    
    Args:
        file_path: 文件路径
        
    Returns:
        是否有效
    """
    if not os.path.exists(file_path):
        return False
    
    if not file_path.endswith('.docx'):
        return False
    
    # 检查文件大小
    file_size = os.path.getsize(file_path)
    if file_size == 0:
        return False
    
    return True


def format_file_size(size_bytes: int) -> str:
    """
    格式化文件大小
    
    Args:
        size_bytes: 字节数
        
    Returns:
        格式化后的文件大小字符串
    """
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.2f} MB"


def get_file_info(file_path: str) -> dict:
    """
    获取文件信息
    
    Args:
        file_path: 文件路径
        
    Returns:
        文件信息字典
    """
    if not os.path.exists(file_path):
        return {}
    
    stat = os.stat(file_path)
    
    return {
        'path': file_path,
        'name': os.path.basename(file_path),
        'size': stat.st_size,
        'formatted_size': format_file_size(stat.st_size),
        'modified_time': stat.st_mtime
    }
