import os
import json


main="darknet.exe detector test data/coco.data yolov3.cfg yolov3.weights -i 0 -thresh 0.25 people.jpg -ext_output"
f=os.popen(main)
data=f.readlines()
f.close()
print(data)
count=0
for value in data:
    if "%" in value:
        count+=1

x={"people":count}

with open("record.json","w") as f:
    json.dump(x,f)
