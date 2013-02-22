#!/usr/bin/python
# -*- coding: utf-8 -*=
import time;
from datetime import datetime
class LogAssist:
    def getTime(self):
        today = datetime.today()
        dt = today.strftime('%Y%m%d%H%M%S')
        return dt
    def startTimer(self):
        self.start = time.time();
    def stopTimer(self):
        self.end = time.time();
    def timerDuration(self):
        self.process = self.end - self.start;
        self.h = int(self.process / 3600);
        self.process -= self.h * 3600;
        self.m = int(self.process / 60);
        self.process -= self.m * 60;
        self.s = self.process;
        t = "time: %dh %dm %fs" % (self.h, self.m, self.s)
        return t;
    
