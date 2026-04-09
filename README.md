# OpenPage

A simple Python script designed to interact with GitHub profile view counters (specifically the `komarev.com/ghpvc` badge). It simulates browser requests to automatically update or "refresh" the view count on a GitHub profile.

## Features
- Fetches the GitHub Camo proxied URL for the badge to simulate real views.
- Randomizes User-Agent strings to mimic different browsers.
- Sends appropriate `Cache-Control` headers to bypass caching.
- Includes randomized delays between requests to prevent rate limiting.

## Prerequisites
- Python 3.x
- `requests` library

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/godragun/openpage.git
   cd openpage
   ```
2. Install the required dependencies:
   ```bash
   pip install requests
   ```

## Usage
Run the script using Python:
```bash
python refresh.py
```

## Disclaimer
This script is created for educational purposes to demonstrate how HTTP headers, caching, and proxies (like GitHub Camo) work. Abusing this to artificially inflate metrics may violate GitHub's Terms of Service. Use responsibly.
