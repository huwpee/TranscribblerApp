# TranscribblerApp5.spec
import os
import speechbrain
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

try:
    from PyInstaller.utils.hooks import Tree
except ImportError:
    def Tree(src, prefix):
        items = []
        for root, dirs, files in os.walk(src):
            rel = os.path.relpath(root, src)
            for fn in files:
                src_path = os.path.join(root, fn)
                dst_dir = prefix if rel in (".", os.curdir) else os.path.join(prefix, rel)
                items.append((src_path, dst_dir))
        return items

block_cipher = None
HERE = os.getcwd()

datas = [
    ("config.ini", "."),
    ("diarize.py", "."),
]

datas += collect_data_files("whisper")
datas += collect_data_files("lightning_fabric")

sb_pkg_dir = os.path.dirname(speechbrain.__file__)
datas += Tree(sb_pkg_dir, prefix="speechbrain")

hiddenimports = [
    "pkg_resources.py2_warn",
    "rich",
    "packaging.version",
] + collect_submodules("pyannote.audio")

hook_dir = os.path.join(HERE, "hooks")
runtime_hooks = [
    os.path.join(hook_dir, "packaging_patch.py"),
    os.path.join(hook_dir, "patch_speechbrain_importutils.py"),
]

a = Analysis(
    ["main.py"],
    pathex=[HERE],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[hook_dir],
    runtime_hooks=runtime_hooks,
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="TranscribblerApp",
    debug=False,
    strip=False,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name="TranscribblerApp",
)