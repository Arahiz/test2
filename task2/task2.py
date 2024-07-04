import sys

c_file, p_file = sys.argv[1], sys.argv[2]

with open(c_file) as f1, open(p_file) as f2:
    x0, y0 = map(float, f1.readline().strip().split())
    R_2 = float(f1.readline().strip()) ** 2
    e = 10**-10
    for st in f2:
        x1, y1 = map(float, st.strip().split())
        d = (x1 - x0)**2 + (y1 - y0)**2
        if abs(d - R_2) < e:
            print(0, end='\n')
        elif d < R_2:
            print(1, end='\n')
        else:
            print(2, end='\n')
