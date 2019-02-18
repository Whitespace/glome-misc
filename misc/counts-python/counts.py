#! /usr/bin/env python
from random import sample

all = [24, 30, 36, 42, 48, 54, 60, 66, 72, 24, 30, 36, 42, 48, 54, 60, 66, 72, 24, 30, 36, 42, 48, 54, 60, 66, 72, 24, 30, 36, 42, 48, 54, 60, 66, 72, 24, 30, 36, 42, 48, 54, 60, 66, 72, 24, 30, 36, 42, 48, 54, 60, 66, 72, 25, 30, 35, 40, 45, 50, 55, 60, 25, 30, 35, 40, 45, 50, 55, 60, 25, 30, 35, 40, 45, 50, 55, 60, 25, 30, 35, 40, 45, 50, 55, 60]
c=0
l=65

while True:
  s = sample(all, k=86)
  for i in range(0, 86-l):
    for j in range(i+l, 86-1):
      strips = all[i:j]
      total = sum(strips)
      count = len(strips)
      if total % 50 == 0 and total / 50 == count:
        print(f"i: {i} j: {j}\n{count} strings ({total} lights)\n{sorted(strips)}")
      c+=1
      if c % 10000000 == 0:
        print(c)
