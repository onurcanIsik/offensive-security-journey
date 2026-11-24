# Linux / Terminal Basics

Commands I use most while learning pentesting.

## Navigation
pwd                   # print current directory
ls -la                # list all files (incl. hidden) with details
cd <dir>              # change directory
cd ..                 # go up one level
cd ~                  # go to home

## Files
cat <file>            # print file content
less <file>           # view file page by page (q to quit)
head / tail <file>    # first / last lines
touch <file>          # create empty file
mkdir <dir>           # create directory
cp / mv <src> <dst>   # copy / move (or rename)
rm <file>             # delete file
rm -r <dir>           # delete directory

## Search
grep "text" <file>    # find text in a file
grep -r "text" <dir>  # search recursively
find / -name "flag*"  # find files by name
find . -type f        # list all files under current dir

## Permissions
chmod +x <file>       # make a file executable
chmod 600 <file>      # owner read/write only
chown user <file>     # change owner
sudo <cmd>            # run as root

## Network / Recon
nmap <ip>             # scan open ports
nmap -sV <ip>         # scan + service versions
curl <url>            # request a URL
curl -u user:pass <url>   # with basic auth
wget <url>            # download a file
ssh user@<ip>         # remote login over SSH
nc <ip> <port>        # netcat: connect to a port

## Processes / System
ps aux                # list running processes
whoami                # current user
id                    # current user + groups
kill <pid>            # stop a process

## Helpful
man <cmd>             # manual for a command
<cmd> -h              # quick help
history               # commands I ran before
clear                 # clear the screen
