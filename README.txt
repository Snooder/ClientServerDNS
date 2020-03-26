Matt Snyder mcs307
Marco Garcia	mag518

The way to make recursive DNS functionality requires the
client to first contact the root server with a query of
the hostnames but when it does not find the Hostname within
its own DNS table, it then goes to ask the top level servers
for its own query of the hostname.

No errors within the code

The majority of creating a socketing connection between the
client and servers were not very difficult until the challenge
of communicating with servers that were not all running on the
localhost. In the end it was just as simple as changing the
server_address to connect with the gethostname() instead of
'localhost' to allow other hosts to connect.

This project has taught us the abilities of socket programming
with a hidden lesson about how recursive versus iteration DNS
look up really works which had confused me for the longest time.
The strengths of network coding are incredibly powerful and
especially now with this template of network code with separate hosts.
