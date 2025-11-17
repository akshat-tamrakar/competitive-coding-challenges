# 🚀 Competitive Coding Challenges

A comprehensive collection of solutions to competitive programming problems from various platforms including LeetCode, Code360, and other algorithmic challenges.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Solutions](#solutions)
- [Development](#development)
- [Contributing](#contributing)

## 🎯 Overview

This repository contains well-documented solutions to competitive programming problems, organized by platform and difficulty level. Each solution includes:
- Clear problem descriptions
- Optimized implementations
- Time and space complexity analysis
- Test cases for verification

## 📁 Project Structure

```
competitive-coding-challenges/
├── leet_code/              # LeetCode problem solutions
│   ├── easy/               # Easy difficulty problems
│   │   ├── consecutive_characters.py
│   │   ├── palindrome_number.py
│   │   ├── remove_duplicates_sorted_array.py
│   │   ├── roman_to_integer.py
│   │   ├── two_sum.py
│   │   └── valid_parentheses.py
│   └── medium/             # Medium difficulty problems
│       ├── jump_game.py
│       ├── maximum_subarray.py
│       └── two_sum_ii.py
├── code360/                # Code360 problem solutions
│   └── easy/
│       └── pair_sum.py
├── other/                  # Additional algorithmic problems
│   ├── ag_pairs.py
│   ├── integer_to_roman.py
│   ├── algorithm/
│   │   └── searching/
│   │       └── binary_search.py
│   └── python_weird_behaviours/
│       └── try_finally.py
├── playground/             # Experimental code and testing
│   └── playground.py
├── main.py                 # Main entry point
├── pyproject.toml          # Project configuration
└── README.md               # This file
```

## 🛠️ Setup

This project uses [uv](https://github.com/astral-sh/uv) for fast and reliable dependency management.

### Prerequisites

- **Python** >= 3.9
- **uv** package manager

### Installation Steps

#### 1. Install uv

**Linux and macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installation, restart your shell or add `uv` to your PATH:
```bash
source $HOME/.local/bin/env
```

#### 2. Clone and Setup Project

```bash
# Clone the repository
git clone git@github.com:akshat-tamrakar/competitive-coding-challenges.git
cd competitive-coding-challenges

# Create virtual environment
uv venv

# Install dependencies
uv sync
```

#### 3. Activate Virtual Environment (Optional)

**Linux/macOS:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

## 💻 Usage

### Run Main Entry Point
```bash
python main.py
```

### Run Individual Solutions

**LeetCode Problems:**
```bash
# Easy problems
python leet_code/easy/two_sum.py
python leet_code/easy/palindrome_number.py
python leet_code/easy/valid_parentheses.py

# Medium problems
python leet_code/medium/maximum_subarray.py
python leet_code/medium/jump_game.py
```

**Code360 Problems:**
```bash
python code360/easy/pair_sum.py
```

**Algorithm Implementations:**
```bash
python other/algorithm/searching/binary_search.py
```

## 📚 Solutions

### LeetCode

#### Easy Problems
| Problem | File | Description |
|---------|------|-------------|
| Two Sum | `two_sum.py` | Find two numbers that add up to target using hash map |
| Palindrome Number | `palindrome_number.py` | Determine if an integer is a palindrome |
| Roman to Integer | `roman_to_integer.py` | Convert Roman numerals to integers |
| Remove Duplicates from Sorted Array | `remove_duplicates_sorted_array.py` | Remove duplicates in-place from sorted array |
| Valid Parentheses | `valid_parentheses.py` | Check if parentheses are valid using stack |
| Consecutive Characters | `consecutive_characters.py` | Find maximum consecutive character count |

#### Medium Problems
| Problem | File | Description |
|---------|------|-------------|
| Maximum Subarray | `maximum_subarray.py` | Find contiguous subarray with largest sum (Kadane's Algorithm) |
| Jump Game | `jump_game.py` | Determine if you can reach the last index |
| Two Sum II | `two_sum_ii.py` | Two Sum variant for sorted input array |

### Code360

#### Easy Problems
| Problem | File | Description |
|---------|------|-------------|
| Pair Sum | `pair_sum.py` | Find pairs with given sum |

### Other Algorithms

| Topic | File | Description |
|-------|------|-------------|
| Binary Search | `searching/binary_search.py` | Classic binary search implementation |
| Integer to Roman | `integer_to_roman.py` | Convert integers to Roman numerals |
| AG Pairs | `ag_pairs.py` | Custom pair-finding algorithm |

## 🔧 Development

This project uses **Ruff** for linting and code formatting.

### Code Quality Checks

**Run linter:**
```bash
uv run ruff check .
```

**Auto-fix linting issues:**
```bash
uv run ruff check . --fix
```

**Format code:**
```bash
uv run ruff format .
```

### Best Practices

- Write clean, readable code with meaningful variable names
- Include docstrings for functions and classes
- Add type hints where applicable
- Write comprehensive test cases
- Maintain consistent code style using Ruff

## 🤝 Contributing

Contributions are welcome! Follow these guidelines when adding new solutions:

### Adding New Solutions

1. **Choose the appropriate folder** based on platform and difficulty:
   - LeetCode: `leet_code/{easy|medium|hard}/`
   - Code360: `code360/{easy|medium|hard}/`
   - Other: `other/` or relevant subdirectory

2. **Use descriptive filenames** matching the problem name (snake_case):
   ```
   reverse_linked_list.py
   longest_substring.py
   ```

3. **Include problem details** as a docstring at the top:
   ```python
   """
   Problem: Problem Name
   Platform: LeetCode/Code360
   Difficulty: Easy/Medium/Hard
   Link: [problem URL]
   
   Description:
   [Brief problem description]
   
   Approach:
   [Your solution approach]
   
   Time Complexity: O(?)
   Space Complexity: O(?)
   """
   ```

4. **Add test cases** in a `__main__` block:
   ```python
   if __name__ == "__main__":
       # Test cases
       assert solution([1, 2, 3]) == expected_output
   ```

5. **Format your code** before committing:
   ```bash
   uv run ruff format .
   uv run ruff check . --fix
   ```

6. **Update README.md** with your new solution in the appropriate table

### Pull Request Guidelines

- Create a descriptive PR title
- Reference the problem number/name
- Ensure all tests pass
- Follow the existing code style

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Akshat Tamrakar**
- GitHub: [@akshat-tamrakar](https://github.com/akshat-tamrakar)

## 🌟 Acknowledgments

- [LeetCode](https://leetcode.com/) for problem inspiration
- [Code360](https://www.naukri.com/code360/) for additional challenges
- The competitive programming community

---

**Happy Coding! 🎉**
