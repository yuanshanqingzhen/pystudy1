import re
from collections import defaultdict

def word_frequency_analyzer(file_path, output_to_file=False, output_filename="word_frequency_result.txt"):
    """
    单词频率统计器
    
    参数:
    file_path: 英文文章文件路径
    output_to_file: 是否将结果输出到文件
    output_filename: 输出文件名
    """
    
    try:
        # 1. 读取文件
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # 2. 清洗和分割单词
        # 使用正则表达式只保留字母和连字符
        # \b - 单词边界，确保匹配完整单词
        # [a-zA-Z\-] - 字符类，匹配：
        # a-z：小写字母
        # A-Z：大写字母
        # \-：连字符 -
        # + - 量词，匹配前面的字符类一次或多次
        # \b - 结束的单词边界
        # 转换为小写
        words = re.findall(r'\b[a-zA-Z\-]+\b', text)
        words = [word.lower() for word in words]
        
        # 3. 统计频率
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        
        # 4. 按频率排序（频率相同按字母顺序）
        # key=lambda x: (-x[1], x[0]) 使主要条件（频率）降序，次要条件（单词字母）升序
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        
        # 5. 输出结果
        if output_to_file:
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write("单词频率统计结果\\n")
                output_file.write("=" * 30 + "\\n")
                for i, (word, count) in enumerate(sorted_words, 1):
                    output_file.write(f"{i:3d}. {word:<20} {count:>3}次\\n")
            print(f"结果已保存到文件: {output_filename}")
        else:
            print("单词频率统计结果")
            print("=" * 30)
            for i, (word, count) in enumerate(sorted_words, 1):
                print(f"{i:3d}. {word:<20} {count:>3}次")
        
        # 返回统计信息
        total_words = len(words)
        unique_words = len(sorted_words)
        
        print("\n统计摘要:")
        print(f"总单词数: {total_words}")
        print(f"独特单词数: {unique_words}")
        print(f"最常出现的单词: '{sorted_words[0][0]}' (出现{sorted_words[0][1]}次)")
        
        return sorted_words
        
    except FileNotFoundError:
        print(f"错误：找不到文件 '{file_path}'")
        return None
    except Exception as e:
        print(f"发生错误: {e}")
        return None

def create_sample_file():
    """创建一个示例文件用于测试"""
    sample_text = """
    The quick brown fox jumps over the lazy dog. The dog was not happy about this.
    Foxes are known for being quick and clever. The dog, however, preferred to stay lazy.
    In the end, both the fox and the dog went their separate ways.
    Quick thinking and lazy days both have their place in life.
    """
    
    with open("sample_article.txt", "w", encoding="utf-8") as file:
        file.write(sample_text)
    
    print("已创建示例文件: sample_article.txt")
    return "sample_article.txt"

# 主程序
if __name__ == "__main__":
    print("英文单词频率统计器")
    print("=" * 40)
    
    # 询问用户文件路径
    file_path = input("请输入英文文章文件路径(直接回车使用示例文件): ").strip()
    
    if not file_path:
        file_path = create_sample_file()
    
    # 询问输出方式
    output_choice = input("是否将结果保存到文件? (y/n): ").strip().lower()
    
    # 执行统计
    result = word_frequency_analyzer(
        file_path, 
        output_to_file=(output_choice == 'y')
    )