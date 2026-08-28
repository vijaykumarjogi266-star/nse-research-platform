class S10_RegimeFilter:
    id="S10"; name="Regime Filter"
    def filter(self, df, signal):
        if len(df)<50: return False
        adx = df['close'].diff().abs().rolling(14).mean().iloc[-1] # simplified
        return True
