# logstream

Real-time log aggregation and parsing with pattern matching.

## Features

- Parse multiple log formats
- Real-time streaming
- Pattern-based filtering
- Structured output (JSON)
- Configurable patterns

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Parse single file
python -m logstream parse app.log

# Stream logs
tail -f app.log | python -m logstream stream

# Filter by level
python -m logstream parse app.log --level ERROR
```

## Supported Formats

- Apache/Nginx access logs
- Application logs (JSON, plain text)
- Syslog
- Custom patterns via YAML config

## Troubleshooting

- **Empty output**: Check that the log file exists and contains data matching the selected pattern
- **Permission errors**: Ensure the log file is readable by the current user

## Requirements

- Python 3.8+

## License

MIT
