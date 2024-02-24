# Development info

After publishing on PyPI, also do a GitHub release.

After the GitHub release, bump version number in the `Makefile` and `pyproject.toml`

Python packaging tutorials: https://packaging.python.org/en/latest/tutorials/



## Documentation

From the `docs` folder:
```bash
sphinx-apidoc -o source ../src/sbmlsh/
# to create stubs. Then
make clean
make html

xdg-open _build/html/index.html
```

