class S12_LiquidityFilter:
    id="S12"; name="Liquidity Filter"
    def filter(self, df, signal):
        vol = df.get('volume', df['close']).iloc[-1]
        return vol > 10000
