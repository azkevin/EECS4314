import os
import sys

file_ta = open(sys.argv[2], "w")

for root, dirs, files in os.walk(sys.argv[1], topdown=False):
    for name in files:
        if name[-3:] == ".cc" or name[-2:] == ".h" \
                or name[-2:] == ".c" or name[-4:] == ".cpp" \
                or name[-4:] == ".hpp" or name[-5:] == ".java":

            if name[-5:] == ".java":
                find_include = "import"
                include_size = 6

            else:
                find_include = "#include"
                include_size = 8

            lines = open(os.path.join(root, name), "r")
            for line in lines:
                if line[:include_size] == find_include:
                    left_dependency = os.path.join(root, name).replace('\\', '/')[os.path.join(root, name)
                            .find("mysql-server-mysql-8.0.2"):]

                    if name[-5:] == ".java":
                        line_copy = line
                        split = 0
                        pos = 0
                        while line_copy.find('.') != -1:
                            pos = line_copy.find('.')
                            split += pos + 1
                            line_copy = line_copy[pos + 1:]

                        string = "{} -> {}.java\n".format(left_dependency, line[split:-2])
                    else:
                        string = "{} -> {}\n".format(left_dependency, line[10:-2])

                    if string.rfind('"') != -1:
                        string = string[0:string.rfind('"')] + "\n"
                    if (string.rfind('>') != -1) & (string.count('>') > 1):
                        string = string[0:string.rfind('>')] + "\n"
                    if string[string.find('>')+2:-1].find('/') > -1:
                        string = "{} -> {}\n"\
                            .format(left_dependency, os.path.basename(os.path.normpath(string[string.find('>')+2:-1])))
                    file_ta.write(string)
file_ta.close()

