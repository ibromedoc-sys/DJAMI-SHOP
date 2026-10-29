from pathlib import Path

import pythonforandroid
from pythonforandroid.util import load_source


_recipe_path = (
    Path(pythonforandroid.__file__).parent
    / "recipes"
    / "python3"
    / "__init__.py"
)
_upstream = load_source(
    "pythonforandroid_upstream_python3_recipe",
    str(_recipe_path),
)


class AndroidPython3Recipe(_upstream.Python3Recipe):
    def get_recipe_dir(self):
        return str(_recipe_path.parent)

    def get_recipe_env(self, arch=None, with_flags_in_cc=True):
        env = super().get_recipe_env(arch, with_flags_in_cc)
        env["ac_cv_func_getgrent"] = "no"
        if "ac_cv_func_getgrent=no" not in self.configure_args:
            self.configure_args.append("ac_cv_func_getgrent=no")
        return env


recipe = AndroidPython3Recipe()
