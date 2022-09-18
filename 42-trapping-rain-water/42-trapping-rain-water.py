class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        result = 0
        max_left = height[0]
        max_right = height[-1]
        meet_point = height.index(max(height))
        for x in range(1, meet_point):
            current_bar_height = height[x]
            if current_bar_height >= max_left:
                max_left = current_bar_height
            else:
                result += max_left - current_bar_height
        for x in range(len(height)-1, meet_point, -1):
            current_bar_height = height[x]
            if current_bar_height >= max_right:
                max_right = current_bar_height
            else:
                result += max_right - current_bar_height
        return result