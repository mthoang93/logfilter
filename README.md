# logfilter
Tools to manipulate log file

# How to use

```python
python3 logfilter --help

usage: logfilter.py [-h] [-i] -t TOKEN [-p PATH] [-f FILE_PREFIX] FILE

Log filter

positional arguments:
  FILE

optional arguments:
  -h, --help            show this help message and exit
  -i                    Case insensitive
  -t TOKEN, --token TOKEN
                        Token used to split the log
  -p PATH, --path PATH  Path of the output folder
  -f FILE_PREFIX, --file-prefix FILE_PREFIX
                        Sliced log files prefix
```