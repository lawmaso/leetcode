#!/usr/bin/env bash
#
# create.sh
#
# Generates a Python boilerplate file containing a TreeNode class
# and a Solution class with a method stub.
#
# Usage:
#   ./create.sh <output_file> <method_signature>
#
# Example:
#   ./create.sh solution.py "goodNodes(self, root: TreeNode | None) -> int"

set -euo pipefail

if [[ $# -lt 2 ]]; then
    echo "Usage: $0 <output_file> <method_signature>"
    echo 'Example: ./create question.py "fn(self, tree: TreeNode | None) -> int"'
    exit 1
fi

OUTPUT_FILE="$1"
METHOD_SIGNATURE="$2"

if [[ -e "$OUTPUT_FILE" ]]; then
    read -r -p "'$OUTPUT_FILE' already exists. Overwrite? [y/N] " confirm
    case "$confirm" in
        [yY][eE][sS]|[yY]) ;;
        *) echo "Aborted."; exit 1 ;;
    esac
fi

cat > "$OUTPUT_FILE" << EOF
from __future__ import annotations

class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None

    def __init__(self, val: int = 0):
        self.val = val

class Solution:
    """
    """

    def ${METHOD_SIGNATURE}:
        pass
EOF

echo "'$OUTPUT_FILE' created"