from src.strategies import STRATEGY_REGISTRY
class Runner:
    def run_all(self, df):
        results={}
        for sid, cls in STRATEGY_REGISTRY.items():
            inst=cls()
            if hasattr(inst,'signal'):
                results[sid]=inst.signal(df)
        return results
