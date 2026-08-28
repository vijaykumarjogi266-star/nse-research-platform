class S04_TrendPullback:
    id="S04"; name="Trend Pullback"
    def signal(self, df):
        if len(df)<50: return 0
        ema20 = df['close'].ewm(20).mean().iloc[-1]
        ema50 = df['close'].ewm(50).mean().iloc[-1]
        c = df.iloc[-1]['close']
        if ema20>ema50 and c<ema20: return 1
        if ema20<ema50 and c>ema20: return -1
        return 0
