def codegen(context):
    for role in context.roles:
        print('define %s = Character("%s")' % (role, role))

    print("")

    for i in context.ir:
        if i['type'] == 'word':
            # 旁白
            if i['role'] == None:
                print('"' + i['words'] + '"')
            else:
                print('%s "%s"' % (i['role'], i['words']))
        elif i['type'] == 'meta':
            print('# %s' % (i['data']))