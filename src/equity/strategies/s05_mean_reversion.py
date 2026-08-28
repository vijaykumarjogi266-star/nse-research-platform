class S05_MeanReversion:
    id="S05"; name="Mean Reversion"
    def signal(self, df):
        if len(df)<30: return 0
        z = (df['close'].iloc[-1] - df['close'].rolling(20).mean().iloc[-1]) / df['close'].rolling(20).std().iloc[-1]
        if z<-2: return 1
        if z>2: return -1
        return 0
