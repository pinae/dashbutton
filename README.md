# Amazon Dash button
The script `listen.py` registers ARP-packets in the local network. 
If you enter the MAC of your Amazon Dash button it registers if the
button is pressed. It can act on this event with a request to a ITTT 
webhook (ITTT maker channel) or by writing a mail using a 
Gmail-account.

## Installation
Activate your dash button with the Amazon smartphone app. You do not 
need to select a product to order. The script will register if the 
button is pressed even if no product was selected.

The script uses scapy to sniff the ARP-packets the button sends when 
connecting to your wifi. Because of that it only works with Python 2.7.
If you want to trigger the webhook you also need requests, the mail
part uses smtplib.

The script probably needs root-privileges:
```shell
sudo python2 listen.py
```

Run the script without any modification. It will list all unrecognized 
MAC addresses in ARP packets. Your router will answer all the packets
so its mac address pops up many times. Press your button and note the 
MAC that pops up next. If you are unsure which one it is: it is not
harmful to press the button more than once. After noting the MAC of your
button and router insert those in `listen.py`. The addresses listed there
are mine - just replace them.

Change the code so it fits your needs. For ITTT you need to change the 
URL for the webhook so it matches your key. If you want to mail directly
change the Gmail settings in `send_mail.py`.

Run `listen.py` again. It now prints `Button Pressed!` every time you 
press your button.
