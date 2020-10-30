# voted={}
#
# def check_voter(name):
#     if voted.get(name):
#         print("kick them out")
#     else:
#         print("let him vote")
#
# check_voter("tom")
# check_voter("mike")
# check_voter("mike")

# the costs table
infinity=float("inf")
costs={}
costs["a"]=6
costs["b"]=2
costs["fin"]=infinity
print(costs)

for i in costs:
    print(i)

for j in costs.keys():
    print(j)

for value in costs.values():
    print(value)