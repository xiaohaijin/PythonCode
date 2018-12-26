#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
author : xiaohai
email : xiaohaijin@outlook.com
"""


import os
import subprocess


result = os.listdir(os.getcwd())
for eachFile in result:
    if str(eachFile).endswith(".con"):
        subprocess.call(("condor_submit", eachFile))
