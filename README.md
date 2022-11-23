# Quick Start

Ecosystem Plugin for Milkomeda A1 support in Ape

## Dependencies

* [python3](https://www.python.org/downloads) version 3.8 or greater, python3-dev

## Installation

### via `ape`

You can install this plugin using `ape`:

```bash
ape plugins install milkomeda
```

or via config file:

```yaml
# ape-config.yaml
plugins:
  - name: milkomeda
```

### via `pip`

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install ape-milkomeda
```

### via `setuptools`

You can clone the repository and use [`setuptools`](https://github.com/pypa/setuptools) for the most up-to-date version:

```bash
git clone https://github.com/nhaga/ape-milkomeda.git
cd ape-milkomeda
python3 setup.py install
```

## Quick Usage

Installing this plugin adds support for the Milkomeda ecosystem:

```bash
ape console --network milkomeda:a1
```

## Development

Comments, questions, criticisms and pull requests are welcomed.
