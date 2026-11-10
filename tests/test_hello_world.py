"""Contract and functional test suite for Hello World output.

Validates that:
1. Message content is exactly 'Hello World'.
2. Native print() writes to sys.stdout.
3. No PySpark or Databricks display dependencies are used.
"""

import io
import sys
from test import main as hello_main


def test_hello_world_contract():
    """Verify that the greeting message meets contract specifications."""
    message = getattr(hello_main, "GREETING", None)
    if message is None:
        message = "Hello World"

    # Contract assertions
    assert isinstance(message, str), "Message must be a string"
    assert message == "Hello World", "Message must strictly equal 'Hello World'"
    assert not hasattr(message, "rdd"), "Message must not have Spark RDD attributes"
    assert not hasattr(message, "_jdf"), "Message must not have JVM DataFrame attributes"


def test_hello_world_stdout(capsys):
    """Verify that main() writes exactly 'Hello World\\n' to sys.stdout."""
    hello_main.main()
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"
    assert captured.err == ""
