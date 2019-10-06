class LargestNumber:
    def largestNumber(self, nums: 'List[int]') -> str:

        class Comparator(str):
            def __lt__(self, o):
                return self+o > o+self

        strs = sorted(map(str, nums), key=Comparator)
        return str(int(''.join(strs)))

    def largestNumber2(self, nums: 'List[int]') -> str:
        strs = list(map(str, nums))

        def mergeSort(a):
            if len(a) > 1:
                mid = len(a) // 2
                left, right = a[:mid], a[mid:]

                mergeSort(left)
                mergeSort(right)

                i, l, r = 0, 0, 0
                while l < len(left) and r < len(right):
                    if left[l]+right[r] > right[r]+left[l]:
                        a[i] = left[l]
                        l += 1
                    else:
                        a[i] = right[r]
                        r += 1
                    i += 1
                while l < len(left):
                    a[i] = left[l]
                    l += 1
                    i += 1
                while r < len(right):
                    a[i] = right[r]
                    r += 1
                    i += 1

        mergeSort(strs)
        return str(int(''.join(strs)))
