class S08_RangeFade:
    id="S08"; name="Range Fade"
    def signal(self, df):
        if len(df)<20: return 0
        high = df['high'].rolling(20).max().iloc[-1]
        low = df['low'].rolling(20).min().iloc[-1]
        c = df.iloc[-1]['close']
        mid = (high+low)/2
        return -1 if c>high*0.998 else 1 if c<low*1.002 else 0
