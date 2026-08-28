import random
from src.strategies import STRATEGY_REGISTRY

class Series(list):
    def max(self): return max(self) if self else 0
    def min(self): return min(self) if self else 0
    def mean(self): return sum(self)/len(self) if self else 0

class Iloc:
    def __init__(self, data): self.data=data
    def __getitem__(self, k):
        if isinstance(k, slice): return FakeDF(self.data[k])
        return self.data[k]

class FakeDF:
    def __init__(self, rows):
        self._rows=rows
        self.iloc=Iloc(rows)
    def __len__(self): return len(self._rows)
    def __getitem__(self, key):
        if isinstance(key, str):
            return Series([r.get(key,0) for r in self._rows])
        return FakeDF(self._rows[key])

def gen_dummy(n=600, start=100):
    rows=[]; price=start
    for _ in range(n):
        price+=random.uniform(-1,1)
        o=price+random.uniform(-0.5,0.5)
        c=price+random.uniform(-0.5,0.5)
        h=max(o,c)+random.uniform(0,0.8)
        l=min(o,c)-random.uniform(0,0.8)
        rows.append({'open':o,'high':h,'low':l,'close':c,'volume':5000})
        price=c
    return rows

def backtest(strat, data):
    pnl=0.0; trades=0; pos=0
    for i in range(50, len(data)-1):
        fdf=FakeDF(data[:i])
        try: sig=strat.signal(fdf)
        except Exception: sig=0
        if sig and sig!=pos:
            ret=data[i+1]['close']-data[i]['close']
            if pos: pnl+=ret*pos
            pos=sig; trades+=1
    return pnl, trades

if __name__=="__main__":
    data=gen_dummy()
    print(f"Dummy: {len(data)} bars")
    for sid, Cls in STRATEGY_REGISTRY.items():
        pnl,trades=backtest(Cls(), data)
        print(f"{sid}: pnl={pnl:7.2f} trades={trades}")
