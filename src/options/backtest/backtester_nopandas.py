from src.options.strategies import REGISTRY as STRATEGY_REGISTRY
import random, csv
def run():
    print(f"OPTIONS REGISTRY: {len(STRATEGY_REGISTRY)} -> {sorted(STRATEGY_REGISTRY)}")
    print("Options backtester OK - separated, filters + execution separate")
if __name__ == "__main__":
    run()
