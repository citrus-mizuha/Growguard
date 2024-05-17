import os
import radef

a = str(os.system("less update-log.log | grep updated"))
print(a)