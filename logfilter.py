import os
import sys
import re
import argparse

argparser = argparse.ArgumentParser(description="Log filter")

argparser.add_argument('-i', action='store_true', help='Case insensitive')
argparser.add_argument('file', metavar='FILE', type=str)
argparser.add_argument('-t', '--token', action='store',
                       type=str, required=True, help="Token used to split the log")
argparser.add_argument('-p', '--path', action='store',
                       type=str, default=os.path.join(os.getcwd(), "logs"), help='Path of the output folder')
argparser.add_argument('-f', '--file-prefix', action='store',
                       type=str, default="log_", help='Sliced log files prefix')

args = argparser.parse_args()

in_log_file = args.file
token = args.token
case_insensitive = args.i
log_path = args.path
file_prefix = args.file_prefix


def search_token(file, token):
    ret = [1]
    with open(file, 'r') as f:
        line_num = 1
        for l in f:
            if re.search(token, l):
                ret.append(line_num)
                print(f"{line_num}: {l}")
            line_num += 1
    return ret


def slice_log(log_file, line_list):
    if len(line_list) > 1:
        for i in range(len(line_list) - 1):
            start = line_list[i]
            end = line_list[i + 1]
            with open(log_file, 'r') as f:
                with open(os.path.join(log_path, f"{file_prefix}{i}.txt"), "a") as f2:
                    num = 1
                    for l in f:
                        if num >= start and num <= end:
                            f2.write(l)
                        num += 1
                        if num > end:
                            break


def main():
    try:
        os.mkdir(log_path)
    except:
        pass
    lines = search_token(args.file, token)
    slice_log(args.file, lines)
    print("Finished!")


if __name__ == "__main__":
    main()
