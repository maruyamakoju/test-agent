# Test

A general-purpose testing utility framework for running, organizing, and reporting on test suites. Test provides a simple interface for defining test cases, executing them in parallel or sequentially, and generating clear, actionable reports.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Example](#basic-example)
  - [Running Tests](#running-tests)
  - [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
  - [Getting Started](#getting-started)
  - [Development Workflow](#development-workflow)
  - [Pull Request Process](#pull-request-process)
  - [Code Style](#code-style)
- [License](#license)

## Features

- Simple and intuitive API for defining test cases
- Support for parallel and sequential test execution
- Built-in assertion helpers
- Configurable reporters (console, JSON, HTML)
- Easy integration with CI/CD pipelines

## Prerequisites

- Git
- A compatible runtime environment (see installation steps below)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/test.git
   cd test
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Verify the installation:

   ```bash
   npm test
   ```

## Usage

### Basic Example

```javascript
const { describe, it, expect } = require('test');

describe('Math operations', () => {
  it('should add two numbers', () => {
    expect(1 + 2).toBe(3);
  });

  it('should multiply two numbers', () => {
    expect(3 * 4).toBe(12);
  });
});
```

### Running Tests

Run all tests:

```bash
npm test
```

Run a specific test file:

```bash
npm test -- path/to/test-file.js
```

Run tests in watch mode:

```bash
npm run test:watch
```

### Configuration

Create a `test.config.json` file in the project root to customize behavior:

```json
{
  "parallel": true,
  "reporter": "console",
  "timeout": 5000,
  "retries": 0
}
```

| Option     | Type    | Default     | Description                              |
|------------|---------|-------------|------------------------------------------|
| `parallel` | boolean | `false`     | Run test suites in parallel              |
| `reporter` | string  | `"console"` | Output format: `console`, `json`, `html` |
| `timeout`  | number  | `5000`      | Timeout per test case in milliseconds    |
| `retries`  | number  | `0`         | Number of times to retry failing tests   |

## Project Structure

```
test/
├── calculator/     # Simple browser-based calculator
│   ├── index.html
│   ├── style.css
│   └── script.js
├── src/            # Source code
├── tests/          # Test files
├── docs/           # Documentation
├── README.md       # This file
└── package.json    # Project metadata and dependencies
```

## Contributing

Contributions are welcome! Whether it is a bug report, feature request, or a pull request, your input helps improve this project.

### Getting Started

1. Fork the repository on GitHub.

2. Clone your fork locally:

   ```bash
   git clone https://github.com/your-username/test.git
   cd test
   ```

3. Create a branch for your changes:

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. Install dependencies:

   ```bash
   npm install
   ```

### Development Workflow

1. Make your changes in the appropriate files.
2. Add or update tests to cover your changes.
3. Run the test suite to ensure everything passes:

   ```bash
   npm test
   ```

4. Commit your changes with a clear, descriptive message:

   ```bash
   git commit -m "Add support for custom reporters"
   ```

### Pull Request Process

1. Push your branch to your fork:

   ```bash
   git push origin feature/your-feature-name
   ```

2. Open a pull request against the `main` branch of this repository.
3. Fill out the pull request template with a description of your changes.
4. Wait for a maintainer to review your pull request. Address any requested changes.
5. Once approved, your pull request will be merged.

### Code Style

- Write clear, readable code with meaningful variable and function names.
- Keep functions small and focused on a single responsibility.
- Include tests for any new functionality or bug fixes.
- Follow the existing patterns and conventions in the codebase.

## Calculator

A simple, modern calculator built with HTML, CSS, and JavaScript. No build tools or dependencies required.

### Features

- Four basic operations: add (+), subtract (-), multiply (×), divide (÷)
- Percent (%), sign toggle (±), decimal point
- Clear (C) and backspace
- Keyboard input support
- Responsive design for mobile and desktop

### How to Use

1. Open `calculator/index.html` in any browser.
2. Click buttons or use the keyboard:

| Key | Action |
|-----|--------|
| `0`-`9` | Enter digits |
| `.` | Decimal point |
| `+` `-` `*` `/` | Operators |
| `Enter` or `=` | Calculate result |
| `Backspace` | Delete last digit |
| `Escape` | Clear all |
| `%` | Percent |

## License

This project is licensed under the [MIT License](LICENSE).
