import argparse
import subprocess as sp

parser = argparse.ArgumentParser(description='Time And Memory')
parser.add_argument('-f')

args = parser.parse_args()
file = int(args.f.rstrip('.py'))

files = f'python/{(file//10000)*10000}/{file//1000}000/{file}.py'

with open(files) as f:
    con = f.read()

with open('input.txt') as f:
    inp = f.read()


with open('tst.py','w') as f:
    f.write('import time\n')
    f.write('starttimertimer = time.perf_counter_ns()\n')
    f.write(con)
    f.write('\n')
    f.write('print(f"Time : {(time.perf_counter_ns()-starttimertimer)*1e-05}ms")')

sp.run(['python3','tst.py'],input=inp,text=True)