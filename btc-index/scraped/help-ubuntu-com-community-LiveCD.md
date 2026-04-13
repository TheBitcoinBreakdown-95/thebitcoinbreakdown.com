# help.ubuntu.com -- Scraped Content

**URL:** https://help.ubuntu.com/community/LiveCD
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Dice.md
**Scraped:** 2026-04-12

---

* [Partners](https://canonical.com/partners)
  * [Support](https://ubuntu.com/community/support)
  * [Community](https://ubuntu.com/community)
  * [Ubuntu.com](https://ubuntu.com)


# [Ubuntu Documentation](https://help.ubuntu.com/)

  * [Official Documentation](https://help.ubuntu.com/)
  * [Community Help Wiki](https://help.ubuntu.com/community/CommunityHelpWiki)
  * [Contribute](https://ubuntu.com/community/contribute)


  * [Page History](/community/LiveCD?action=info)
  * [Login to edit](/community/LiveCD?action=login&login=1)


#  [LiveCD](/community/LiveCD)

* * *

|  **Needs Expansion**   
This article is incomplete, and needs to be expanded. [More info...](/community/Tag#NeedsExpansion)  
---|---  
  
Contents

  1. Introduction
     1. Reasons for Using a LiveCD Session
     2. Other Ways to Try Ubuntu
  2. How-To LiveCD Ubuntu
     1. Preparing your LiveCD
     2. Using your LiveCD
     3. Installing Programs or Other Packages
     4. Making a Customised LiveCD
  3. Troubles with a LiveCD
     1. Logging in
     2. Security and Updating
     3. Setting a Password
     4. Text-Mode Installation
  4. See also

  
---  
  
# Introduction

A live CD can be used for a quick demo or test of Ubuntu. Try Ubuntu without any changes to your machine! Windows or whatever you use normally is unaffected after trying this and then rebooting. 

The standard Ubuntu Cd can be used as a LiveCd as well as an installer. Live mode is the default option when booting from CD. Only some of the non-standard downloads (such as the "Alternate Cd") lack this functionality. [Windows users](/community/SwitchingToUbuntu/FromWindows) might be familiar with the term 'boot CD' or 'bootable CD' or 'Recovery/Restore Media'. A "LiveCD" is more than that because it gives the option of running a normal desktop environment with all the normal programs and some extras. A LiveCD usually finds your wired internet connection and Firefox should be able to surf the internet into here. 

This guide has screen-shots of the 8.04 and 10.04 Desktop Edition of Ubuntu. However, Lubuntu, Xubuntu, Kubuntu and even unofficial Ubuntu-based distros as well as other versions all tend to have similar screens & menus. 

Most [distributions](http://distrowatch.com) (versions or "distros" of Linux) have this LiveCd functionality on their installer CD, a few have a separate Cd to download. It is rare to find a distro that has no LiveCd session at all. Ubuntu tries to make their LiveCD the easiest to use. Although a LiveCD session is a good way to demo Ubuntu _without making changes to a machine_ , a LiveCD will always be slower than a proper installation to the hard-drive. Cd-drives & Dvd-drives are physically slower than hard drives. 

You can use a [persistent image](/community/LiveCD/Persistence) to keep data & settings safe after shut-down. This does go against many reasons for using a LiveCd session (rather than an installation) but it can be useful for multi-user machines, such as offices or in third world education projects. 

## Reasons for Using a LiveCD Session

LiveCD sessions are good to: 

  * give a 'demo' session on a machine before installing or upgrading 
    * checks hardware works as expected 
    * check the look & feel of the distro 
  * repair or preparation for awkward installations 
    * repair/replace/install grub perhaps after (re)installing [Windows](/community/DualBoot/Grub#recovering-grub)
    * fix Windows problems on a machine that doesn't have a [dual-boot](/community/DualBoot/Windows)
    * [anti-virus](/community/Antivirus) problems on a Windows system 
    * [data recovery](/community/DataRecovery)
    * [resizing partitions](/community/HowtoPartition) to give Ubuntu more (or less) room 
    * [adding a new partition](/community/HowtoPartition)(s) to your hard-drive for [other distros](http://distrowatch.com) or for a new Windows 
  * preparing a machine for installing Ubuntu, if you are shy of using default or automatic settings or if the hardware is too unique or awkward 
  * 'showing off' Ubuntu to people on their own machine 
  * using on a random computer where access is limited 
  * a familiar desktop environment on an unfamiliar machine 
  * safely using a computer which seems to have poor security or lacks privacy. This is particularly good if you have a Usb stick or something to save your data and settings on (see '[persistent image](/community/LiveCD/Persistence)') 


## Other Ways to Try Ubuntu

LiveCDs are designed for people that want to use Ubuntu on a computer for a few hours. If you want to carry a LiveCD around with you, a [persistent image](/community/LiveCD/Persistence) lets you customise your live session. If you want to use Ubuntu on a computer for a few weeks or months, [Wubi](/community/Wubi) lets you install Ubuntu inside Windows. If you want to use Linux on a computer permanently, [dual-booting](/community/DualBoot/Windows) lets you install Window and Ubuntu (or which-ever distro) side-by-side on the same computer. 

Because Wubi needs Windows and Ubuntu to co-operate, you have to deal with all the problems of both systems. For example, it's not easy to completely uninstall Wubi. An experienced linux user or someone with considerable technical knowledge about Windows might find it better to try Wubi in some certain circumstances where dual-booting is infeasible or inadvisable. See [the Wubi guide](https://wiki.ubuntu.com/WubiGuide "Ubuntu") for more information about Wubi, particularly how to uninstall it cleanly. 

[Dual-booting](/community/DualBoot/Windows) can be daunting at first, but tends to work better once you've got it set up. This allows Window & Ubuntu to work without relying on the other for anything, except the boot-loader. As you get more comfortable with Ubuntu, you can just forget about your Windows partition. Reinstalling Windows is quite tricky, so it's best to leave your Windows partition in place unless you're absolutely sure you'll never use Windows again. 

# How-To LiveCD Ubuntu

## Preparing your LiveCD

You need to create, borrow, buy or request an Ubuntu CD or [Usb-stick](/community/Installation/FromUSBStick#live-usb). Once you have an Ubuntu Cd or Usb it should work as an installer and as a !LiveCD or LiveUsb. There are some downloads, such as the Alternate Cd that cannot be used as !LiveCd/Usb. 

### To create a LiveCd

  * [Download](http://www.ubuntu.com/getubuntu/download) Ubuntu. For a live CD, avoid the "alternate CD" & the Server Edition because it has no desktop. For installing, using the alternate CD is a good idea, if installing using the standard CD does not work. 
  * [Make your own CD](/community/BurningIsoHowto). Cheap "write once" CDs in packs of 10 or more are usually best. You could burn a new CD once every 6 months to get the latest version but all version are supported for 18 months and long time support releases for 3 years. You could also use the remaining CDs for trying out other [distros](http://distrowatch.com) Having a quick demo of other distros can help you understand Linux in general a LOT better a LOT faster, which helps you understand Ubuntu better. 


### To create a LiveUsb

  * The Usb stick needs to be 1Gb or more and there are 2 different pages giving advice. I prefer the first; [Installation/FromUSBStick](/community/Installation/FromUSBStick), [Installation/FromImgFiles](/community/Installation/FromImgFiles)


### To buy an Ubuntu Cd

The official [Cannonical store](http://www.ubuntulinux.org/getubuntu/purchase), OnDisc, OSDisc or your local Ubuntu team might be able to help you find somewhere in your country from which to buy Ubuntu CDs. Also see [GettingUbuntu](/community/GettingUbuntu) for more information. 

## Using your LiveCD

Put the Ubuntu CD into the CD/DVD-drive and reboot the computer. You should see a menu with "Try Ubuntu without any change to your computer" at the top. If you don't get this menu, read the [booting From the CD](/community/BootFromCD) guide for more information. 

  
**Figure 1:** The first thing you will see when you boot from your Ubuntu CD  
Press the up or down arrow on keyboard to get your language and then press enter  
---  
  
  
**Figure 2:** F6 will give you Boot Options & allows you to edit the boot-string  
---  
  
Choose "Try Ubuntu without any change to your computer". You should get a desktop which we call a "LiveCD session". If you don't see a desktop, or need safe graphics mode, read the [boot options](/community/BootOptions) for more information. 

  
**Figure 3:** The LiveCD lets you manage partitions with GPartEd.  
Also see the installer icon top-left  
---  
  
The Firefox icon on the top panel should let you surf the internet. Other normal programs are available in the menus. 

After you have finished, shut the computer down and remove the CD. At this point anything you saved to the desktop or Documents folders and such will vanish - only things you saved into folders on the hard-drive will remain. This means that there won't be any trace of your personal data (e-mails, passwords etc.) left on the machine, which can be quite useful if you don't trust the Windows installation on the computer. 

If you have troubles getting the working desktop but if it is still not behaving then try asking for help in [Launchpad](https://answers.launchpad.net/ubuntu/+addquestion) or use [Signpost Help](/community/Signpost), or both. 

## Installing Programs or Other Packages

You can install programs to a LiveCD session in the [normal way](/community/InstallingSoftware), although these will be forgotten as soon as you switch the machine off. For example, you might install [antivirus](/community/Antivirus) or [data-recovery](/community/DataRecovery) tools to fix the system installed on the computer's hard drive. Because space is limited on a LiveCD, you should limit the number of packages you install or consider using a [persistent image](/community/LiveCD/Persistence). 

## Making a Customised LiveCD

If you want to make custom Ubuntu-based Live CD, you should read the [LiveCD Customisation HowTo](/community/LiveCDCustomization). Without even starting from an existing Ubuntu CD you can make a customised live system, see [LiveCD Customisation From Scratch](/community/LiveCDCustomizationFromScratch). 

# Troubles with a LiveCD

## Logging in

Sometimes a LiveCD might ask you for a user-name or password. Just leave these blank and press enter (or allow it to time-out). 

  
**Figure 4:_Just press enter to get past this, or let it time-out  
---  
  
  
**Figure 5:_ 10.04 login screen  
---  
  
## Security and Updating

While linux systems are more secure than Windows, LiveCD sessions are not meant for long-term use nor for sessions lasting several days. Because LiveCDs can't easily be updated, they may well be vulnerable to security issues discovered in the months since their release. They also can't protect you against scams such as [phishing](http://en.wikipedia.org/wiki/Phishing "WikiPedia"). If a criminal broke in to your live session, any changes he made to your session would be reset along with everything else when you reboot, although he could make permanent changes to the computer's hard drive. 

A [persistent image](/community/LiveCD/Persistence) can be updated as new security issues emerge, but also lets any damage done to your computer persist across sessions. 

## Setting a Password

You can set a password during a LiveCD session by opening a [terminal](/community/UsingTheTerminal), and typing in: 
    
    
    $ sudo passwd ubuntu

## Text-Mode Installation

If your normal installation fails without giving an error message, or if you want to install on a very limited system, you can use the text-based installer instead. 

# See also

  * [CdDvd](/community/CdDvd)
  * [Common problems booting from the CD](/community/BootFromCD)
  * [LiveCdRecovery](https://help.ubuntu.com/community/LiveCdRecovery)


* * *

[CategoryLive](/community/CategoryLive)

LiveCD (last edited 2012-06-02 22:06:40 by 66)

The material on this wiki is available under a free license, see [Copyright / License](https://help.ubuntu.com/community/
		License) for details  
**You** can contribute to this wiki, see [Wiki Guide](https://help.ubuntu.com/community/WikiGuide) for details
