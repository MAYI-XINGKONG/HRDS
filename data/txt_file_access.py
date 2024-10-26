def read_txt_file_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def parse_txt_file_chapters(content):
    # 这里简单假设章节是以特定格式，比如以"第X章"开头的行来划分章节
    chapters = []
    lines = content.split('\n')
    for line in lines:
        if line.startswith("第") and "章" in line:
            chapters.append(line)
    return chapters