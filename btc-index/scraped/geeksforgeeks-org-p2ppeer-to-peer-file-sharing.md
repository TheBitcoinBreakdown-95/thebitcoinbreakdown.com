# geeksforgeeks.org -- Scraped Content

**URL:** https://geeksforgeeks.org/p2ppeer-to-peer-file-sharing
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\What is a P2P Network.md
**Scraped:** 2026-04-12

---

[](https://www.geeksforgeeks.org/)

 __

  * Courses

 __
  * Tutorials

 __
  * Interview Prep

 __


__

  * [CN Tutorial](https://www.geeksforgeeks.org/computer-networks/computer-network-tutorials/)
  * [Interview Questions](https://www.geeksforgeeks.org/computer-networks/commonly-asked-computer-networks-interview-questions-set-1/)
  * [Quizzes](https://www.geeksforgeeks.org/quizzes/50-computer-networks-mcqs-with-answers/)
  * [Gate](https://www.geeksforgeeks.org/computer-networks/computer-networks-for-gate/)
  * [OSI Model](https://www.geeksforgeeks.org/computer-networks/open-systems-interconnection-model-osi/)
  * [TCP-IP](https://www.geeksforgeeks.org/computer-networks/tcp-ip-model/)
  * [Network Security](https://www.geeksforgeeks.org/computer-networks/network-security/)
  * [COA](https://www.geeksforgeeks.org/computer-organization-architecture/computer-organization-and-architecture-tutorials)
  * [TOC](https://ww\)w.geeksforgeeks.org/theory-of-computation/introduction-of-theory-of-computation/)
  * [Compiler Design](https://www.geeksforgeeks.org/compiler-design/compiler-design-tutorials/)
  * [DBMS](https://www.geeksforgeeks.org/dbms/dbms/)


# P2P (Peer To Peer) File Sharing

Last Updated : 23 Jul, 2023

  *   *   * 


In Computer Networking, P2P (Peer-to-Peer) is a file-sharing technology, that allows users to access mainly the multimedia files like videos, music, e-books, games, etc. The individual users in this network are referred to as peers. The peers request files from other peers by establishing TCP or UDP connections. 

## How Does P2P (Peer-to-Peer) Work?

A peer-to-peer network allows computer hardware and software to communicate without the need for a server. Unlike client-server architecture, there is no central server for processing requests in a [P2P architecture](https://www.geeksforgeeks.org/computer-networks/what-is-p2p-peer-to-peer-process/). The peers directly interact with one another without the requirement of a central server.   
  
Now, when one peer makes a request, multiple peers may have a copy of that requested object. Now the problem is how to get the IP addresses of all those peers. This is decided by the underlying architecture supported by the P2P systems. Using one of these methods, the client peer can get to know all the peers which have the requested object/file and the file transfer takes place directly between these two peers.

## P2P Architecture

  1. Centralized Directory
  2. Query Flooding
  3. Exploiting Heterogeneity


### **1\. Centralized Directory**

A centralized Directory is somewhat similar to [client-server architecture](https://www.geeksforgeeks.org/system-design/client-server-model/) in the sense that it maintains a huge central server to provide directory service. All the peers inform this central server of their IP address and the files they are making available for sharing. The server queries the peers at regular intervals to make sure if the peers are still connected or not. So basically this server maintains a huge database regarding which file is present at which IP addresses. The first system which made use of this method was **Napster** , for Mp3 distribution.

**Working**

  * Now whenever a requesting peer comes in, it sends its query to the server.
  * Since the server has all the information of its peers, so it returns the IP addresses of all the peers having the requested file to the peer.
  * Now the file transfer takes place between these two peers.

Centralized Directory

The major problem with such an architecture is that there is a single point of failure. If the server crashes, the whole P2P network crashes. Also, since all of the processing is to be done by a single server so a huge amount of the database has to be maintained and regularly updated.

### 2\. Query Flooding

Unlike the centralized approach, this method makes use of distributed systems. In this, the peers are supposed to be connected to an overlay network. It means if a connection/path exists from one peer to another, it is a part of this overlay network. In this overlay network, peers are called nodes, and the connection between peers is called an edge between the nodes, thus resulting in a graph-like structure. **Gnutella** was the first decentralized peer-to-peer network. 

#### **Working**

  * Now when one peer requests for some file, this request is sent to all its neighboring nodes i.e. to all nodes connected to this node. If those nodes don't have the required file, they pass on the query to their neighbors and so on. This is called query flooding.
  * When the peer with the requested file is found (referred to as query hit), the query flooding stops and it sends back the file name and file size to the client, thus following the reverse path.
  * If there are multiple query hits, the client selects from one of these peers.


**Gnutella:** Gnutella represents a new wave of P2P applications providing distributed discovery and sharing of resources across the Internet. Gnutella is distinguished by its support for anonymity and its decentralized architecture. A Gnutella network consists of a dynamically changing set of peers connected using TCP/IP.

Query Flooding

This method also has some disadvantages, the query has to be sent to all the neighboring peers unless a match is found. This increases traffic in the network. 

### 3\. Exploiting Heterogeneity

This P2P architecture makes use of both the above-discussed systems. It resembles a distributed system like Gnutella because there is no central server for query processing. But unlike Gnutella, it does not treat all its peers equally. The peers with higher bandwidth and network connectivity are at a higher priority and are called **group leaders/supernodes**. The rest of the peers are assigned to these supernodes. These supernodes are interconnected and the peers under these supernodes inform their respective leaders about their connectivity, IP address, and the files available for sharing.

**KaZaA** technology is such an example that makes use of Napster and Gnutella. Thus, the individual group leaders along with their child peers form a Napster-like structure. These group leaders then interconnect among themselves to resemble a Gnutella-like structure.

#### Working

  * This structure can process the queries in two ways.
  * The first one is that the supernodes could contact other supernodes and merge their databases with their database. Thus, this supernode now has information about a large number of peers.
  * Another approach is that when a query comes in, it is forwarded to the neighboring super nodes until a match is found, just like in Gnutella. Thus query flooding exists but with limited scope as each supernode has many child peers. Hence, such a system exploits the heterogeneity of the peers by designating some of them as group leaders/supernodes and others as their child peers

Exploiting heterogeneity

## P2P File Sharing Security Concerns

Steps that ensure that Sensitive Information on the network is secure:

  * You must delete your sensitive information which you don't require and you can apply some restrictions to important file present within the network.
  * For strong or accessing sensitive information, try to reduce or remove P2P file-sharing programs on computers.
  * Constantly try to monitor the network to find unauthorized file-sharing programs.
  * Try to block the unauthorized Peer-to-Peer file sharing programs within the perimeter of the network.
  * Implement strong access controls and authentication mechanisms to prevent unauthorized access to sensitive information on the network.
  * Use encryption techniques such as Secure Socket Layer (SSL) or Transport Layer Security (TLS) to protect data in transit between peers on the network.
  * Implement firewalls, intrusion detection and prevention systems, and other security measures to prevent unauthorized access to the network and to detect and block malicious activity.
  * Regularly update software and security patches to address known vulnerabilities in P2P file-sharing programs and other software used on the network.
  * Educate users about the risks associated with P2P file-sharing and provide training on how to use these programs safely and responsibly.
  * Use data loss prevention tools to monitor and prevent the transmission of sensitive data outside of the network.
  * Implement network segmentation to limit the scope of a security breach in case of a compromise, and to prevent unauthorized access to sensitive areas of the network.
  * Regularly review and audit the network to identify potential security threats and to ensure that security controls are effective and up-to-date.


Comment

Article Tags:

Article Tags:

[Misc](https://www.geeksforgeeks.org/category/misc/)

[Computer Networks](https://www.geeksforgeeks.org/category/computer-subject/computer-networks/)

### Explore

Computer Network Basics __

    * [Computer Networking __3 min read](https://www.geeksforgeeks.org/computer-networks/basics-computer-networking/)
    * [Types __4 min read](https://www.geeksforgeeks.org/computer-networks/types-of-computer-networks/)
    * [Internet __5 min read](https://www.geeksforgeeks.org/computer-science-fundamentals/introduction-to-internet/)
    * [Network Devices __3 min read](https://www.geeksforgeeks.org/computer-networks/network-devices-hub-repeater-bridge-switch-router-gateways/)
    * [OSI Model __8 min read](https://www.geeksforgeeks.org/computer-networks/open-systems-interconnection-model-osi/)
    * [TCP/IP Model __6 min read](https://www.geeksforgeeks.org/computer-networks/tcp-ip-model/)
    * [OSI vs TCP/IP Model __4 min read](https://www.geeksforgeeks.org/computer-networks/difference-between-osi-model-and-tcp-ip-model/)

Physical Layer __

    * [Physical Layer __2 min read](https://www.geeksforgeeks.org/computer-networks/physical-layer-in-osi-model/)
    * [Network Topology __9 min read](https://www.geeksforgeeks.org/computer-networks/types-of-network-topology/)
    * [Transmission Modes __2 min read](https://www.geeksforgeeks.org/computer-networks/transmission-modes-computer-networks/)
    * [Transmission Media __9 min read](https://www.geeksforgeeks.org/computer-networks/types-transmission-media/)

Data Link Layer __

    * [Data Link Layer __4 min read](https://www.geeksforgeeks.org/computer-networks/data-link-layer/)
    * [Switching __3 min read](https://www.geeksforgeeks.org/computer-networks/what-is-switching/)
    * [Virtual LAN __4 min read](https://www.geeksforgeeks.org/computer-networks/virtual-lan-vlan/)
    * [Framing __3 min read](https://www.geeksforgeeks.org/computer-networks/framing-in-data-link-layer/)
    * [Error Control __4 min read](https://www.geeksforgeeks.org/computer-networks/error-control-in-data-link-layer/)
    * [Flow Control __4 min read](https://www.geeksforgeeks.org/computer-networks/flow-control-in-data-link-layer/)
    * [Piggybacking __2 min read](https://www.geeksforgeeks.org/computer-networks/piggybacking-in-computer-networks/)

Network Layer __

    * [Network Layer __3 min read](https://www.geeksforgeeks.org/computer-networks/network-layer-in-osi-model/)
    * [Classful Addressing __7 min read](https://www.geeksforgeeks.org/computer-networks/introduction-of-classful-ip-addressing/)
    * [Classless Addressing __7 min read](https://www.geeksforgeeks.org/computer-networks/ip-addressing-classless-addressing/)
    * [IP Address __11 min read](https://www.geeksforgeeks.org/computer-science-fundamentals/what-is-an-ip-address/)
    * [IPv4 Datagram Header __4 min read](https://www.geeksforgeeks.org/computer-networks/introduction-and-ipv4-datagram-header/)
    * [IPv4 vs IPv6 __3 min read](https://www.geeksforgeeks.org/computer-networks/differences-between-ipv4-and-ipv6/)
    * [Public vs Private IP __4 min read](https://www.geeksforgeeks.org/computer-networks/difference-between-private-and-public-ip-addresses/)
    * [Subnetting __5 min read](https://www.geeksforgeeks.org/computer-networks/introduction-to-subnetting/)
    * [Routing __5 min read](https://www.geeksforgeeks.org/computer-networks/what-is-routing/)
    * [Protocols __9 min read](https://www.geeksforgeeks.org/computer-networks/network-layer-protocols/)

Transport Layer __

    * [Transport Layer __4 min read](https://www.geeksforgeeks.org/computer-networks/transport-layer-in-osi-model/)
    * [Protocols __3 min read](https://www.geeksforgeeks.org/computer-networks/transport-layer-protocols/)
    * [TCP __4 min read](https://www.geeksforgeeks.org/computer-networks/what-is-transmission-control-protocol-tcp/)
    * [UDP __3 min read](https://www.geeksforgeeks.org/computer-networks/user-datagram-protocol-udp/)

Session Layer & Presentation Layer __

    * [Session Layer __2 min read](https://www.geeksforgeeks.org/computer-networks/session-layer-in-osi-model/)
    * [Presentation Layer __3 min read](https://www.geeksforgeeks.org/computer-networks/presentation-layer-in-osi-model/)
    * [Secure Socket Layer __3 min read](https://www.geeksforgeeks.org/computer-networks/secure-socket-layer-ssl/)
    * [Point-to-Point Tunneling Protocol __3 min read](https://www.geeksforgeeks.org/computer-networks/pptp-full-form/)
    * [MIME Protocol __3 min read](https://www.geeksforgeeks.org/computer-networks/multipurpose-internet-mail-extension-mime-protocol/)

Application Layer __

    * [Application Layer __4 min read](https://www.geeksforgeeks.org/computer-networks/application-layer-in-osi-model/)
    * [Client-Server Model __5 min read](https://www.geeksforgeeks.org/system-design/client-server-model/)
    * [WWW __4 min read](https://www.geeksforgeeks.org/computer-networks/world-wide-web-www/)
    * [Electronic Mail __4 min read](https://www.geeksforgeeks.org/computer-science-fundamentals/introduction-to-electronic-mail/)
    * [Content Distribution Network __4 min read](https://www.geeksforgeeks.org/computer-networks/what-is-a-content-distribution-network-and-how-does-it-work/)
    * [Protocols __4 min read](https://www.geeksforgeeks.org/computer-networks/protocols-application-layer/)

Advanced Topics __

    * [Network Security __4 min read](https://www.geeksforgeeks.org/computer-networks/network-security/)
    * [QoS & Multimedia __8 min read](https://www.geeksforgeeks.org/computer-networks/computer-network-quality-of-service-and-multimedia/)
    * [Authentication __3 min read](https://www.geeksforgeeks.org/computer-networks/authentication-in-computer-network/)
    * [Encryption __6 min read](https://www.geeksforgeeks.org/ethical-hacking/encryption-its-algorithms-and-its-future/)
    * [Firewall __2 min read](https://www.geeksforgeeks.org/computer-networks/introduction-of-firewall-in-computer-network/)
    * [MAC Filtering __3 min read](https://www.geeksforgeeks.org/computer-networks/mac-filtering-in-computer-network/)
    * [Wi-Fi Standards __3 min read](https://www.geeksforgeeks.org/computer-networks/wi-fi-standards-explained/)
    * [Bluetooth __5 min read](https://www.geeksforgeeks.org/computer-networks/bluetooth/)
    * [Wireless Communication __5 min read](https://www.geeksforgeeks.org/computer-networks/generations-of-wireless-communication/)
    * [Cloud Networking __4 min read](https://www.geeksforgeeks.org/computer-networks/cloud-networking/)

Practice __

    * [Networking Interview Q &A __15+ min read](https://www.geeksforgeeks.org/blogs/networking-interview-questions/)
    * [TCP/IP Interview Q&A __15+ min read](https://www.geeksforgeeks.org/blogs/top-50-tcp-ip-interview-questions-and-answers/)
    * [Network Fundamentals Interview Questions __15+ min read](https://www.geeksforgeeks.org/blogs/top-50-ip-addressing-interview-questions-and-answers/)
    * [Notes __15+ min read](https://www.geeksforgeeks.org/computer-networks/last-minute-notes-computer-network/)
    * [Cheat Sheet __15+ min read](https://www.geeksforgeeks.org/computer-networks/computer-network-cheat-sheet/)
