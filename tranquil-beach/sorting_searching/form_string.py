from collections import defaultdict
class FormString:
    def shortestWay(self, source: str, target: str) -> int:
        idx, count = len(source), 0
        for i, c in enumerate(target):
            next_idx = source.find(c, idx+1)
            if next_idx != -1:
                idx = next_idx
                continue
            count += 1
            next_idx = source.find(c, 0)
            if next_idx == -1:
                return -1
            idx = next_idx
        return count

    def shortestWay2(self, source: str, target: str) -> int:
        m, n = len(source), len(target)
        c2i = defaultdict(list)
        for i in range(len(source)):
            c2i[source[i]].append(i)

        if target[0] not in c2i: return -1
        idx = c2i[target[0]][0]
        queue, result = [([[idx]], 1)], []
        while queue:
            seqs, t_idx = queue.pop(0)
            if t_idx >= n:
                result.append(len(seqs))
                continue
            if target[t_idx] not in c2i:
                continue
            s_idx = seqs[-1][-1]
            indices = [idx for idx in c2i[target[t_idx]] if idx > s_idx]
            if len(indices) > 0:
                seqs[-1].append(indices[0])
            else:
                seqs.append([c2i[target[t_idx]][0]])
            queue.append((seqs, t_idx+1))
        if len(result) == 0: return -1
        else: return min(result)