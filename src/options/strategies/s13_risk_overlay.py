class S13_RiskOverlay:
    id="S13"; name="Risk Overlay"
    def size(self, capital, risk_per_trade=0.01):
        return capital * risk_per_trade
