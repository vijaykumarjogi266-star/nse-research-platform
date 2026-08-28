import pandas as pd
def backtest(df, strategy_cls):
    strat=strategy_cls()
    pnl=0
    trades=[]
    for i in range(20,len(df)):
        sig=strat.signal(df.iloc[:i])
        if sig!=0:
            ret=df['close'].iloc[i+1]-df['close'].iloc[i] if i+1<len(df) else 0
            pnl+=ret*sig
            trades.append((i,sig,ret))
    return {"pnl":pnl,"trades":len(trades)}
