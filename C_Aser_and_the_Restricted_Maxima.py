import sys
input_data = sys.stdin.read().split()

t = int(input_data[0])
idx = 1

out = []
for _ in range(t):
    n = int(input_data[idx])
    k = int(input_data[idx+1])
    s = input_data[idx+2]
    idx += 3
    
    mx_streak = 0
    curr = 0
    for ch in s:
        if ch == '1':
            curr += 1
            if curr > mx_streak:
                mx_streak = curr
        else:
            curr = 0
            
    if mx_streak >= k:
        out.append("NO")
        continue
        
    out.append("YES")
    
    z = s.count('0')
    hi = n
    lo = n - z
    
    res = []
    for ch in s:
        if ch == '0':
            res.append(str(hi))
            hi -= 1
        else:
            res.append(str(lo))
            lo -= 1
            
    out.append(" ".join(res))
    
print('\n'.join(out))