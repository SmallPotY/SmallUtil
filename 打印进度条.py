# -*- coding:utf-8 -*-

import time
import sys

for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write("%s%% |%s" % (int(i % 101), int(i % 101) * '#'))
    sys.stdout.flush()
    time.sleep(0.5)

sys.stdout.write('\n')