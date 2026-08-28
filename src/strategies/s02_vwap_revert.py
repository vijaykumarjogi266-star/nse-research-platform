class S02_VWAPRevert:
    id="S02"; name="VWAP Reversion"
    def signal(self, df):
        if len(df)<20: return 0
        vwap = (df['close']*df.get('volume',1)).rolling(20).mean() / df.get('volume',1).rolling(20).mean()
        # simplified
        close = df.iloc[-1]['close']
        sma = df['close'].rolling(20).mean().iloc[-1]
        if close < sma*0.99: return 1
        if close > sma*1.01: return -1
        return 0
