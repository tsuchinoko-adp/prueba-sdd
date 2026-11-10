# Interface Contract: Standard Output Greeting

**Feature**: `001-print-hello-world`
**Interface Type**: CLI / Notebook Standard Output (`sys.stdout`)

## 1. Interface Signature

### Python Execution Contract

```python
def main() -> None:
    """Emits 'Hello World' to standard output using native print()."""
```

## 2. Input / Output Specifications

### Inputs
- **Arguments**: None (`*args = ()`, `**kwargs = {}`)
- **Environment Variables**: None required
- **Interactive Input**: None (`sys.stdin` is not accessed)

### Outputs
- **Channel**: `sys.stdout`
- **Payload**: `"Hello World\n"` (12 bytes including standard newline)
- **Exit Code**: `0` on successful completion

## 3. Preconditions & Postconditions

### Preconditions (Contract Assertions)
Before calling `print()`, the following assertions MUST pass:
```python
assert isinstance(mensaje, str), "Message must be a string"
assert mensaje == "Hello World", "Message content must be 'Hello World'"
assert "pyspark" not in globals(), "Environment must not import pyspark globally"
```

### Postconditions
- Exactly one line containing `"Hello World"` written to the output stream.
- Zero mutations to global or cluster state.
- No DataFrame jobs triggered on Databricks cluster nodes.
