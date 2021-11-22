#! /usr/bin/env python3

import json
import subprocess

output = subprocess.getoutput("sensors -j")
lines = output.splitlines()
stdout = "".join("".join(lines).split("  "))

stdout = json.loads(stdout)
sensors = dict(stdout)

temperature = sensors["coretemp-isa-0000"]["Package id 0"]["temp1_input"]
temperature += sensors["coretemp-isa-0000"]["Core 0"]["temp2_input"]
temperature += sensors["coretemp-isa-0000"]["Core 1"]["temp3_input"]
temperature += sensors["coretemp-isa-0000"]["Core 2"]["temp4_input"]
temperature += sensors["coretemp-isa-0000"]["Core 3"]["temp5_input"]
temperature /= 5

print(str(temperature).split('.')[0])
