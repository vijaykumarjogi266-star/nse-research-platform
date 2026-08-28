class S09_VolFilter:
    id="S09"; name="Volatility Filter"
    def filter(self, df, signal):
        if len(df)<20: return False
        atr = (df['high']-df['low']).rolling(14).mean().iloc[-1]
        return atr/df.iloc[-1]['close'] > 0.003 # only trade if vol enough
