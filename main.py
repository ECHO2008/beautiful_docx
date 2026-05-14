"""
DOCX文档智能美化系统
主入口程序
"""
import sys
import os
import argparse
from core.beautifier import DocumentBeautifier, beautify_document, batch_beautify_documents
from utils.helpers import find_docx_files, validate_docx_file, get_file_info


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='DOCX文档智能美化系统',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 美化单个文档（覆盖原文件）
  python main.py -f document.docx
  
  # 美化并保存到指定目录（文件名不变）
  python main.py -f document.docx -o ./output_dir
  
  # 批量美化目录下所有文档（必须指定输出目录）
  python main.py -d ./documents -o ./output_dir
  
  # 递归批量美化
  python main.py -d ./documents -o ./output_dir -r
  
  # 查看支持的文档类型
  python main.py --types
        """
    )
    
    parser.add_argument('-f', '--file', type=str, help='要美化的DOCX文件路径')
    parser.add_argument('-o', '--output', type=str, help='输出目录（单文件模式可选，批量模式必选）')
    parser.add_argument('-d', '--directory', type=str, help='批量处理目录')
    parser.add_argument('-r', '--recursive', action='store_true', help='递归查找子目录中的文件')
    parser.add_argument('--types', action='store_true', help='显示支持的文档类型')
    
    args = parser.parse_args()
    
    # 显示支持的文档类型
    if args.types:
        beautifier = DocumentBeautifier()
        types = beautifier.get_supported_types()
        print("\n支持的文档类型:")
        print("-" * 40)
        for doc_type in types:
            type_names = {
                'contract': '合同',
                'manual': '说明书',
                'report': '报告',
                'proposal': '方案书'
            }
            name_cn = type_names.get(doc_type, doc_type)
            print(f"  {doc_type:15} - {name_cn}")
        print()
        return
    
    # 单文件模式
    if args.file:
        if not validate_docx_file(args.file):
            print(f"错误: 无效的文件路径或格式: {args.file}")
            sys.exit(1)
        
        try:
            result = beautify_document(args.file, args.output)
            
            if result['success']:
                print("\n美化成功！")
                print(f"输入文件: {result['input_path']}")
                print(f"输出文件: {result['output_path']}")
                if args.output:
                    print(f"保存位置: 输出目录 ({args.output})")
                else:
                    print(f"保存位置: 覆盖原文件")
                print(f"文档类型: {result['doc_type']}")
                print(f"置信度: {result['confidence']:.2%}")
            else:
                print(f"\n美化失败: {result.get('error', '未知错误')}")
                sys.exit(1)
                
        except Exception as e:
            print(f"\n处理出错: {str(e)}")
            sys.exit(1)
    
    # 批量模式
    elif args.directory:
        # 批量模式必须指定输出目录
        if not args.output:
            print(f"错误: 批量处理时必须指定输出目录 (-o 参数)")
            print(f"示例: python main.py -d {args.directory} -o ./output_dir")
            sys.exit(1)
        
        if not os.path.isdir(args.directory):
            print(f"错误: 无效的目录路径: {args.directory}")
            sys.exit(1)
        
        # 查找DOCX文件
        docx_files = find_docx_files(args.directory, args.recursive)
        
        if not docx_files:
            print(f"在目录 {args.directory} 中未找到DOCX文件")
            sys.exit(1)
        
        print(f"找到 {len(docx_files)} 个DOCX文件:")
        for file_path in docx_files:
            info = get_file_info(file_path)
            print(f"  - {info['name']} ({info['formatted_size']})")
        print()
        print(f"输出目录: {args.output}")
        print("注意: 已处理的文件将被跳过（支持断点续传）")
        print()
        
        # 确认是否继续
        confirm = input("是否继续处理? (y/n): ").strip().lower()
        if confirm != 'y':
            print("已取消")
            return
        
        # 批量处理
        print("\n开始批量处理...")
        print("=" * 60)
        
        results = batch_beautify_documents(docx_files, args.output)
        
        # 统计结果
        success_count = sum(1 for r in results if r.get('success') and not r.get('skipped'))
        skipped_count = sum(1 for r in results if r.get('skipped'))
        fail_count = sum(1 for r in results if not r.get('success'))
        
        print("\n" + "=" * 60)
        print(f"处理完成！")
        print(f"  新处理: {success_count} 个文件")
        print(f"  已跳过: {skipped_count} 个文件（已存在）")
        print(f"  失败: {fail_count} 个文件")
        
        if fail_count > 0:
            print("\n失败的文件:")
            for result in results:
                if not result.get('success'):
                    print(f"  - {result['input_path']}: {result.get('error')}")
    
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
