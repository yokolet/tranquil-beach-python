class ExclusiveTime:
    def exclusiveTime(self, n: int, logs: 'List[str]') -> 'List[int]':
        result = [0] * n
        f, event, t = logs[0].split(":")
        unit = int(t)
        stack = [int(f)]
        for log in logs:
            f, event, t = log.split(":")
            t_ = int(t)
            if event == "start":
                result[stack[-1]] += t_ - unit
                stack.append(int(f))
                unit = t_
            else:
                result[stack[-1]] += t_ - unit + 1
                stack.pop()
                unit = t_ + 1
        return result