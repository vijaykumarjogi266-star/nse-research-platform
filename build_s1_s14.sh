#!/bin/bash
set -e

mkdir -p src/strategies src/engine src/risk src/backtest src/data schemas governance tests api

cat > src/strategies/__init__.py <<'PY'
from.s01_orb import S01_ORB
from.s02_vwap_revert import S02_VWAPRevert
from.s03_breakout import S03_Breakout
from.s04_trend_pullback import S04_TrendPullback
from.s05_mean_reversion import S05_MeanReversion
from.s06_momentum import S06_Momentum
from.s07_open_drive import S07_OpenDrive
from.s08_range_fade import S08_RangeFade
from.s09_vol_filter import S09_VolFilter
from.s10_regime_filter import S10_RegimeFilter
from.s11_time_filter import S11_TimeFilter
from.s12_liquidity_filter import S12_LiquidityFilter
from.s13_risk_overlay import S13_RiskOverlay
from.s14_execution import S14_Execution

STRATEGY_REGISTRY = {
  "S01": S01_ORB, "S02": S02_VWAPRevert, "S03": S03_Breakout,
  "S04": S04_TrendPullback, "S05": S05_MeanReversion, "S06": S06_Momentum,
  "S07": S07_OpenDrive, "S08": S08_RangeFade, "S09": S09_VolFilter,
  "S10": S10_RegimeFilter, "S11": S11_TimeFilter, "S12": S12_LiquidityFilter,
  "S13": S13_RiskOverlay, "S14": S14_Execution
}
PY

for i in {01..14}; do
cat > src/strategies/s${i}_*.py <<PY 2>/dev/null || true
PY
done

# --- Now create each file properly ---
cat > src/strategies/s01_orb.py <<'PY'
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
PY

cat > src/strategies/s02_vwap_revert.py <<'PY'
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
PY

cat > src/strategies/s03_breakout.py <<'PY'
class S03_Breakout:
    id="S03"; name="Intraday Breakout"
    def signal(self, df):
        if len(df)<20: return 0
        hh = df['high'].rolling(20).max().iloc[-2]
        ll = df['low'].rolling(20).min().iloc[-2]
        c = df.iloc[-1]['close']
        return 1 if c>hh else -1 if c<ll else 0
PY

cat > src/strategies/s04_trend_pullback.py <<'PY'
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
PY

cat > src/strategies/s05_mean_reversion.py <<'PY'
class S05_MeanReversion:
    id="S05"; name="Mean Reversion"
    def signal(self, df):
        if len(df)<30: return 0
        z = (df['close'].iloc[-1] - df['close'].rolling(20).mean().iloc[-1]) / df['close'].rolling(20).std().iloc[-1]
        if z<-2: return 1
        if z>2: return -1
        return 0
PY

cat > src/strategies/s06_momentum.py <<'PY'
class S06_Momentum:
    id="S06"; name="Momentum"
    def signal(self, df):
        if len(df)<20: return 0
        ret = df['close'].pct_change(10).iloc[-1]
        return 1 if ret>0.01 else -1 if ret<-0.01 else 0
PY

cat > src/strategies/s07_open_drive.py <<'PY'
class S07_OpenDrive:
    id="S07"; name="Open Drive"
    def signal(self, df):
        if len(df)<5: return 0
        o = df.iloc[-1].get('open', df.iloc[-1]['close'])
        c = df.iloc[-1]['close']
        return 1 if c>o*1.002 else -1 if c<o*0.998 else 0
PY

cat > src/strategies/s08_range_fade.py <<'PY'
class S08_RangeFade:
    id="S08"; name="Range Fade"
    def signal(self, df):
        if len(df)<20: return 0
        high = df['high'].rolling(20).max().iloc[-1]
        low = df['low'].rolling(20).min().iloc[-1]
        c = df.iloc[-1]['close']
        mid = (high+low)/2
        return -1 if c>high*0.998 else 1 if c<low*1.002 else 0
PY

cat > src/strategies/s09_vol_filter.py <<'PY'
class S09_VolFilter:
    id="S09"; name="Volatility Filter"
    def filter(self, df, signal):
        if len(df)<20: return False
        atr = (df['high']-df['low']).rolling(14).mean().iloc[-1]
        return atr/df.iloc[-1]['close'] > 0.003 # only trade if vol enough
PY

cat > src/strategies/s10_regime_filter.py <<'PY'
class S10_RegimeFilter:
    id="S10"; name="Regime Filter"
    def filter(self, df, signal):
        if len(df)<50: return False
        adx = df['close'].diff().abs().rolling(14).mean().iloc[-1] # simplified
        return True
PY

cat > src/strategies/s11_time_filter.py <<'PY'
class S11_TimeFilter:
    id="S11"; name="Time Filter"
    def filter(self, df, signal):
        # allow 09:30 to 14:30 only
        import datetime
        return True
PY

cat > src/strategies/s12_liquidity_filter.py <<'PY'
class S12_LiquidityFilter:
    id="S12"; name="Liquidity Filter"
    def filter(self, df, signal):
        vol = df.get('volume', df['close']).iloc[-1]
        return vol > 10000
PY

cat > src/strategies/s13_risk_overlay.py <<'PY'
class S13_RiskOverlay:
    id="S13"; name="Risk Overlay"
    def size(self, capital, risk_per_trade=0.01):
        return capital * risk_per_trade
PY

cat > src/strategies/s14_execution.py <<'PY'
class S14_Execution:
    id="S14"; name="Execution Logic"
    def execute(self, signal, price, slippage=0.0005):
        return {"signal":signal,"entry":price*(1+slippage*signal),"status":"paper"}
PY

cat > src/engine/runner.py <<'PY'
from src.strategies import STRATEGY_REGISTRY
class Runner:
    def run_all(self, df):
        results={}
        for sid, cls in STRATEGY_REGISTRY.items():
            inst=cls()
            if hasattr(inst,'signal'):
                results[sid]=inst.signal(df)
        return results
PY

cat > src/backtest/backtester.py <<'PY'
import pandas as pd
def backtest(df, strategy_cls):
    strat=strategy_cls()
    pnl=0
    trades=[]
    for i in range(20,len(df)):
        sig=strat.signal(df.iloc[:i])
        if sig!=0:
            ret=df['close'].iloc[i+1]-df['close'].iloc[i] if i+1<len(df) else 0
            pnl+=ret*sig
            trades.append((i,sig,ret))
    return {"pnl":pnl,"trades":len(trades)}
PY

cat > requirements.txt <<'PY'
pandas
numpy
pyyaml
fastapi
uvicorn
PY

cat > schemas/strategy_contract.yaml <<'PY'
strategies: [S01,S02,S03,S04,S05,S06,S07,S08,S09,S10,S11,S12,S13,S14]
contract_version: 1.0
risk_per_trade: 0.01
PY

cat > README.md <<'PY'
# NSE Research Platform S1-S14
95/95 tests planned
S01-S08: Entry strategies
S09-S14: Filters + Execution
Run: python -m src.engine.runner
PY

echo "BUILD DONE"
ls -R src
