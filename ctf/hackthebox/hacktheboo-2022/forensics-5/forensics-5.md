# forensics 5

a bunch of windows logs...great

https://github.com/williballenthin/python-evtx

```txt
https://www.ultimatewindowssecurity.com/securitylog/book/page.aspx?spid=chapter5

security log
```

```sh
# LARGE file incoming
python3 ~/Downloads/python-evtx/scripts/evtx_dump.py ~/Downloads/Logs/Security.evtx |& tee security_dump.xml
```

```txt
https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4624

4624 = successful login
```

```txt
https://jumpcloud.com/blog/active-directory-authentication

kerberos ?
```

```sh
cat security_dump.xml | grep -a "AuthenticationPackageName" | sort > auth_package.xml

# NTLM ?
```

```sh
python3 scan_ntlm.py > ntlm.xml

# first record
# <ns0:Data Name="TargetUserName">ANONYMOUS LOGON</ns0:Data>
# <ns0:TimeCreated SystemTime="2020-03-21 20:24:15.832811" />

# hmm nothing
```

```txt
<Computer>srv01.boocorp.htb</Computer>
2022-09-28 12:04:21.258808 ?? nope


noticed that viewing log on Windows Event Viewer, event record ID goes to 18786 (filter on 4624 event ID)
in security_dump.xml record ID goes to 18492...I guess the package screwed up? nice

login event record ID 18636
```

```xml
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-a5ba-3e3b0328c30d}" />
    <EventID>4624</EventID>
    <Version>1</Version>
    <Level>0</Level>
    <Task>12544</Task>
    <Opcode>0</Opcode>
    <Keywords>0x8020000000000000</Keywords>
    <TimeCreated SystemTime="2022-09-28T13:10:57.3143161Z" />
    <EventRecordID>18636</EventRecordID>
    <Correlation />
    <Execution ProcessID="488" ThreadID="2112" />
    <Channel>Security</Channel>
    <Computer>srv01.boocorp.htb</Computer>
    <Security />
  </System>
  <EventData>
    <Data Name="SubjectUserSid">S-1-0-0</Data>
    <Data Name="SubjectUserName">-</Data>
    <Data Name="SubjectDomainName">-</Data>
    <Data Name="SubjectLogonId">0x0</Data>
    <Data Name="TargetUserSid">S-1-5-21-3330634377-1326264276-632209373-500</Data>
    <Data Name="TargetUserName">Administrator</Data>
    <Data Name="TargetDomainName">BOOCORP</Data>
    <Data Name="TargetLogonId">0x42dbad</Data>
    <Data Name="LogonType">3</Data>
    <Data Name="LogonProcessName">NtLmSsp </Data>
    <Data Name="AuthenticationPackageName">NTLM</Data>
    <Data Name="WorkstationName">kali</Data>
    <Data Name="LogonGuid">{00000000-0000-0000-0000-000000000000}</Data>
    <Data Name="TransmittedServices">-</Data>
    <Data Name="LmPackageName">NTLM V2</Data>
    <Data Name="KeyLength">128</Data>
    <Data Name="ProcessId">0x0</Data>
    <Data Name="ProcessName">-</Data>
    <Data Name="IpAddress">-</Data>
    <Data Name="IpPort">-</Data>
    <Data Name="ImpersonationLevel">%%1833</Data>
  </EventData>
</Event>
```



