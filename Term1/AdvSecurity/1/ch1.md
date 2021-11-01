what role does security play 'n the design of a large system and seven important concepts

## 1.1 security is holistic

security is holistic, so all the three types of security including technological security(application, OS, and network security, we mostly discuss this type in this book), physical security and good policies and procedures are required together to guarantee that a system is safe

physical security: e.g protect the data center(or even the rubbish) physically

technological security(at a software level)

* application security

  example: web server which provides valuable document for specific users

  potential vulnerabilities: invalid authentication/inappropriate web server configurations(such as allowing the access to remote file system)/bugs from web browsers allow hackers to take control of users' computer when users are visiting a malicious website

* OS security

  OS developers publish patches periodically to eliminate these vulnerabilities

* network security

  no malicious traffic: cause unexpected behavior to users

  solutions: firewall or IDS(intrusion detection systems)

a set of policies and procedures for everybody which is involved in the project/company. For example, never give your password to others including the administrator. social engineering attack.

## 1.2 Authentication

Authentication means verifying others' identity. It's important for Bob to confirm that the people she is communicating with are actually Alice! Authentication can base on 3 types of methods:

**something you know**

for instance, a password.

advantages: simple to implement than biometrics, and can be easily understood by users.

disadvantages: easy to hack since users tend to use simple passwords; user have to reuse their passwords for many time, so that hacker may "listen to" these passwords. This problem can be solved by using an OTP system, but usually it is necessary to use a special device, which is more likely a 'something you have' method

**something you have**

just as we mentioned before, an OTP card, or something which is integrated into the PDA(personal digital assistants) system. It generates a new password periodically and show the password to its users.

Another device is a smart card. It is tamper-resistant. Only the microprocessor inside the card can access the memory which contains sensitive data. In other words, all the components are designed to be integrated. When inserting it into a card reader, a PIN is required to start the transaction. Disadvantages: an untrusted card reader can record the PIN users input, or sensitive data inside the card can be unveiled by analyzing the power consumption of the card.

ATM cards: the magnetic stripe on the card is easy to copy by attackers, signatures are not checked most of the time

**something you are**

biometric techniques: should consider its effectiveness and social acceptability

examples: palm & fingerprint scan(more effective than only fingerprint scan); iris scan which is more acceptable than palm scan since it's less intrusive; retinal scan is the most intrusive; fingerprinting; voice identification; facial recognition; signature dynamics(including pressure and timing); 

cons: false positive(system reject an authentic user's request) and false negatives(when impersonators successfully impersonate a user); various social acceptability(all less acceptable than a password); people cannot change their biometric data after they are stolen by attackers. By contrast, passwords can be easily changed.

**notes**

we can use combination of different authentication methods.

two-factor authentication: both inserting the ATM card into the ATM and providing your PIN are required. GPS location can also take into account, but this can bring some inconvenience.

Computers authenticate other computers in a large distributed system. There're 3 types of authentications: client/server/mutual authentication. It depends on the cost of setting up a client/server/or both.

## 1.3 Authorization

authorization: whether a user is permitted to do something. example: bank will check whether you have enough money in your account

OS example: ACL. 3 different access control models:

* mandatory access control(MAC): user cannot share file with others even if he wants. Everything is controlled by the OS.
* discretionary access control(DAC): user can share file with others by using some commands(like Unix)
* role-based access control(RBAC): like MAC, but every user is assigned with a role which determines that what he is allowed to do(user groups in Unix)

another model which can be used to implement MAC and DAC: Bell-Lapadula Model, every resource has a certain level of access e.g. unclassified/confidential/secret/top secret, all users are also classified. 3 properties which illustrate the relationship between the level of access of the resources and the users:

* simple property: user can only access <= user's level(aka 'no read up')
* star property: user cannot write a lower level resource which can be viewed by a lower level user(aka 'no write down')
* tranquility property: level of resource cannot be changed while there're users accessing them(synchronization)

## 1.4 Confidentiality

confidentiality: keep the content or data of communication stored or temporary or permanent storage safe, which means that even if it is theft by attackers(Eve, this can be done by exploiting the vulnerabilities in the OS), them cannot interpret them.

This can be achieved by encryption methods. Data are encrypted are can only by decrypted through a key, which is only known and kept by Alice and Bob.

## 1.5 Message/Data Integrity

Mallory(aka 'a man in the middle') can modify a part of the message or data which is sent to Alice by Bob. Alice may want to find out that whether the message has been modified by others. Bob also want to add some redundant part in the message to prevent this from happening.

DoS attack: modify every message even if the receiver is able to know that the message has been modified

in networking communication protocols, CRCs(cyclic redundancy check) can be used to achieve integrity. It's enough the deal with the inadvertent failures, but it's not enough when facing with advertent failures. Instead we can use message authentication codes(MACs).

Overall, integrity is different from confidentiality. It aims at preventing attackers from 'touching' the data even if they can 'see' them.

## 1.6 Accountability

keep a system log recording every operations of every user. The safety of the system log should be guaranteed so that it cannot be deleted or changed at ease. In this case, when something is going wrong, we can easily find out who should take the responsibility.

It's also important to keep the timestamp synchronized among different computer systems.

## 1.7 Availability

reasonable response time, but more than a performance metric

sample attack: DoS for a single server, DDoS for a distributed server which installs malicious software on many computers and launch DoS attacks at the same time

a trade-off between secure and availability

solutions: add redundancy to eliminate point of failure;

another attack: fill up the disk(not useful in nowadays cloud executing environment)

## 1.8 Non-repudiation

ensure the transactions won't be refused under the help of trusted third parties(or dropped by the other side since it's not trusted). In general, two parties cannot deny what they interacted with each other since trusted parties can intervene.

Cons: good in theory but very expensive for practice







