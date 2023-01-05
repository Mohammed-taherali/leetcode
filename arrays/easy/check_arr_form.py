class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:

        for piece in pieces:
            if len(piece) == 1:
                if piece[0] not in arr:
                    return False

            else:
                try:
                    start = arr.index(piece[0])
                    end = arr.index(piece[-1])
                except ValueError:
                    return False    
                sub_arr = arr[start:end+1]
                if sub_arr != piece:
                    return False

        return True


arr = [91,4,64,78]
pieces = [[78],[4,64],[91]]

sol = Solution()
ans = sol.canFormArray(arr, pieces)
print(ans)

#         first_to_piece = {p[0]: p for p in pieces}
        
#         first = 0
#         while first < len(arr):    
#             if arr[first] not in first_to_piece:
#                 return False
            
#             piece = first_to_piece[arr[first]]
#             if arr[first:first + len(piece)] != piece:
#                 return False
            
#             first += len(piece)
            
#         return True