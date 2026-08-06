class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for p, s in pair:
            stack.append(((target - p) / s, p))
            if len(stack) >= 2 and stack[-1][0] <= stack[-2][0]:
                stack.pop()
        
        print(stack)
        return len(stack)