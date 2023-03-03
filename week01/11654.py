import sys
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'input.txt')
sys.stdin = open(filename, "rt")

char = sys.stdin.readline().rstrip()
print(ord(char))