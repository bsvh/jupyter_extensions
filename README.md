# jupyter_extensions

This repository contains my extensions written for Jupyter and IPython.

## IPython

### scienceimports

Adds an IPython magic command to simplify writing command imports for
scientific programming in python. For example, typing the following
into ipython/qtconsole/jupyter-notebook

```
%scimp mpl, np, nl, pd
```

will result in the following code

```python
import matplotlib as mpl
from matplotlib import pyplot as plt

import pandas as pd
```

For more information, and to see the list of supported shortcuts,
type `%scimp help` into your ipython shell after installing the
extension.
