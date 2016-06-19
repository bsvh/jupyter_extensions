#!/usr/bin/env python
# -*- coding: utf-8 -*-

from IPython.core.magic import line_magic, Magics, magics_class 

@magics_class
class ScienceImports(Magics):
    """Provides IPython magic for scientific imports."""

    known = { 
            "mpl": "import matplotlib as mpl",
            "pd": "import pandas as pd",
            "np": "import numpy as np",
            "plt": "from matplotlib import pyplot as plt",
            "sns": "import seaborn as sns",
            "nl": ""
    }

    def __dir__(self):
        return self.known.keys()

    def help(self):
        """Print out a help message."""

        print("%scimp [argument|key1,key2,...keyn]\n")
        print("Arguments")
        print("---------")
        print("  help: Print this help message.")
        print("  list: List known keywords and their imports.\n")

        self.list()

    def list(self):
        """Print a list of known keywords and their imports."""

        print("Keywords")
        print("--------")
        for key, val in self.known.items():
            if key != "nl":
                print("  {}: {}".format(key, val))
        print("  nl: Adds a newline.")

    @line_magic
    def scimp(self, line):
        """Replace the current input with imports specified by a list of
        keywords.

        Parameters
        ----------
        line : string
            A comma seperated list of keywords corresponding to keywords
            associated with each import, where the keyword is the usual
            alias given to an import. Additionally, a newline can be added
            with the nl keyword.

            To see a list of keywords and their corresponding imports, the
            ``list`` parameter can be given.

        Examples
        --------
        To import matplotlib, pyplot, and pandas, the following will work:

        >>> %scimp mpl, plt, nl, pd

        This will replace the current import with the following::
        
            import matplotlib as mpl
            from matplotlib import pyplot as plt

            import pandas as pd

        """


        imports = []
        for key in (x.strip() for x in line.split(",")):
            if key in ("help", "list"):
                getattr(self, key)()
                break
            elif key not in self.known:
                print("No import is defined for keyword '{}'".format(key))
                break
            else:
                imports.append(self.known[key])
        else:
            self.shell.set_next_input("\n".join(imports), replace=True)

def load_ipython_extension(ipython):
    ipython.register_magics(ScienceImports)
