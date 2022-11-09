import os
import pathlib

def get_source_file_path():
    print('请输入文件路径:')    #source file path
    dir = input()
    if os.path.isabs(dir) == True:
        dir = dir
    else:
        dir = os.path.abspath(dir)
    dir = pathlib.Path(dir)
    return dir
def get_file_format():
    print('请输入文件类型,例如.jpg:')   #.jpg e.g.
    format = input()
    format = '**/*' + format    #search subfolder
    return format
def get_target_file_path():
    print('请输入保存路径:')    #target file path
    dest_dir = input()
    if os.path.isabs(dest_dir) == True:
        dest_dir = dest_dir
    else:
        dest_dir = os.path.abspath(dest_dir)
    return dest_dir

result = list(get_source_file_path().glob(get_file_format()))
os.chdir(get_target_file_path())  #change current dir
result_file = open('result.txt','w')
for i in result:
    result_file.write(str(i)+'\n')
print('Successful')
