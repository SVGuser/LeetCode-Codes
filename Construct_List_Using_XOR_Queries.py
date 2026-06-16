class Solution:
  def constructList(self, queries):
    arr = [0]
    the_xor = 0
    for q in queries:
      if q[0] == 0:
        arr.append(q[1] ^ the_xor)
      else:
        the_xor ^= q[1]
        arr = [num ^ the_xor for num in arr]
      return sorted(arr)
