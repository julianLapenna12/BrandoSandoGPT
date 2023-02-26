import sys

count = 0

# call with --main_file.txt --file1_to_append.txt --file2_to_append.txt --file3_to_append.txt, etc.

for arg in sys.argv[1:]:
    count += 1

    if count != 1:
        assert arg.startswith('--')
        append_file = open(arg[2:], 'r', encoding='utf-8')
        main_file.write(append_file.read())
        append_file.close()
    else:
        assert arg.startswith('--')
        main_file = open(arg[2:], 'a', encoding='utf-8')

