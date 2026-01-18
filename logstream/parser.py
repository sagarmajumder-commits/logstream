"""Log parsing utilities."""
import re
import json
from datetime import datetime
from typing import Dict, Optional, List


class LogParser:
    """Parse log entries into structured format."""
    
    # Common log patterns
    PATTERNS = {
        'apache': r'(?P<ip>[\d.]+) - - \[(?P<timestamp>[^\]]+)\] "(?P<method>\w+) (?P<path>[^\s]+) HTTP/[\d.]+" (?P<status>\d+) (?P<size>\d+)',
        'json': r'^\{.*\}$',
        'level': r'(?P<timestamp>[\d\-:,\s]+)\s+(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL)\s+(?P<message>.*)',
    }
    
    def __init__(self, pattern_name: str = 'level'):
        self.pattern_name = pattern_name
        self.pattern = re.compile(self.PATTERNS.get(pattern_name, self.PATTERNS['level']))
    
    def parse_line(self, line: str) -> Optional[Dict]:
        """
        Parse a single log line.
        
        Args:
            line: Raw log line
            
        Returns:
            Parsed log entry as dict, or None if no match
        """
        line = line.strip()
        if not line:
            return None
        
        # Try JSON first
        if line.startswith('{'):
            try:
                return json.loads(line)
            except json.JSONDecodeError:
                pass
        
        # Try pattern matching
        match = self.pattern.match(line)
        if match:
            return match.groupdict()
        
        # Fallback: return raw line
        return {'raw': line, 'timestamp': datetime.now().isoformat()}
    
    def parse_file(self, filepath: str, level_filter: Optional[str] = None) -> List[Dict]:
        """
        Parse entire log file.
        
        Args:
            filepath: Path to log file
            level_filter: Optional log level filter (ERROR, WARNING, etc.)
            
        Returns:
            List of parsed log entries
        """
        entries = []
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                entry = self.parse_line(line)
                if entry:
                    if level_filter and entry.get('level') != level_filter:
                        continue
                    entries.append(entry)
        
        return entries
