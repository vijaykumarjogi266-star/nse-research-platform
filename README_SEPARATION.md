# Separated
Equity: S01-S07 -> src/equity/strategies/
Options: S08-S14 -> src/options/strategies/
No cross-import allowed.
Test: from src.equity.strategies import REGISTRY (7)
      from src.options.strategies import REGISTRY (7)
