class ValidSquare:
    def validSquare(self, p1: 'List[int]', p2: 'List[int]',
                        p3: 'List[int]', p4: 'List[int]') -> bool:
        def dist(a, b):
            return (a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])

        dists = [dist(p1, p2), dist(p1, p3), dist(p1, p4),
                    dist(p2, p3), dist(p2, p4), dist(p3, p4)]
        dists.sort(reverse=True)
        # 2 diagonals and 4 sides
        if dists[0] != 0 and dists[0] == dists[1] and\
            dists[5] != 0 and dists[5] == dists[2] and\
            dists[5] == dists[3] and dists[5] == dists[4]:
            return True
        else:
            return False

    def validSquare1(self, p1: 'List[int]', p2: 'List[int]',
                        p3: 'List[int]', p4: 'List[int]') -> bool:
        if p1 == p2 == p3 == p4: return False

        def dist(a, b):
            return (a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])
        
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
        return dist(p1, p4) == dist(p2, p3) and \
            dist(p1, p2) == dist(p1, p3)
