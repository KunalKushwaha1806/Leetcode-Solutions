class Solution:
    def evaluate(self, s: str, d: List[List[str]]) -> str:
        return re.sub(r'\((\w+)\)',lambda m,d=dict(d):d.get(m[1],'?'),s)