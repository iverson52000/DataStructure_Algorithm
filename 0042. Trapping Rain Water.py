"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.
"""

#Two Pointers

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        res = 0
        left = 0; right = len(height)-1
        left_height_max = right_height_max = 0
        while left < right:
            if height[left] < height[right]:
                left_height_max = max(left_height_max, height[left])
                res += left_height_max-height[left]
                left += 1
            else:
                right_height_max = max(right_height_max, height[right])
                res += right_height_max-height[right]
                right -= 1
        return res 

#Stack
        
class Solution:
    def trap(self, height: List[int]) -> int:
        s = []
        i = 0
        res = 0
        while i < len(height):
            if not s or height[i] <= height[s[-1]]:
                s.append(i)
                i += 1
            else:
                i_pop = s.pop(-1)
                if not s: continue	# i doesn’t change!!
                res += (min(height[i], height[s[-1]])-height[i_pop])*(i-s[-1]-1)
        return res


#java stack
class Solution {
    public int trap(int[] height) {
        Stack<Integer> stack = new Stack<>();
        int res = 0;
        
        for (int i = 0; i < height.length; i++) {
            // Maintain heights in stack are decreasing
            while (!stack.isEmpty() &&  height[i] > height[stack.peek()]) {
                int bottom = stack.pop();
                if (stack.isEmpty()) break;
                int left = stack.peek();
                int water = (Math.min(height[i], height[left])-height[bottom])*(i-left-1);
                res += water;
            }
            stack.push(i);
        }
        
        return res;
    }
}

