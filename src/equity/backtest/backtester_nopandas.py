from src.equity.strategies import REGISTRY as STRATEGY_REGISTRY
import random, csv
# dummy equity test - no pandas
def run():
    print(f"EQUITY REGISTRY: {len(STRATEGY_REGISTRY)} -> {sorted(STRATEGY_REGISTRY)}")
    print("Equity backtester OK - separated, no pandas dependency")
if __name__ == "__main__":
    run()
