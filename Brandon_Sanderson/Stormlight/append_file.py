import sys
import os

count = 0
f_path = os.path.dirname(__file__) + '/'

# call with --main_file.txt --file1_to_append.txt --file2_to_append.txt --file3_to_append.txt, etc.

for arg in sys.argv[1:]:
    count += 1

    if count != 1:
        assert arg.startswith('--')
        append_file = open(f_path + arg[2:], 'r', encoding='utf-8')
        main_file.write(append_file.read())
        append_file.close()
    else:
        assert arg.startswith('--')
        main_file = open(f_path + arg[2:], 'a', encoding='utf-8')

