class Solution:

    def encode(self, strs: List[str]) -> str:
        s = 'vinay'.join(strs)
        if len(strs) == 0:
            s = 'ntohign'
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        lst =  s.split('vinay')
        if s == 'ntohign' :
            lst = []
        print(lst)
        return lst
        