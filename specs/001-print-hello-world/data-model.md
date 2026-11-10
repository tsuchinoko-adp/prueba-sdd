# Data Model: Print Hello World

**Feature**: `001-print-hello-world`
**Date**: 2026-11-09

## Entities

### GreetingMessage (`Mensaje de Saludo`)

Represents the immutable text payload emitted to standard output.

#### Attributes

| Attribute | Type | Nullable | Default | Description | Validation Rules |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `content` | `str` | No | `"Hello World"` | The exact text string of the greeting | Must be exact string `"Hello World"`, length == 11, UTF-8 encodable |

#### Invariants & Constraints

1. **Immutability**: Once defined, `content` cannot be modified or transformed.
2. **Type Safety**: Strictly a native Python `str`. No object wrapping, no Spark Column or Row representation.
3. **Purity**: Contains zero references to JVM, Spark, or Databricks context objects.

#### Lifecycle & State Transitions

```text
[Defined: content = "Hello World"]
            │
            ▼ (Contract Evaluation: assert checks pass)
[Validated]
            │
            ▼ (Side Effect: print(content))
[Emitted to stdout]
```
