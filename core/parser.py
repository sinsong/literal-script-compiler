import re

def parse(context):
    ir = []

    re_meta = re.compile(R"^\s*#")
    re_name = re.compile(R"【(.+)】")
    re_meta2 = re.compile(R"^\s*#(.*)")

    for logic_line in context.ll:
        if re_name.match(logic_line[0]):
            # 角色说话
            role = re_name.match(logic_line[0]).group(1)
            context.roles.add(role) # 加入角色表
            ir.append({'type': 'word', 'role': role, 'words': "".join(logic_line[1:])})
        elif re_meta.match(logic_line[0]):
            # 元信息
            ir.append({'type': 'meta', 'data': "".join(logic_line).strip('\t').strip().lstrip('#')})
        else:
            # 旁白
            ir.append({'type': 'word', 'role': None, 'words': "".join(logic_line)})

    # return ir
    context.ir = ir