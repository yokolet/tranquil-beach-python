class FloodFill:
    def floodFill(self, image: 'List[List[int]]', sr: int, sc: int, newColor: int) -> 'List[List[int]]':
        if not image or not image[0]: return []
        m, n, color = len(image), len(image[0]), image[sr][sc]
        if color == newColor: return image
        stack = [[sr, sc]]
        image[sr][sc] = newColor
        while stack:
            cur_r, cur_c = stack.pop()
            for i, j in [[cur_r-1, cur_c], [cur_r, cur_c-1], [cur_r, cur_c+1], [cur_r+1, cur_c]]:
                if 0 <= i < m and 0 <= j < n and image[i][j] == color:
                    image[i][j] = newColor
                    stack.append([i, j])
        return image
