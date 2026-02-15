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

## Performance Notes

- Streaming mode is recommended for log files larger than 500MB to minimize memory footprint
- Parse mode loads entire file into memory; monitor system resources for very large files
- Processing speed depends on pattern complexity and log format

## Notes

- For large log files (>100MB), consider using the streaming mode to avoid memory issues
- Ensure log files have appropriate read permissions before parsing
- Python 3.9+ recommended for optimal performance

## Limitations

- Binary log files are not supported; logs must be text-based
- Pattern matching is line-based and does not handle multi-line log entries
- Maximum file size for parse mode is limited by available system memory

## Troubleshooting

- **Empty output**: Check that the log file exists and contains data matching the selected pattern
- **Permission errors**: Ensure the log file is readable by the current user

## Requirements

- Python 3.8+

## License

MIT
