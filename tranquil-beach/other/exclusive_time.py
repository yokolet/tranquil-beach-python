class ExclusiveTime:
    def exclusiveTime(self, n: int, logs: 'List[str]') -> 'List[int]':
        result = [0 for _ in range(n)]
        f_id, event, t = logs[0].split(":")
        prev_t = int(t)
        stack = [int(f_id)]
        for log in logs:
            f_id, event, t = log.split(":")
            cur_t = int(t)
            if event == "start":
                result[stack[-1]] += cur_t - prev_t
                stack.append(int(f_id))
                prev_t = cur_t
            else:
                result[stack[-1]] += cur_t - prev_t + 1
                stack.pop()
                prev_t = cur_t + 1
        return result