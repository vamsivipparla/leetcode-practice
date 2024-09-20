class Solution:

    def encode(self, strs):
        ct=''
        for i in range(0,len(strs)):
            if i==0:
                ct=ct+strs[i]
            else:
                ct=ct+'$'+strs[i]
        return ct
    


    def decode(self, s):

        lst=s.split('$')
        return lst




strs=["neet","code","love","you"]
obj = Solution()
en=obj.encode(strs)
ret=obj.decode(en)
print (ret)


'''
optimized
class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res


'''