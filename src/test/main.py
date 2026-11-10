"""Minimalist Hello World program adhering to the SDD Constitution.

Zero overengineering: outputs 'Hello World' directly to standard output
using Python's native print(), guarded by pure contract assertions.
"""

GREETING: str = "Hello World"


def main() -> None:
    """Execute the contract validation and emit Hello World to stdout."""
    # Contract Assertions (Phase 4 of SDD)
    assert isinstance(GREETING, str), "Contract violation: GREETING must be of type str"
    assert GREETING == "Hello World", "Contract violation: GREETING must equal 'Hello World'"
    assert not hasattr(GREETING, "rdd"), "Constitution violation: Spark RDD detected"
    assert not hasattr(GREETING, "_jdf"), "Constitution violation: Spark JVM DataFrame detected"

    # Minimalist Execution (Phase 3 of SDD)
    print(GREETING)


if __name__ == "__main__":
    main()
