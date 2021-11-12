# Author: IBN (AMDG) 11/12/2021

colors = ["red", "blue", "yellow", "green"]

colors.extend(["orange", "indigo", "violet"])
print(colors)

print(colors.count("yellow"))

colors.insert(3, "teal")
print(colors)

colors.clear()
print(colors)

print(colors.count("red"))
