# clampnum

Keep a number inside an inclusive range.

```python
from clampnum import clamp, within

clamp(11, 0, 10)  # 10
within(5, 0, 10)  # True
```

```bash
python -m unittest test_clampnum.py
```

MIT
