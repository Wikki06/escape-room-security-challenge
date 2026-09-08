#!/usr/bin/env bash
set -euo pipefail
target="/app/challenge/challenge.py"
printf '%s\n' "[*] Looking for hidden clue..."
ans=$(python3 "$target" --read-file "../../tmp/escape_room/clue.txt")
printf '%s\n' "[+] Server response: $ans"
key=$(echo "$ans" | cut -d'=' -f2)
if [[ -z "$key" ]]; then
    printf '%s\n' "[-] Error: Failed to extract the clue."
    exit 1
fi
printf '%s\n' "[+] Clue received: $key"
printf '%s\n' "[*] Using the clue to continue"
flag=$(python3 "$target" --exec-clue "hello; cat /app/flag.txt")
if echo "$flag" | grep -q '^FLAG{'; then
    printf '%s\n' "[+] Challenge solved successfully!!!"
    printf '%s\n' "[+] Flag: $flag"
    touch /app/challenge/.solved
    exit 0
else
    printf '%s\n' "[-] Unable to recieve the flag : $flag"
    exit 1
fi