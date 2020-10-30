import json

d={}
# d={"谦谦":{"sex":"男","addr":"北京","age":34},"千千":{"sex":"女","addr":"北京","age":34},}
d.update({"果果":{"sex":"男","addr":"四川","age":24}})
fw=open("user_nfo.json","w",encoding="utf-8")
json.dump(d,fw,ensure_ascii=False,indent=4)
fw.close()