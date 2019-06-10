import chardet
import pprint

def row_file_open(filename):
    with open(filename, 'rb') as f:
        raw_file = f.read()    

    try:
        raw_content = str(raw_file, 'utf8')
    except UnicodeDecodeError:
        print('不是 UTF-8 编码，检测到：')
        pprint.pprint(chardet.detect(raw_content))
        exit(1)
    
    return raw_content