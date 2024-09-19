class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a=dict()
        b=dict()

        for i in range(0,len(s)):
            if s[i] in a:
                a[s[i]]=a[s[i]]+1
            else:
                a[s[i]]=1
        for i in range(0,len(t)):
            if t[i] in b:
                b[t[i]]=b[t[i]]+1
            else:
                b[t[i]]=1 

        
        if len(a)!=len(b):
            return False
        else:
            for key in a:
                 if key not in b or a[key]!=b[key] :
                      return False
            return True
        
'''
optimized
1)
        # If the lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Initialize a list of size 26 to count frequencies of each letter
        count = [0] * 26
        
        # Iterate through each character in both strings
        for i in range(len(s)):
            # Increment the count for the character in string s
            count[ord(s[i]) - ord('a')] += 1
            # Decrement the count for the character in string t
            count[ord(t[i]) - ord('a')] -= 1
        
        # If all counts are 0, the strings are anagrams
        for c in count:
            if c != 0:
                return False
        
        return True
2)
return all([s.count(c)==t.count(c) for c in string.ascii_lowercase])
'''