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
