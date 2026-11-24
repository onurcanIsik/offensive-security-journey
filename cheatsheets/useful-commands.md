# Useful Commands

Commands I use most while learning.

## Commands and their explanations

```bash
find [location] -type f -size +100c         # finds files byte size
wc -l [filename]                            # Number of lines in a file
grep "keyword" [filename]                   # find keyword in a file
cat [filename] | tr 'a-zA-Z' 'n-za-mN-ZA-M' # ROT13 on a file
mv [file] [file.txt]                        # Change file name and copy
tar -xf [file.tar]                          # extract the tar file
gzip2 -d [filename]                         # extract the gz file
bzip2 -d [filename]                         # extract the bz2 file
ssh [websitelink] -p [port] -i [key]        # Log in to a server with a specific port and key
unique -u [filename].                       # finds a unique word
sort [filename]                             # sort the all lines in a one file and uniqe words
```

```bash
curl [URL]     #download the html of the website and show us in the terminal
curl -I [URL] # The command just give us http header with status codes
nmap -sV [IP_ADDRESS]  # Show us which port are open and what service is running on them
gobuster dir -u [URL] # The command give hidden line and endpoints like /admin /login etc this like journal on website
gobuster dir -u [URL] -w [wordlist - /usr/share/wordlists/dirb/common.txt] # this is almost same before command but we just gie a wordlist for this command for try this words.
```
