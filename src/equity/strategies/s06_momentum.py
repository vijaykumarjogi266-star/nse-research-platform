class S06_Momentum:
    id="S06"; name="Momentum"
    def signal(self, df):
        if len(df)<20: return 0
        ret = df['close'].pct_change(10).iloc[-1]
        return 1 if ret>0.01 else -1 if ret<-0.01 else 0
