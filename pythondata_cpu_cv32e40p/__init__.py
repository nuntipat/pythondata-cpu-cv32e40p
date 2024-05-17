import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40p.git"

# Module version
version_str = "0.0.post152"
version_tuple = (0, 0, 152)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post152")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10"
data_version_tuple = (0, 0, 10)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10")
except ImportError:
    pass
data_git_hash = "6adc6b3d71d93dfbb5006cd3fa095331df38e8fd"
data_git_describe = "v1.0.0_doc-564-g6adc6b3"
data_git_msg = """\
commit 6adc6b3d71d93dfbb5006cd3fa095331df38e8fd
Author: Davide Schiavone <davide@openhwgroup.org>
Date:   Wed Feb 14 14:07:20 2024 +0100

    Merge pull request #918 from openhwgroup/dev
    
    Automatic PR dev->master

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_cv32e40p."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_cv32e40p".format(f))
    return fn
