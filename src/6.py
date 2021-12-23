#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#1-2-2-5.py
import torch
a=[[10.2,20.6],[2,4]]
x=torch.DoubleTensor(a)
print(x)
y=torch.IntTensor(a)
print(y)
b=[[1,2],[3,4]]
z=torch.IntTensor(b)
print(z)