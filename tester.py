import argparse
import subprocess as sp
import os
import psutil

parser = argparse.ArgumentParser(description='Time And Memory')
parser.add_argument('-f', required=True)

args = parser.parse_args()
filename = args.f
if filename.endswith('.py'):
    file = int(filename[:-3])
else:
    file = int(filename)

files = f'python/{(file//10000)*10000}/{file//1000}000/{file}.py'

try:
    with open(files) as f:
        con = f.read()
except FileNotFoundError:
    print(f"문제 파일을 찾을 수 없습니다: {files}")
    exit(1)

try:
    with open('tstdir/input.txt') as f:
        inp = f.read()
except FileNotFoundError:
    print("tstdir/input.txt 파일을 찾을 수 없습니다.")
    exit(1)

tst_path = 'tstdir/tst.py'
with open(tst_path, 'w') as f:
    f.write('import time\n')
    f.write('import psutil\n')
    f.write('process = psutil.Process()\n')
    f.write('start_mem = process.memory_info().rss\n')
    f.write('starttimer = time.perf_counter()\n')
    f.write(con)
    f.write('\n')
    f.write('endtimer = time.perf_counter()\n')
    f.write('end_mem = process.memory_info().rss\n')
    f.write('print(f"Time : {(endtimer-starttimer)*1000:.2f}ms")\n')
    f.write('print(f"Memory : {(end_mem-start_mem)/1024:.2f}KB")\n')

try:
    sp.run(['python3', tst_path], input=inp, text=True)
finally:
    if os.path.exists(tst_path):
        os.remove(tst_path)