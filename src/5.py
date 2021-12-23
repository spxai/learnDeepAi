#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#1-2-2-4.py
import torch
x1=torch.tensor([[10,20],[2,4]])
print(x1)
print(x1.size())
y=((11,21),(11,66))
x2=torch.tensor(y)
print(x2)