#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#1-2-2-3.py
import torch
x=torch.DoubleTensor(3,5)
print(x.dtype)
print(x.type())
y=torch.BoolTensor(3,5)
print(y.dtype)
print(y.type())