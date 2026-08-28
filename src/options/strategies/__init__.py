from importlib import import_module
from pathlib import Path
REGISTRY={}
for p in Path(__file__).parent.glob("s*.py"):
    mod = import_module(f"src.options.strategies.{p.stem}")
    for k,v in vars(mod).items():
        if k.upper().startswith("S") and isinstance(v, type):
            REGISTRY[k.upper()] = v
