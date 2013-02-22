#!/usr/bin/python
# -*- coding: utf-8 -*-
import Image
import os

class SymbolSeeker:
    def __init__(self):
        self.position = []
        
    def split_seq(self, seq, size):
        return [seq[i:i+size] for i in range(0, len(seq), size)]

    def seek(self, srcImage, dstImage, resume_xy):
        # Initialize
        print 'Start seek symbol. ' + \
              '(Symbol image file: ' + srcImage + \
              '  Target image file: ' + dstImage + ')'
        srcimg = Image.open(srcImage)
        srcimg = srcimg.convert('1')
        dstimg = Image.open(dstImage)
        dstimg = dstimg.convert('1')
        src_width, src_height = srcimg.size
        dst_width, dst_height = dstimg.size
        print 'srcimg.size:' + str(srcimg.size)
        print 'dstimg.size:' + str(dstimg.size)
        
        l1 = list(srcimg.getdata())
        m1 = self.split_seq(l1, src_width)
        l2 = list(dstimg.getdata())
        m2 = self.split_seq(l2, dst_width)
        precision = float(80)
        hits = float(0)
        bits = float(src_width / 2) * float(src_height / 3)
        index = 0
        dx_range = dst_width - src_width
        dy_range = dst_height - src_height
        rx,ry = resume_xy
        found = False
        
        # Seek symbol image
        for dx in range(500 + rx, dx_range, 2):
            for dy in range(0 + ry, dy_range, 3):
                hits = 0
                for sx in range(0, src_width, 1):
                    for sy in range(0, src_height, 1):
                        if m1[sy][sx] == m2[dy + sy][dx + sx]:
                            hits += 1
                if float(hits) / bits * 100 > precision:
                    self.position.append((dx, dy - src_height))
                    print 'Symbol is matched.: ' + str(self.position[index])
                    index += 1
                    found = True
        return found

    def blankfield(self, image, position):
        img = Image.open(image)
        img = img.convert('1')
        width, height = img.size
        m1 = self.split_seq(list(img.getdata()), width)
        #print 'is this black? : ' + str(m1[145][624])
        hits = float(0)
        bits = float(32 / 3) * float(32 / 3)
        gx,gy = position
        
        hits = 0
        for x in range(gx, gx + 32, 3):
            for y in range(gy, gy + 32, 3):
                #print 'x,y:' + str(x) + ',' + str(y) + ' : ' + str(m1[y][x])
                if m1[y][x] == 0:
                    hits += 1
        print 'hits: ' + str(hits) + ' bits:' + str(bits) + \
              ' percentage: ' + str(float(hits) / bits * 100)
        if float(hits) / bits * 100 > float(10):
            return False
        else:
            return True
