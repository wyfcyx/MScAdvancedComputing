## Realm Management Extension

four security states: secure/non-secure/realm/root state

software under secure and root state distrusts each other

> Furthermore, these states do not trusted each other!

EL3: root state, secure monitor

secure state: trusted application(EL0), trusted OS(EL1), SPM(EL2)

realm state: App/OS/Realm manager(EL0-2)