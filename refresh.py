import requests
import time
import random
import re

url = "https://github.com/dulakdi"
total_refreshes = 100

print(f"Fetching GitHub profile to find the badge URL...")
try:
    response = requests.get(url)
    # The view counter is usually proxied by GitHub's camo server. 
    # We need to hit that Camo URL to mimic a real profile view.
    # The URL itself is hex-encoded, so we match it alongside the data-canonical-src attribute.
    camo_url_match = re.search(r'src="(https://camo\.githubusercontent\.com/[^"]+)"[^>]*?data-canonical-src="https://komarev\.com/ghpvc', response.text)
    
    if camo_url_match:
        badge_url = camo_url_match.group(1).replace("&amp;", "&")
        print(f"Found Camo Badge URL! Starting {total_refreshes} requests...")
    else:
        print("Could not find the camo URL for the badge. Using fallback.")
        badge_url = "https://komarev.com/ghpvc/?username=dulakdi&label=Profile%20Views&color=blueviolet&style=for-the-badge"

    for i in range(1, total_refreshes + 1):
        try:
            # We must send standard browser Accept headers and Cache-Control
            # Without this, GitHub/Komarev caches the image and ignores the request.
            headers = {
                "User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(110, 122)}.0.0.0 Safari/537.36",
                "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "Cache-Control": "max-age=0, no-cache",
                "Pragma": "no-cache",
                "Referer": "https://github.com/"
            }
            
            response = requests.get(badge_url, headers=headers)
            print(f"Refresh {i}/{total_refreshes} - Status: {response.status_code}")
            
            # Avoid getting rate limited by GitHub Camo
            time.sleep(random.uniform(0.5, 1.5))
            
        except requests.exceptions.RequestException as e:
            print(f"Error on refresh {i}: {e}")

except Exception as main_e:
    print(f"Failed to fetch profile: {main_e}")