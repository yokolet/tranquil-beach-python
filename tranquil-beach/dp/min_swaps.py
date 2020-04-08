class MinSwaps:
    def minSwap(self, A: 'List[int]', B: 'List[int]') -> int:
        x, y = 0, 1 # x: no swap, y: swap
        for i in range(1, len(A)):
            if max(A[i-1], B[i-1]) < min(A[i], B[i]):
                x = y = min(x, y)
                y += 1
            elif A[i-1] < A[i] and B[i-1] < B[i]:
                y += 1
            else:
                x, y = y, x + 1
        return min(x, y)

    def minSwap2(self, A: 'List[int]', B: 'List[int]') -> int:
        # unswap represents the minimum value if we don't swap list[i]
        # swap represents the minimum value if we swap list[i]
        unswap, swap = 0, 1
        for i in range(1, len(A)):
            if min(A[i], B[i]) > max(A[i-1], B[i-1]):
                # no matter i-1 swap or not, i doesn't need to swap
                unswap = swap = min(unswap, swap)
                swap += 1
            elif A[i] > A[i-1] and B[i] > B[i-1]:
                # if i-1 swaps, then i must swap accordingly
                unswap, swap = unswap, swap + 1
            else:
                # if i-1 doesn't swap, then i must swap
                unswap, swap = swap, unswap + 1

        return min(unswap, swap)

    def minSwap3(self, A: 'List[int]', B: 'List[int]') -> int:
        x = 0 # not swapping at index i
        y = 1 # swapping at index i
        for i in range(1, len(A)):
            new_x = 1001
            new_y = 1001
            if A[i] > A[i-1] and B[i] > B[i-1]:
                new_x = min(new_x, x)
                new_y = min(new_y, y+1)
            if A[i] > B[i-1] and B[i] > A[i-1]:
                new_x = min(y, new_x)
                new_y = min(new_y, x+1)
            x = new_x
            y = new_y
        return min(x,y)
