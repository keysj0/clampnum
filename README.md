# clampnum

Keep a number inside an inclusive range.

```python
from clampnum import clamp, within, overflow, clamp_all

clamp(11, 0, 10)  # 10
within(5, 0, 10)  # True
overflow(11, 0, 10)  # 1
```

```bash
python -m unittest test_clampnum.py
```

MIT
