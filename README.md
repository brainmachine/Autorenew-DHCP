# Autorenew-DHCP
Python script that automatically renew your DHCP lease in case you lose your network connection.
I wrote this because I had a bad internet connection in my workspace and had to renew my DHCP lease every 10 minutes or so.
To use it run  ```python autoRenewDHCP.py ``` and then type your admin password (required so the script can run the 'networksetup' command-line tool).
