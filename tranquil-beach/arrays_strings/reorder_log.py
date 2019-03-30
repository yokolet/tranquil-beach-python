from collections import defaultdict

class ReorderLog:
    def reorderLogFiles(self, logs: 'List[str]') -> 'List[str]':
        def key_f(log):
            id_, rest = log.split(' ', 1)
            if rest[0].isdigit():
                return (1,)
            else:
                return (0, rest, id_)
        return sorted(logs, key=key_f)

    def reorderLogFiles1(self, logs: 'List[str]') -> 'List[str]':
        digits = []
        letters = []
        for log in logs:
            id_, rest = log.split(' ', 1)
            if rest[0].isdigit():
                digits.append(log)
            else:
                letters.append((log, rest, id_))
        return [log for log, _, _ in sorted(letters, key=lambda x: (x[1], x[2]))] + digits
