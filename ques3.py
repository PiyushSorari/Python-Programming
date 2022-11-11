#* ABC is a right triangle, 90° at B.
#Therefore, ABC = 90°.
#Point M is the midpoint of hypotenuse AC.
#You are given the lengths AB and BC.
#Your task is to find MBC (angle, as shown in the figure) in degrees.
import math

AB = int(input())
BC = int(input())

H = math.sqrt(AB**2 + BC**2)
H = H/2.0
adj = BC/2.0

Output = int(round(math.degrees(math.acos(adj/H))))

Output = str(Output)

print(Output+chr(176))