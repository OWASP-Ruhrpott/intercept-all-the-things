# Advanced modify traffic

Now the vendor improved his server and client to be more up to date!
The new release includes now an encrypted channel and a nonce to match the username with the requested id.

## Protocol Structure

Get user id by username:
```
42|username
```
Response from the server:
```
id|nonce
```

Login:
```
01|length|02|length_payload|03|user_id|nonce|password|04|MD5(01|length|02|length_payload|03|user_id|nonce|password)|ffff
```

### How to intercept

We will use `socat` again and the new `fixed-proxy.py`.

Create a certificate for socat ssl:
```
openssl req -newkey rsa:2048 -new -nodes -keyout key.pem -out csr.pem
openssl x509 -req -days 365 -in csr.pem -signkey key.pem -out server.crt
cat key.pem server.crt > cert.pem
```

Use the following commands in 3 different terminals:
```
socat -v openssl-listen:9998,cert=cert.pem,verify=0,reuseaddr,fork tcp4:localhost:6666
```
```
python3 fixed-proxy.py 6666 127.0.0.1 6665
```
```
socat -v tcp4-listen:6665,reuseaddr,fork ssl:0.0.0.0:9999,verify=0
```
The `socat` commands will terminate the encrypted channel on each side of the encryption.

## Challenge 03

Start the improved versions of bob and alice and the server.

```
./ssl_server
./ssl_bob_and_alice -i 0.0.0.0 -p 9998
```

Create based on the `fixed-proxy.py` an attack to update the userid to admin and update the checksum at the end.

1. What is the flag of the admin user? Use the template for the `fixed-proxy.py` to login as admin.
