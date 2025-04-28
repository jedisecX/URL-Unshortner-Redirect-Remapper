# URL-Unshortner-Redirect-Remapper

Maps the full redirect chain of short URLs, developed by Jedi Security.

## Features
- Follows and logs each redirect hop
- Handles multiple URLs from a file
- Simple CLI usage
- Max 10 redirects per URL (safe default)

## Usage
```bash
python3 url_unshortner_redirect_remapper.py urls.txt

Example

Input file (urls.txt):


http://bit.ly/3abcd
https://tinyurl.com/xyz

Output:


[+] Redirect chain for http://bit.ly/3abcd:
    301 -> http://example.com
    200 -> http://final.com/page

[+] Redirect chain for https://tinyurl.com/xyz:
    301 -> https://anotherdomain.com
    200 -> https://anotherdomain.com/final
