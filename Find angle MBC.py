#-*- coding: utf-8 -*-
import sys
import math

ab, bc = map(int, [input(), input()])
answer = u'%.0f\N{DEGREE SIGN}' % math.degrees(math.atan(ab/bc))
sys.stdout.buffer.write(answer.encode('utf-8'))
