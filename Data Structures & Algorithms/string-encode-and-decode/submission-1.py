class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'ntohign'
        return '$$'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == 'ntohign' :
            return []
        return s.split('$$')
        