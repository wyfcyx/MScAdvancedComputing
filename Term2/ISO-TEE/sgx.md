## a glance

secure remote computation?(cloud service, multi-tenant), protect data's confidentiality and integrity, relies on *software attestation*(predecessors: TPM{trusted platform module} and TXT)

what is software attestation: prove to the users that the **specific software** is running in a **secure container** hosted by the **trusted hardware**; container contents are verified through its hash value; user can load any software into the container after the container content is verified by the user

> like digital signature:
>
> 1. Alice generate a pair of (public key, private key)
> 2. Alice wants to send to Bob `m`="Hello world!"
> 3. Alice encrypts the message using the private key into `sign`
> 4. Alice sends `m` and encrypted message `sign` at the same time to Bob
> 5. Bob decrypts `sign` using the public key, if the result equals to `m`, then Bob can **believe that the message `m` is from Alice**

> background knowledge: Diffie-Hellman Key exchange algorithm
>
> 1. Alice and Bob agree on a prime number(17) and a generator(3) of this prime number which satisfies that $g^0,g^1,...,g^{p-1}$ are all different $\mod p$.
> 2. Alice selects a private number 15, calculate $3^{15}\mod 17=6$, and publicly sends it to Bob.
> 3. Bob selects a private number 13, calculates $3^{13}\mod{17}=12$, and publicly send it to Alice.
> 4. Alice and Bob calculate their shared public key: $12^{15}\mod{17}=6^{13}\mod{17}=10$
> 5. Now Alice and Bob can use their shared key for symmetric encryption and they do not need to send the key through the non-secure channel.

details of verification: hardware's manufacturer provides **an endorsement certificate**, the **attestation key** is used to generate a signature against the certificate, 