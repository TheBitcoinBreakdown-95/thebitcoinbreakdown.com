# bitcointalk.org -- Scraped Content

**URL:** https://bitcointalk.org/index.php?topic=626.msg6490
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Golden rules.md
**Scraped:** 2026-04-12

---

Bitcoin Forum |   
---|---  
April 13, 2026, 01:14:57 AM  
---  
| Welcome, **Guest**. Please [login](https://bitcointalk.org/index.php?action=login) or [register](https://bitcointalk.org/index.php?action=register).   
---  
**News** : Latest Bitcoin Core release: [30.2](https://bitcoincore.org/en/download/) [[Torrent](https://bitcointalk.org/bitcoin-30.2.torrent)] |  [](https://bitcointalk.org/index.php?action=search;advanced)    
---|---  
  
 |   |  [Home](https://bitcointalk.org/index.php) |   |  [Help](https://bitcointalk.org/index.php?action=help) |  [Search](https://bitcointalk.org/index.php?action=search) |  [Login](https://bitcointalk.org/index.php?action=login) |  [Register](https://bitcointalk.org/index.php?action=register) |  [More](/more.php) |    
---|---|---|---|---|---|---|---|---|---  
  
**[Bitcoin Forum](https://bitcointalk.org/index.php)**  > **[Bitcoin](https://bitcointalk.org/index.php#1)**  > **[Bitcoin Discussion](https://bitcointalk.org/index.php?board=1.0)**  > **[*** ALERT *** Upgrade to 0.3.6](https://bitcointalk.org/index.php?topic=626.0)**

Pages: [**1**] [2](https://bitcointalk.org/index.php?topic=626.20) [3](https://bitcointalk.org/index.php?topic=626.40) [»](https://bitcointalk.org/index.php?topic=626.20)  [All](https://bitcointalk.org/index.php?topic=626.0;all) |  [« previous topic](https://bitcointalk.org/index.php?topic=626.0;prev_next=prev#new) [next topic »](https://bitcointalk.org/index.php?topic=626.0;prev_next=next#new) |   | [Print](https://bitcointalk.org/index.php?action=printpage;topic=626.0) |    
---|---|---  
|  Author |  Topic: *** ALERT *** Upgrade to 0.3.6  (Read 26112 times)   
---|---|---  
|  |  **[satoshi](https://bitcointalk.org/index.php?action=profile;u=3 "View the profile of satoshi")** (OP) Founder  
Sr. Member  
  
Offline  
  
Activity: 364  
Merit: 8738  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=3)  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6451#msg6451) |  [*** ALERT *** Upgrade to 0.3.6](https://bitcointalk.org/index.php?topic=626.msg6451#msg6451) July 29, 2010, 07:13:06 PM  
Last edit: October 04, 2010, 01:37:36 PM by satoshi |  [#1](https://bitcointalk.org/index.php?topic=626.msg6451#msg6451)  
---|---|---  
  
* * *

Please upgrade to 0.3.6 ASAP!  We fixed an implementation bug where it was possible that bogus transactions could be displayed as accepted.  Do not accept Bitcoin transactions as payment until you upgrade to version 0.3.6!  
  
If you can't upgrade to 0.3.6 right away, it's best to shut down your Bitcoin node until you do.  
  
Also in 0.3.6, faster hashing:  
\- midstate cache optimisation thanks to tcatm  
\- Crypto++ ASM SHA-256 thanks to BlackEye  
Total generating speedup 2.4x faster.  
  
Download:  
<http://sourceforge.net/projects/bitcoin/files/Bitcoin/bitcoin-0.3.6/>  
  
Windows and Linux users: if you got 0.3.5 you still need to upgrade to 0.3.6.  
  
  
|   
---  
|   
|  |  **[Olipro](https://bitcointalk.org/index.php?action=profile;u=526 "View the profile of Olipro")** Member  
  
Offline  
  
Activity: 70  
Merit: 10  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=526)  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6453#msg6453) |  [Re: *** ALERT *** Upgrade to 0.3.5 ASAP](https://bitcointalk.org/index.php?topic=626.msg6453#msg6453) July 29, 2010, 07:25:38 PM |  [#2](https://bitcointalk.org/index.php?topic=626.msg6453#msg6453)  
---|---|---  
  
* * *

is this in the SVN?  
  
|   
---  
|   
|  |  **[knightmb](https://bitcointalk.org/index.php?action=profile;u=345 "View the profile of knightmb")** Sr. Member  
  
Offline  
  
Activity: 308  
Merit: 260  
  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=345) [](http://timekoin.net/ "Timekoin")  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6455#msg6455) |  [Re: *** ALERT *** Upgrade to 0.3.5 ASAP](https://bitcointalk.org/index.php?topic=626.msg6455#msg6455) July 29, 2010, 07:26:39 PM |  [#3](https://bitcointalk.org/index.php?topic=626.msg6455#msg6455)  
---|---|---  
  
* * *

I appreciate the quickness of this security update, but unfortunately none of the Linux builds work (32bit or 64 bit) because the file is missing. I'm assuming if I go find the file it will work, not sure what luck others will have though using the new build.  
  
Error  


Code:

./bitcoin: error while loading shared libraries: libjpeg.so.62: cannot open shared object file: No such file or directory  
  
  
|   
---  
|   
  
* * *

Timekoin - The World's Most Energy Efficient Encrypted Digital Currency  
  
|  |  **[andy_3_913](https://bitcointalk.org/index.php?action=profile;u=385 "View the profile of andy_3_913")** Newbie  
  
Offline  
  
Activity: 42  
Merit: 0  
  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=385)  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6457#msg6457) |  [Re: *** ALERT *** Upgrade to 0.3.5 ASAP](https://bitcointalk.org/index.php?topic=626.msg6457#msg6457) July 29, 2010, 07:30:42 PM |  [#4](https://bitcointalk.org/index.php?topic=626.msg6457#msg6457)  
---|---|---  
  
* * *

are satoshi and Olipro working together?  
if not, any chance you could?   
  
i'm well pleased with the speed enhancements Olipro is making, but i would like bc to be secure!  
  
|   
---  
|   
|  |  **[jgarzik](https://bitcointalk.org/index.php?action=profile;u=541 "View the profile of jgarzik")** Legendary  
  
Offline  
  
Activity: 1596  
Merit: 1156  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=541)  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6458#msg6458) |  [Re: *** ALERT *** Upgrade to 0.3.5 ASAP](https://bitcointalk.org/index.php?topic=626.msg6458#msg6458) July 29, 2010, 07:30:57 PM |  [#5](https://bitcointalk.org/index.php?topic=626.msg6458#msg6458)  
---|---|---  
  
* * *

[Quote from: satoshi on July 29, 2010, 07:13:06 PM](https://bitcointalk.org/index.php?topic=626.msg6451#msg6451)

Please upgrade to 0.3.5 ASAP!  We fixed an implementation bug where it was possible that bogus transactions could be accepted.  Do not accept Bitcoin transactions as payment until you upgrade to version 0.3.5!  


  
Like Olipro, got a lot of people doing custom builds out there -- in fact, I **must** use a custom build on several machines.  
  
May we assume SVN has _all_ necessary updates?  
  
  
|   
---  
|   
  
* * *

Jeff Garzik, Bloq CEO, former bitcoin core dev team; opinions are my own.  
Visit bloq.com / metronome.io  
Donations / tip jar: 1BrufViLKnSWtuWGkryPsKsxonV2NQ7Tcj  
  
|  |  **[knightmb](https://bitcointalk.org/index.php?action=profile;u=345 "View the profile of knightmb")** Sr. Member  
  
Offline  
  
Activity: 308  
Merit: 260  
  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=345) [](http://timekoin.net/ "Timekoin")  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6459#msg6459) |  [Re: *** ALERT *** Upgrade to 0.3.5 ASAP](https://bitcointalk.org/index.php?topic=626.msg6459#msg6459) July 29, 2010, 07:34:22 PM |  [#6](https://bitcointalk.org/index.php?topic=626.msg6459#msg6459)  
---|---|---  
  
* * *

[Quote from: andy_3_913 on July 29, 2010, 07:30:42 PM](https://bitcointalk.org/index.php?topic=626.msg6457#msg6457)

are satoshi and Olipro working together?  
if not, any chance you could?   
  
i'm well pleased with the speed enhancements Olipro is making, but i would like bc to be secure!  


So far, the new build (stock) has given a 100% speed increase on my Celeron Machines that couldn't run those custom builds before. I'll compare the new release to the older *optimized* builds to see what the speed difference is just out of curiosity.   
  
|   
---  
|   
  
* * *

Timekoin - The World's Most Energy Efficient Encrypted Digital Currency  
  
|  |  **[Bitquux](https://bitcointalk.org/index.php?action=profile;u=511 "View the profile of Bitquux")** Member  
  
Offline  
  
Activity: 116  
Merit: 10  
  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=511)  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6461#msg6461) |  [Re: *** ALERT *** Upgrade to 0.3.5 ASAP](https://bitcointalk.org/index.php?topic=626.msg6461#msg6461) July 29, 2010, 07:39:46 PM |  [#7](https://bitcointalk.org/index.php?topic=626.msg6461#msg6461)  
---|---|---  
  
* * *

[Quote from: knightmb on July 29, 2010, 07:34:22 PM](https://bitcointalk.org/index.php?topic=626.msg6459#msg6459)

[Quote from: andy_3_913 on July 29, 2010, 07:30:42 PM](https://bitcointalk.org/index.php?topic=626.msg6457#msg6457)

are satoshi and Olipro working together?  
if not, any chance you could?   
  
i'm well pleased with the speed enhancements Olipro is making, but i would like bc to be secure!  


So far, the new build (stock) has given a 100% speed increase on my Celeron Machines that couldn't run those custom builds before. I'll compare the new release to the older *optimized* builds to see what the speed difference is just out of curiosity.    


  
So far I'm seeing a comparable hashing rate to the most recent of the Olipro 32-bit binaries. It might even be slightly faster.  
  
|   
---  
|   
|  |  **[jgarzik](https://bitcointalk.org/index.php?action=profile;u=541 "View the profile of jgarzik")** Legendary  
  
Offline  
  
Activity: 1596  
Merit: 1156  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=541)  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6462#msg6462) |  [Re: *** ALERT *** Upgrade to 0.3.5 ASAP](https://bitcointalk.org/index.php?topic=626.msg6462#msg6462) July 29, 2010, 07:42:15 PM |  [#8](https://bitcointalk.org/index.php?topic=626.msg6462#msg6462)  
---|---|---  
  
* * *

  
With the official Linux-64bit build, run on Fedora 13, I see it failing badly:  
  


Code:

************************  
EXCEPTION: 22DbRunRecoveryException         
DbEnv::open: DB_RUNRECOVERY: Fatal error, run database recovery         
bitcoin in AppInit()         
  
  
  
************************  
EXCEPTION: 22DbRunRecoveryException         
DbEnv::open: DB_RUNRECOVERY: Fatal error, run database recovery         
bitcoin in CMyApp::OnUnhandledException()         
  
terminate called after throwing an instance of 'DbRunRecoveryException'  
  what():  DbEnv::open: DB_RUNRECOVERY: Fatal error, run database recovery  


  
Praying my bitcoins aren't eaten...  
  
  
|   
---  
|   
  
* * *

Jeff Garzik, Bloq CEO, former bitcoin core dev team; opinions are my own.  
Visit bloq.com / metronome.io  
Donations / tip jar: 1BrufViLKnSWtuWGkryPsKsxonV2NQ7Tcj  
  
|  |  **[knightmb](https://bitcointalk.org/index.php?action=profile;u=345 "View the profile of knightmb")** Sr. Member  
  
Offline  
  
Activity: 308  
Merit: 260  
  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=345) [](http://timekoin.net/ "Timekoin")  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6464#msg6464) |  [Re: *** ALERT *** Upgrade to 0.3.5 ASAP](https://bitcointalk.org/index.php?topic=626.msg6464#msg6464) July 29, 2010, 07:47:37 PM |  [#9](https://bitcointalk.org/index.php?topic=626.msg6464#msg6464)  
---|---|---  
  
* * *

[Quote from: jgarzik on July 29, 2010, 07:42:15 PM](https://bitcointalk.org/index.php?topic=626.msg6462#msg6462)

  
With the official Linux-64bit build, run on Fedora 13, I see it failing badly:  
  


Code:

************************  
EXCEPTION: 22DbRunRecoveryException         
DbEnv::open: DB_RUNRECOVERY: Fatal error, run database recovery         
bitcoin in AppInit()         
  
  
  
************************  
EXCEPTION: 22DbRunRecoveryException         
DbEnv::open: DB_RUNRECOVERY: Fatal error, run database recovery         
bitcoin in CMyApp::OnUnhandledException()         
  
terminate called after throwing an instance of 'DbRunRecoveryException'  
  what():  DbEnv::open: DB_RUNRECOVERY: Fatal error, run database recovery  


  
Praying my bitcoins aren't eaten...  
  


I think you'll be ok, it blew up on me too. Run the older version, you should still see all your coins. Backup first for the next Linux release   
  
|   
---  
|   
  
* * *

Timekoin - The World's Most Energy Efficient Encrypted Digital Currency  
  
|  |  **[jgarzik](https://bitcointalk.org/index.php?action=profile;u=541 "View the profile of jgarzik")** Legendary  
  
Offline  
  
Activity: 1596  
Merit: 1156  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=541)  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6465#msg6465) |  [Re: *** ALERT *** Upgrade to 0.3.5 ASAP](https://bitcointalk.org/index.php?topic=626.msg6465#msg6465) July 29, 2010, 07:49:32 PM |  [#10](https://bitcointalk.org/index.php?topic=626.msg6465#msg6465)  
---|---|---  
  
* * *

[Quote from: jgarzik on July 29, 2010, 07:42:15 PM](https://bitcointalk.org/index.php?topic=626.msg6462#msg6462)

With the official Linux-64bit build, run on Fedora 13, I see it failing badly:  


  
Same result on another machine.  BDB errors, and death.  0.3.5 on 64bit Linux is questionable.  You didn't mix up the builds with 32-bit Linux, did you?  
  
debug.log says:  


Code:

Bitcoin version 0.3.5 beta  
Default data directory /g/g/.bitcoin  
Bound to port 8333  
Loading addresses...  
dbenv.open strLogDir=/garz/bitcoin/data/database strErrorFile=/garz/bitcoin/data/db.log  
  
  
************************  
EXCEPTION: 22DbRunRecoveryException         
DbEnv::open: DB_RUNRECOVERY: Fatal error, run database recovery         
bitcoin in AppInit()         
  
  
|   
---  
|   
  
* * *

Jeff Garzik, Bloq CEO, former bitcoin core dev team; opinions are my own.  
Visit bloq.com / metronome.io  
Donations / tip jar: 1BrufViLKnSWtuWGkryPsKsxonV2NQ7Tcj  
  
|  |  **[jgarzik](https://bitcointalk.org/index.php?action=profile;u=541 "View the profile of jgarzik")** Legendary  
  
Offline  
  
Activity: 1596  
Merit: 1156  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=541)  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6467#msg6467) |  [Re: *** ALERT *** Upgrade to 0.3.5 ASAP](https://bitcointalk.org/index.php?topic=626.msg6467#msg6467) July 29, 2010, 07:52:45 PM |  [#11](https://bitcointalk.org/index.php?topic=626.msg6467#msg6467)  
---|---|---  
  
* * *

[Quote from: knightmb on July 29, 2010, 07:47:37 PM](https://bitcointalk.org/index.php?topic=626.msg6464#msg6464)

I think you'll be ok, it blew up on me too. Run the older version, you should still see all your coins. Backup first for the next Linux release    


  
Double-ACK   
  
older version (SVN 117 + listtransactions + getinfo KHPS) works fine, all bitcoins there.  And yes, I should back up before following "please upgrade" instructions...    
  
|   
---  
|   
  
* * *

Jeff Garzik, Bloq CEO, former bitcoin core dev team; opinions are my own.  
Visit bloq.com / metronome.io  
Donations / tip jar: 1BrufViLKnSWtuWGkryPsKsxonV2NQ7Tcj  
  
|  |  **[knightmb](https://bitcointalk.org/index.php?action=profile;u=345 "View the profile of knightmb")** Sr. Member  
  
Offline  
  
Activity: 308  
Merit: 260  
  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=345) [](http://timekoin.net/ "Timekoin")  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6468#msg6468) |  [Re: *** ALERT *** version 0.3.6](https://bitcointalk.org/index.php?topic=626.msg6468#msg6468) July 29, 2010, 07:54:27 PM |  [#12](https://bitcointalk.org/index.php?topic=626.msg6468#msg6468)  
---|---|---  
  
* * *

[Quote from: davidonpda on July 29, 2010, 07:51:38 PM](https://bitcointalk.org/index.php?topic=626.msg6466#msg6466)

Can windows users upgrade to the 3.5 for now?  


Yes, I've tested on Windows XP, 2003, and 7 all went through just fine. You'll enjoy the speed increase as well.    
  
[**err, wait I guess, new version about to spawn**]  
  
|   
---  
|   
  
* * *

Timekoin - The World's Most Energy Efficient Encrypted Digital Currency  
  
|  |  **[satoshi](https://bitcointalk.org/index.php?action=profile;u=3 "View the profile of satoshi")** (OP) Founder  
Sr. Member  
  
Offline  
  
Activity: 364  
Merit: 8738  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=3)  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6469#msg6469) |  [Re: *** ALERT *** version 0.3.6](https://bitcointalk.org/index.php?topic=626.msg6469#msg6469) July 29, 2010, 07:55:51 PM |  [#13](https://bitcointalk.org/index.php?topic=626.msg6469#msg6469)  
---|---|---  
  
* * *

Haven't had time to update the SVN yet.  Wait for 0.3.6, I'm building it now.  You can shut down your node in the meantime.    
  
|   
---  
|   
|  |  **[satoshi](https://bitcointalk.org/index.php?action=profile;u=3 "View the profile of satoshi")** (OP) Founder  
Sr. Member  
  
Offline  
  
Activity: 364  
Merit: 8738  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=3)  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6480#msg6480) |  [Re: *** ALERT *** version 0.3.6](https://bitcointalk.org/index.php?topic=626.msg6480#msg6480) July 29, 2010, 08:30:15 PM |  [#14](https://bitcointalk.org/index.php?topic=626.msg6480#msg6480)  
---|---|---  
  
* * *

SVN is updated with version 0.3.6.  
  
Uploading Windows build of 0.3.6 to Sourceforge now, then will rebuild linux.  
  
|   
---  
|   
|  |  **[RudeDude](https://bitcointalk.org/index.php?action=profile;u=481 "View the profile of RudeDude")** Newbie  
  
Offline  
  
Activity: 11  
Merit: 0  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=481)  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6485#msg6485) |  [Re: *** ALERT *** version 0.3.6](https://bitcointalk.org/index.php?topic=626.msg6485#msg6485) July 29, 2010, 08:35:54 PM |  [#15](https://bitcointalk.org/index.php?topic=626.msg6485#msg6485)  
---|---|---  
  
* * *

Ha! One of the changes in there is updated some v "0.3.3" stuff to "0.3.6" but that isn't the important part of the update. :-)  
  
|   
---  
|   
|  |  **[jgarzik](https://bitcointalk.org/index.php?action=profile;u=541 "View the profile of jgarzik")** Legendary  
  
Offline  
  
Activity: 1596  
Merit: 1156  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=541)  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6486#msg6486) |  [Re: *** ALERT *** version 0.3.6](https://bitcointalk.org/index.php?topic=626.msg6486#msg6486) July 29, 2010, 08:48:35 PM |  [#16](https://bitcointalk.org/index.php?topic=626.msg6486#msg6486)  
---|---|---  
  
* * *

  
SVN r119 seems to work fine here.  No BDB explosion.  
  
  
  
|   
---  
|   
  
* * *

Jeff Garzik, Bloq CEO, former bitcoin core dev team; opinions are my own.  
Visit bloq.com / metronome.io  
Donations / tip jar: 1BrufViLKnSWtuWGkryPsKsxonV2NQ7Tcj  
  
|  |  **[knightmb](https://bitcointalk.org/index.php?action=profile;u=345 "View the profile of knightmb")** Sr. Member  
  
Offline  
  
Activity: 308  
Merit: 260  
  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=345) [](http://timekoin.net/ "Timekoin")  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6487#msg6487) |  [Re: *** ALERT *** version 0.3.6](https://bitcointalk.org/index.php?topic=626.msg6487#msg6487) July 29, 2010, 08:51:29 PM |  [#17](https://bitcointalk.org/index.php?topic=626.msg6487#msg6487)  
---|---|---  
  
* * *

Tested the Windows build across XP, 2003, Vista, 7 (both 32 and 64bit builds), no issues installing or running client. So far so good, looking forward to the Linux client.   
  
|   
---  
|   
  
* * *

Timekoin - The World's Most Energy Efficient Encrypted Digital Currency  
  
|  |  **[satoshi](https://bitcointalk.org/index.php?action=profile;u=3 "View the profile of satoshi")** (OP) Founder  
Sr. Member  
  
Offline  
  
Activity: 364  
Merit: 8738  
  
  
[](https://bitcointalk.org/index.php?action=profile;u=3)  
|  | [](https://bitcointalk.org/index.php?topic=626.msg6490#msg6490) |  ⇾ [Re: *** ALERT *** Upgrade to 0.3.6 ASAP!](https://bitcointalk.org/index.php?topic=626.msg6490#msg6490) July 29, 2010, 09:20:38 PM  
Last edit: July 29, 2010, 09:36:48 PM by satoshi |  [#18](https:/

[... truncated at 20,000 characters ...]
