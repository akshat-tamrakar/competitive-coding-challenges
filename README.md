# Competitive Coding Challenges

A collection of solutions to competitive programming problems, primarily from LeetCode.

## Project Structure

```
competitive-coding-challenges/
├── leet_code/
│   ├── easy/          # Easy difficulty problems
│   │   └── two_sum.py
│   └── medium/        # Medium difficulty problems
├── main.py            # Entry point
└── pyproject.toml     # Project configuration
```

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

### Prerequisites

- Python >= 3.9
- `uv` package manager - [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

#### 1. Install uv

**Linux and macOS:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installing, you may need to restart your shell or run the command provided by the installer to add `uv` to your `PATH`. For Linux and macOS, this is typically:

```bash
source $HOME/.local/bin/env
```

#### 2. Project Installation

1.  Clone the repository and navigate into the project directory:

    ```bash
    git clone <repository-url>
    cd competitive-coding-challenges
    ```

2.  Create and activate virtual environment

    ```bash
    uv venv
    ```

3. Install the dependencies
    ```bash
    uv sync
    ```

## Usage

Run the main entry point:

```bash
python main.py
```

Run individual solutions:

```bash
python leet_code/easy/two_sum.py
```

## Solutions

### Easy

- **Two Sum** - Find two numbers that add up to a target value using hash map approach

## Development

This project uses `ruff` for linting and formatting.

Run linting:

```bash
uv run ruff check .
```

Format code:

```bash
uv run ruff format .
```

## Activate the virtual environment manually
#### On Linux/macOS:
```bash
    source .venv/bin/activate
```
#### On Windows:
```bash
    .venv\Scripts\activate
```

## Contributing

When adding new solutions:

1. Place them in the appropriate difficulty folder (`easy/`, `medium/`, etc.)
2. Use descriptive filenames matching the problem name
3. Include the problem description as a comment at the top
4. Add a `__main__` block with test cases

## License

[Add your license here]

