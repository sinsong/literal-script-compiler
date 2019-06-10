import re

def llparse(context, raw_lines):
    """
    raw_lines -> logic_lines
    """
    logic_lines = []
    tmp_line = []

    re_meta = re.compile(R"^\s*#")

    for raw_line in raw_lines:
        if len(raw_line) == 0:
            if len(tmp_line) == 0: # 跳过连续空行
                continue
            logic_lines.append(tmp_line)
            tmp_line = []
        else:
            # 检测元信息
            if re_meta.match(raw_line):
                logic_lines.append([raw_line]) # 逻辑行都是列表
                continue

            # 扩张逻辑行
            tmp_line.append(raw_line)

    # 剩余的组成逻辑行
    if len(tmp_line) != 0:
        logic_lines.append(tmp_line)
    
    # return logic_lines
    context.ll = logic_lines