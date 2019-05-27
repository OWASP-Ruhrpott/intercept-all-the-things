# Intercepting all the things!

This repository is about intercepting non http / binary traffic send over tcp.
Often I was confronted during my pentests with a custom protocol, a closed-source device or network service
with a proprietary protocol.

This little workshop should provide you with the knowledge and skills to intercept [(1)](binary-network-protocol/challenges/01/01-How-to-intercept-traffic.md) and modify [(2)](binary-network-protocol/challenges/02/02-How-to-modify-traffic.md) the mentioned traffic.

In the last chapter [(3)](binary-network-protocol/challenges/03/03-How-to-create-a-little-wireshark-plugin.md) we will also learn how to create a little `wireshark` dissector.

## Requirements

The following tools are required for this workshop:
- Linux operating system
- `python3`
- `wireshark`
- `lua`
- `socat`
- `netsed`

Optional:
- A linux VM or another device to test the with other interfaces.
