import sys 
import subprocess

#accept user input
def get_user_input():
    input = sys.argv[1]
    input_str = input
    print("Input String: " + input_str)
    return input_str
    

#return dependency tree
def run_command(cmd, input=""):
    p = create_process(cmd) #, stderr=subprocess.STDOUT)
    cmd_stdout = p.communicate(input=input.encode('utf-8'))[0]
    out = cmd_stdout.decode('utf-8')
    return out

def write_input(process, input):
    process.stdin.write(input)
    return process.stdout.readline()

def create_process(cmd):
    return subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)