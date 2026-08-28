import random
from src.strategies import STRATEGY_REGISTRY

class Series(list):
    def max(self): return max(self) if self else 0
    def min(self): return min(self) if self else 0
    def mean(self): return sum(self)/len(self) if self else 0
    def rolling(self, n): return self # stub
    @property
    def iloc(self): return self

class FakeDF:
    def __init__(self, rows): self._rows=rows
    def __len__(self): return len(self._rows)
    def __getitem__(self, key):
        if isinstance(key,str):
            return Series([r.get(key,0) for r in self._rows])
        return FakeDF(self._rows[key])
    @property
    def iloc(self):
        class I:
            def __init__(self, d): self.d=d
            def __getitem__(self, k):
                if isinstance(k,slice): return FakeDF(self.d._rows[k])
                return self.d._rows[k]
        return I(self)

#... rest same as before - keep your working version for now
