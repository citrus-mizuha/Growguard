import radef
import os
import time
import subprocess
from datetime import datetime, timedelta

update_cashes_file = "update-log.log"
py_v = radef.py_v()
today = datetime.now()
acceptable_days = [today.strftime("%Y/%m/%d")]
for i in range(1, 6):
    day = today - timedelta(days=i)
    acceptable_days.append(day.strftime("%Y/%m/%d"))

print(py_v)
first = float(time.perf_counter())
print("Process Start : " + radef.timestamp(0))

output = subprocess.check_output('less update-log.log | grep updated', shell=True, text=True)

# acceptable_daysのいずれかがoutputに含まれているかをチェック
if not any(day in output for day in acceptable_days):
    radef.pip_update()
    radef.repository_update()
    with open(update_cashes_file, "a") as f:
        print(radef.timestamp(0) + " updated", file=f)
else:
    print("Update process was skipped.")
    with open(update_cashes_file, "a") as f:
        print(radef.timestamp(0) + " skipped", file=f)


end = float(time.perf_counter())
diff = end - first
minutes = int(round(diff // 60, 1))
seconds = int(round(diff % 60, 1))
print("Process End : " + radef.timestamp("ymd") + "\ntime taken : " + str(minutes) + "m " + str(seconds) + "s")
