# Advent of Code 2024

This repository contains my solutions for the [Advent of Code 2024](https://adventofcode.com/2024) challenges. The project is implemented in Python using the [Click](https://click.palletsprojects.com/) library to create a command-line interface (CLI).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/aoc2024.git
    ```
2. Navigate to the project directory:
    ```bash
    cd aoc2024
    ```
3. Install the required dependencies:
    ```bash
    uv sync
    ```

## Usage

Run the CLI application using:
```bash
python aoc2024.py [OPTIONS] COMMAND [ARGS]...
```

To see available commands and options:
```bash
python aoc2024.py --help
```

## Project Structure

Each day's challenge is implemented as a separate command within the CLI. You can run a specific day's solution like this:
```bash
python aoc2024.py dayN
```
Replace `N` with the day number (e.g., `day1`, `day2`, etc.).

## Contributing

Contributions are welcome. Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.