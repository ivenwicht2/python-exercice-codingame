from math import cos, hypot, radians
import sys
fl = lambda x: float(x.replace(',', '.'))
closest = sys.maxsize,''
l, p = fl(input()), fl(input())
for i in range(int(input())):
    number, name, address, phone, lon, lat = input().split(';')
    dl, dp = fl(lon) - l, fl(lat) - p
    closest = min(closest, (hypot(dl * cos(p + dp/2), dp), name))
print(closest[1])
