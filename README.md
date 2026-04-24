# Java-to-Python Test Migration: LLM Evaluation Artifact

Replication package for "From Java to Python: Assessing LLM Effectiveness in Automated Test Migration."

This repository contains function mappings and LLM-generated Python unit tests evaluated in the study, enabling reproducibility and supporting future research on cross-language test migration.

## Overview

This artifact includes:

- Function mappings across 13 algorithm modules (254 mapped functions)
- Generated test cases (1,249 Python unit tests) created by GPT-4o from Java source tests

## Repository Structure

```
.
├── README.md
├── mapping/
│   ├── audio_filters.json
│   ├── backtracking.json
│   ├── bit_manipulation.json
│   ├── ciphers.json
│   ├── conversions.json
│   ├── data_structures.json
│   ├── dynamic_programming.json
│   ├── maths.json
│   ├── matrix.json
│   ├── scheduling.json
│   ├── searches.json
│   ├── sorts.json
│   └── strings.json
└── generated_tests/
    ├── audio_filters/
    ├── backtracking/
    ├── bit_manipulation/
    ├── ciphers/
    ├── conversions/
    ├── data_structures/
    ├── dynamic_programming/
    ├── maths/
    ├── matrix/
    ├── scheduling/
    ├── searches/
    ├── sorts/
    └── strings/
```

## Contents

### `mapping/`

JSON files containing function mappings between Java and Python implementations. Each file follows this format:

```json
{
  "source": "java:[package]:[class]:[method]",
  "target": "python:[module]:[class]:[method]"
}
```

**Example:**
```json
{
  "source": "java:com.thealgorithms.searches:BinarySearch:binarySearch",
  "target": "python:searches.binary_search:binary_search"
}
```

Use these mappings to identify which Java tests were migrated to Python equivalents.

### `generated_tests/`

LLM-generated Python unit tests, organized by module. Each module folder contains:

- `test_*.py` files — test modules corresponding to Python source files
- Tests are pytest-compatible and can be executed with: `pytest test_*.py`

**Test naming convention:** Test files follow the pattern `test_[python_filename].py`, where `python_filename` matches the name of the Python source file being tested. For example, tests for `sorts/bubble_sort.py` are in `test_bubble_sort.py`.

## Citation

If you use this artifact in your research, please cite:

```bibtex
@mastersthesis{doan2026java,
  title={From Java to Python: Assessing LLM Effectiveness in Automated Test Migration},
  author={Doan, Hai Dang},
  year={2026},
  school={Linnaeus University},
  note={Available at: https://github.com/DangOnGitHub/test-migration-llm}
}
```

## License

This artifact is made available under the [MIT License](https://opensource.org/licenses/MIT). See the LICENSE file for details.

## Related Resources

- **Thesis:** Available at [thesis repository or institutional repository]
- **Original Repositories:**
  - [The Algorithms (Java)](https://github.com/TheAlgorithms/Java)
  - [The Algorithms (Python)](https://github.com/TheAlgorithms/Python)

## Questions or Issues

For questions about the artifact, please open an issue on this repository.
