# Agentic Log Parser

An AI-powered test log parser that uses Google's Gemini AI to analyze test logs and extract structured test results. This tool intelligently parses complex test outputs to identify individual test names, their pass/fail status, and overall test suite results.

## Features

- **AI-Powered Parsing**: Uses Google's Gemini 2.0 Flash model for intelligent log analysis
- **Structured Output**: Returns parsed results in a well-defined JSON schema using Pydantic models
- **Test Result Extraction**: Identifies actual test names (not just test files or suites)
- **Overall Status Detection**: Determines if all tests passed, all failed, or mixed results
- **Error Handling**: Handles cases where tests fail to run due to errors

## How to run

1. Make sure you have uv installed
2. Set up your environment variables
3. Install dependencies
4. Run the parser

## Installation

### Prerequisites

- Python 3.13 or higher
- uv package manager
- Google Gemini API key

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd agentic_log_parser
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Create a `.env` file in the project root:
```bash
cp .env.example .env
```

4. Add your Google Gemini API key to the `.env` file:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

## Configuration

### Environment Variables

- `GEMINI_API_KEY`: Your Google Gemini API key (required)

### Getting a Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file

## Usage

### Basic Usage

Run the parser with the sample log:

```bash
uv run main.py
```

### Expected Output

The parser will output:
- Success count: Number of passed tests
- Failed count: Number of failed tests  
- All success: Boolean indicating if all tests passed
- All failed: Boolean indicating if all tests failed

### Output Schema

The parser returns results in the following structure:

```python
class LogParsedResults(BaseModel):
    test_results: Dict[str, TestResult]  # Individual test results
    all_success: bool                    # True if all tests passed
    all_failed: bool                     # True if all tests failed

class TestResult(str, Enum):
    PASSED = "PASSED"
    FAILED = "FAILED"
```

### Customizing Input

To analyze your own logs, modify the `sample_logs.py` file or update the log variable in `main.py`:

```python
# Replace the sample log with your actual test log
log_content = """
Your test log content here...
"""
```

## Project Structure

```
agentic_log_parser/
├── main.py           # Main parser logic
├── sample_logs.py    # Sample test logs for analysis
├── pyproject.toml    # Project configuration and dependencies
├── uv.lock          # Dependency lock file
├── .env             # Environment variables (create this)
└── README.md        # This file
```

## Dependencies

- **google-generativeai**: Google's Gemini AI Python SDK
- **instructor**: Structured outputs from language models
- **pydantic**: Data validation and settings management
- **python-dotenv**: Load environment variables from .env files

## Development

### Running Tests

```bash
uv run pytest
```

### Adding New Sample Logs

Add new log samples to `sample_logs.py`:

```python
your_new_log = """
Your test log content here...
"""
```

## How It Works

1. **Log Input**: Takes test log content as input
2. **AI Analysis**: Sends the log to Google's Gemini AI with specific parsing instructions
3. **Structured Extraction**: Uses the instructor library to ensure structured JSON output
4. **Result Processing**: Processes the AI response to count successes and failures
5. **Output**: Returns parsed results with individual test outcomes and overall status

## Limitations

- Requires internet connection for Gemini AI API calls
- API usage costs apply based on Google's pricing
- Parsing quality depends on log format and AI model performance
- Currently configured for JavaScript/Node.js test logs (easily adaptable)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

[Add your license information here]