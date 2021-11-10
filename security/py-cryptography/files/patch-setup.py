diff --git setup.py.orig setup.py
index 74f69e71..b083387e 100644
--- setup.py.orig
+++ setup.py
@@ -10,22 +10,6 @@ import sys
 
 from setuptools import find_packages, setup
 
-try:
-    from setuptools_rust import RustExtension
-except ImportError:
-    print(
-        """
-        =============================DEBUG ASSISTANCE==========================
-        If you are seeing an error here please try the following to
-        successfully install cryptography:
-
-        Upgrade to the latest pip and try again. This will fix errors for most
-        users. See: https://pip.pypa.io/en/stable/installing/#upgrading-pip
-        =============================DEBUG ASSISTANCE==========================
-        """
-    )
-    raise
-
 
 base_dir = os.path.dirname(__file__)
 src_dir = os.path.join(base_dir, "src")
@@ -43,25 +27,7 @@ with open(os.path.join(src_dir, "cryptography", "__about__.py")) as f:
 # `pyproject.toml`
 setuptools_rust = "setuptools-rust>=0.11.4"
 install_requirements = ["cffi>=1.12"]
-setup_requirements = install_requirements + [setuptools_rust]
-
-if os.environ.get("CRYPTOGRAPHY_DONT_BUILD_RUST"):
-    rust_extensions = []
-else:
-    rust_extensions = [
-        RustExtension(
-            "_rust",
-            "src/rust/Cargo.toml",
-            py_limited_api=True,
-            # Enable abi3 mode if we're not using PyPy.
-            features=(
-                []
-                if platform.python_implementation() == "PyPy"
-                else ["pyo3/abi3-py36"]
-            ),
-            rust_version=">=1.41.0",
-        )
-    ]
+setup_requirements = install_requirements
 
 with open(os.path.join(base_dir, "README.rst")) as f:
     long_description = f.read()
@@ -149,7 +115,7 @@ try:
             "src/_cffi_src/build_openssl.py:ffi",
             "src/_cffi_src/build_padding.py:ffi",
         ],
-        rust_extensions=rust_extensions,
+        rust_extensions=[],
     )
 except:  # noqa: E722
     # Note: This is a bare exception that re-raises so that we don't interfere
