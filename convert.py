#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os, subprocess
class Convert:
    def __init__(self):
        if sys.platform == 'win32':
            self.convert_path = "C:\Program Files\ImageMagick-6.7.9-Q16\convert.exe"
        else:
            self.convert_path = "convert"
    def tiffgif(self, filename):
        base,ext = os.path.splitext(filename)
        command = [self.convert_path, filename, base + ".gif"]
        subprocess.call(command, stderr=subprocess.PIPE)
        return base + ".gif"
