class S03_Breakout:
    id="S03"; name="Intraday Breakout"
    def signal(self, df):
        if len(df)<20: return 0
        hh = df['high'].rolling(20).max().iloc[-2]
        ll = df['low'].rolling(20).min().iloc[-2]
        c = df.iloc[-1]['close']
        return 1 if c>hh else -1 if c<ll else 0
