class NextClosestTime:
    def nextClosestTime(self, time: str) -> str:
        digits = {time[0], time[1], time[3], time[4]}
        times = [i+j+k+l for i in digits \
                        for j in digits \
                        for k in digits \
                        for l in digits \
                        if "0" <= i+j <= "23" and "0" <= k+l <= "59"]
        times.sort()
        t0 = time.replace(':', '')
        if times[-1] <= t0:
            result = times[0]
        else:
            idx = times.index(t0)
            result = times[idx+1]
        return result[:2] + ':' + result[2:]

    def nextClosestTime2(self, time: str) -> str:
        digits = [time[0], time[1], time[3], time[4]]
        ts = []
        queue = ['']
        while queue:
            s = queue.pop(0)
            if len(s) == 0:
                for d in digits:
                    if d in ['0', '1', '2']:
                        queue.append(s+d)
            elif len(s) == 1:
                for d in digits:
                    if s != '2' or (s == '2' and d in ['0', '1', '2', '3']):
                        queue.append(s+d)
            elif len(s) == 2:
                for d in digits:
                    if d in ['0', '1', '2', '3', '4', '5']:
                        queue.append(s+d)
            elif len(s) == 3:
                for d in digits:
                    queue.append(s+d)
            else:
                ts.append(s)
        factor = [60, 1]
        f = lambda t: sum([a*b for a, b in zip(factor, [int(t[:2]), int(t[2:])])])
        t0 = f(time.replace(':', ''))
        tt = {f(s): s for s in ts}
        if t0 >= max(tt.keys()):
            t0 -= 60*24
        min_time, min_diff = '', float('inf')
        for v, s in tt.items():
            if v <= t0: continue
            if v - t0 < min_diff:
                min_time = s
                min_diff = v - t0
        return min_time[:2]+':'+min_time[2:]
            

        