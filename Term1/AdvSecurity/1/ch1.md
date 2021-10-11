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

