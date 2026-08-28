class S01_ORB:
    """Opening Range Breakout - 09:15-09:45 range break"""
    id="S01"; name="Opening Range Breakout"
    def signal(self, df):
        # df needs high, low, close
        if len(df)<50: return 0
        orb_high = df.iloc[-45:-30]['high'].max() if len(df)>45 else df['high'].max()
        orb_low = df.iloc[-45:-30]['low'].min() if len(df)>45 else df['low'].min()
        close = df.iloc[-1]['close']
        if close > orb_high: return 1
        if close < orb_low: return -1
        return 0
