# blog.lopp.net -- Scraped Content

**URL:** https://blog.lopp.net/who-controls-bitcoin-core-
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Golden rules.md
**Scraped:** 2026-04-12

---

[ Cypherpunk Cogitations ](https://blog.lopp.net)

Sign in

Dec 15, 2018  14 min read  [bitcoin](/tag/bitcoin/)

# Who Controls Bitcoin Core?

Understanding how the focal point of Bitcoin development operates. 

[Jameson Lopp](/author/jameson/)

_Note_ : if you'd prefer to consume this essay in audio format, you can [listen to it here](https://lopp.net/media-archive/presentations/Who_Controls_Bitcoin_Core.mp3?ref=blog.lopp.net) (narrated by [Guy Swann](https://guyswann.com/?ref=blog.lopp.net) of the Bitcoin Audible Podcast.)

* * *

The question of who controls the ability to merge code changes into [Bitcoin Core](https://bitcoincore.org/?ref=blog.lopp.net)’s [GitHub repository](https://github.com/bitcoin/bitcoin?ref=blog.lopp.net) tends to come up on a recurring basis. This has been cited as a “central point of control” of the Bitcoin protocol by various parties over the years, but I argue that the question itself is a red herring that stems from an authoritarian perspective — this model does not apply to Bitcoin. It’s certainly not obvious to a layman as to why that is the case, thus the goal of this article is to explain how Bitcoin Core operates and, at a higher level, how the Bitcoin protocol itself evolves.

## The History of Bitcoin Core

Bitcoin Core is a [focal point](https://en.wikipedia.org/wiki/Focal_point_%28game_theory%29?ref=blog.lopp.net) for development of the Bitcoin protocol rather than a point of command and control. If it ceased to exist for any reason, a new focal point would emerge — the technical communications platform upon which it’s based (currently the GitHub repository) is a matter of convenience rather than one of definition / project integrity. In fact, we have already seen Bitcoin’s focal point for development change platforms and even names!

  * In early 2009 the source code for the Bitcoin project was [simply a .rar file](http://www.metzdowd.com/pipermail/cryptography/2009-January/014994.html?ref=blog.lopp.net) hosted on SourceForge. Early developers would actually exchange code patches with Satoshi [via email](https://online.wsj.com/public/resources/documents/finneynakamotoemails.pdf?ref=blog.lopp.net).
  * On October 30 2009, Sirius ([Martti Malmi](https://medium.com/u/2d55f06ada18?ref=blog.lopp.net)) [created a subversion repository](https://sourceforge.net/p/bitcoin/code/1/?ref=blog.lopp.net) for the Bitcoin project on SourceForge
  * In 2011, the [Bitcoin project migrated](https://sourceforge.net/p/bitcoin/code/252?ref=blog.lopp.net) from SourceForge to [GitHub](https://github.com/bitcoin/bitcoin/commit/ca40e581ebcdc85dba15c1e873f5e5aedda45b77?ref=blog.lopp.net)
  * In 2014 the Bitcoin project [was renamed to Bitcoin Core](https://github.com/bitcoin/bitcoin/pull/3408?ref=blog.lopp.net)


## Trust No One

While there are a handful of GitHub “maintainer” accounts at the organization level that have the ability to merge code into the master branch, this is more of a janitorial function than a position of power. If anyone could merge into master it would very quickly turn into a “too many cooks in the kitchen” scenario. Bitcoin Core follows principles of least privilege that any power bestowed to individuals is easily subverted if it is abused.

> Core is transparent about the list that matters: the PGP keys who can sign merge commits.  
>   
> The lesson to be learned here is to not trust GitHub! Even Bitcoin Core doesn't know the full list of people who can change the repo, as that extends to probably dozens of GitHub employees.
> 
> — Peter Todd (@peterktodd) [October 4, 2018](https://twitter.com/peterktodd/status/1047854713029312512?ref_src=twsrc%5Etfw&ref=blog.lopp.net)

From an adversarial perspective, GitHub can not be trusted. Any number of GitHub employees could use their administrative privileges to inject code into the repository without consent from the maintainers. But it’s unlikely that a GitHub attacker would also be able to compromise the PGP key of a Bitcoin Core maintainer.

Rather than base the integrity of the code off of GitHub accounts, Bitcoin Core has a continuous integration system that performs checks of trusted PGP keys that must sign every merge commit. While these keys are tied to known identities, it’s still not safe to assume that it will always be the case — a key could be compromised and we wouldn’t know unless the original key owner notified the other maintainers. As such, the commit keys do not provide perfect security either, they just make it more difficult for an attacker to inject arbitrary code.

## The Keys to the Kingdom

At time of writing, [these are the trusted PGP fingerprints](https://github.com/bitcoin/bitcoin/blob/master/contrib/verify-commits/trusted-keys?ref=blog.lopp.net):

> 71A3B16735405025D447E8F274810B012346C9A6  
> 133EAC179436F14A5CF1B794860FEB804E669320  
> 32EE5C4C3FA15CCADB46ABE529D4BCB6416F53EC  
> B8B3F1C0E58C15DB6A81D30C3648A882F4316B9B  
> CA03882CB1FC067B5D3ACFE4D300116E1C875A3D

These keys are registered to:

> Wladimir J. van der Laan <[laanwj@protonmail.com](mailto:laanwj@protonmail.com)>  
> Pieter Wuille <[pieter.wuille@gmail.com](mailto:pieter.wuille@gmail.com)>  
> Jonas Schnelli <[dev@jonasschnelli.ch](mailto:dev@jonasschnelli.ch)>  
> Marco Falke <[marco.falke@tum.de](mailto:marco.falke@tum.de)>  
> Samuel Dobson <[dobsonsa68@gmail.com](mailto:dobsonsa68@gmail.com)>

Does this mean that we are trusting these five people? Not quite. Keys are not a proof of identity — these keys could potentially fall into the hands of other people. What assurances do you really get if you run the verify-commits python script?

> python3 contrib/verify-commits/verify-commits.py   
> Using verify-commits data from bitcoin/contrib/verify-commits  
> All Tree-SHA512s matched up to 309bf16257b2395ce502017be627186b749ee749  
> There is a valid path from “HEAD” to 82bcf405f6db1d55b684a1f63a4aabad376cdad7 where all commits are signed!

The [verify-commits](https://github.com/bitcoin/bitcoin/tree/master/contrib/verify-commits?ref=blog.lopp.net) script is an integrity check that any developer can run on their machine. When executed, it checks the PGP signature on every single merge commit since commit 82bcf405… in December 2015 — over 3,400 merges at time of writing. If the script completes successfully, it tells us that every line of code that has been changed since that point has passed through the Bitcoin Core development process and been “signed off” by someone with a maintainer key. While this is not a bulletproof guarantee that no one has injected malicious code (a maintainer could go rogue or have their keys stolen), it reduces the attack surface for doing so enormously. What are maintainers and how did they attain this role? We’ll dig into that a bit later.

## Layered Security

The integrity of Bitcoin Core’s code must not rely solely upon a handful of cryptographic keys, which is why there are a multitude of other checks in place. There are many layers of security here to provide defense in depth:

### Pull Request Security

  1. Anyone is free to propose code changes to improve the software by opening a pull request against the master branch on [bitcoin/bitcoin](https://github.com/bitcoin/bitcoin?ref=blog.lopp.net).
  2. Developers review pull requests to ensure that they are not harmful. Anyone is free to review pull requests and provide feedback — there is no gatekeeper or entrance exam when it comes to contributing to Bitcoin Core. If a pull request gets to the point that there are no reasonable objections to it being merged, a maintainer makes the merge.
  3. Core maintainers set [this pre-push hook](https://github.com/bitcoin/bitcoin/blob/master/contrib/verify-commits/pre-push-hook.sh?ref=blog.lopp.net) to ensure that they don’t push unsigned commits into the repository.
  4. Merge commits are optionally securely timestamped [via OpenTimestamps](https://github.com/bitcoin/bitcoin/blob/ebd786b72a2a15143d7ef4ea2229fef121bd8f12/contrib/devtools/README.md?ref=blog.lopp.net#create-and-verify-timestamps-of-merge-commits)
  5. The [Travis Continuous Integration system](https://travis-ci.org/bitcoin/bitcoin?ref=blog.lopp.net) regularly runs [this script](https://github.com/bitcoin/bitcoin/blob/v0.21.0/ci/lint/06_script.sh?ref=blog.lopp.net) to check the integrity of the git tree (history) and to verify that all commits in the master branch were signed with one of the trusted PGP keys.
  6. Anyone who wants to can run [this script](https://github.com/bitcoin/bitcoin/blob/master/contrib/verify-commits/verify-commits.py?ref=blog.lopp.net) to verify the PGP signatures on all of the merge commits going back to December 2015. I ran it while writing this article and it took 25 minutes to complete on my laptop.


### Release Security

  1. Deterministic build systems are run independently by multiple developers with the goal of creating identical binaries. If someone manages to create a build that doesn’t match the builds of other developers, it’s a sign that non-determinism was introduced and thus the final release isn’t going to happen. If there is non-determinism, developers track down what went wrong, fix it, then build another release candidate. Once a deterministic build has succeeded then the developers sign the resulting binaries, guaranteeing that the binaries and tool chain were not tampered with and that the same source was used. This method removes the build and distribution process as a single point of failure. Anyone with the technical skills can run their own build system; for versions prior to v21 Bitcoin Core used [these instructions for Gitian](https://github.com/bitcoin/bitcoin/blob/v0.14.0/doc/gitian-building.md?ref=blog.lopp.net); newer releases use [these instructions for Guix](https://github.com/bitcoin/bitcoin/blob/v23.0/contrib/guix/INSTALL.md?ref=blog.lopp.net).
  2. Once the builds have completed successfully and been signed off by the builders, a Bitcoin Core maintainer will PGP sign a message with the SHA256 hashes of each build. If you decide to run a prebuilt binary, you can check its hash after downloading and then verify the authenticity of the signed release message with the hashes. Instructions for doing so [can be found here](https://bitcoincore.org/en/download/?ref=blog.lopp.net).
  3. All of the above is open source and auditable by anyone with the skills and desire to do so.
  4. Finally, even after going through all of the above quality and integrity checks, code that is committed into Bitcoin Core and eventually rolled into a release is not deployed out onto the network of nodes by any centralized organization. Rather, each node operator must make a conscious decision to update the code they run. **Bitcoin Core deliberately does not include an auto-update feature, since it could potentially be used to make users run code that they didn’t explicitly choose**.


Despite all of the technical security measures that are implemented by the Bitcoin Core project, none of them are perfect and any of them can theoretically be compromised. The last line of defense for the integrity of Bitcoin Core’s code is the same as any other open source project — _constant vigilance_. The more eyes that are reviewing Bitcoin Core’s code, the less likely that malicious or flawed code will make it into a release.

## Code Coverage

Bitcoin Core has a lot of testing code. There is an integration test suite that runs against every PR and an extended test suite that runs every night on master.

You can check the code coverage of the tests yourself by:

  1. Cloning the Bitcoin Core GitHub repository
  2. Installing the [required dependencies](https://github.com/bitcoin/bitcoin/tree/master/doc?ref=blog.lopp.net#building) for building from source
  3. Running [these commands](https://github.com/bitcoin/bitcoin/blob/master/doc/developer-notes.md?ref=blog.lopp.net#compiling-for-test-coverage)
  4. Viewing the report at ./total_coverage/index.html


Alternatively, you can view the coverage report Marco Falke [hosts here](https://drahtbot.github.io/reports/coverage/bitcoin/bitcoin/master/total.coverage/index.html?ref=blog.lopp.net).

Code Coverage Report

Having such a high level of test coverage means that there is a higher level of certainty that the code functions as intended.

Testing is a big deal when it comes to consensus critical software. For particularly complex changes, developers sometimes perform painstaking mutation testing — that is, they test the tests by purposely breaking the code and seeing if the tests fail as expected. Greg Maxwell gave some insight into this process when he discussed the 0.15 release:

> “The test is the test of the software, but what’s the test of the test? The software. To test the test, you must break the software.” — Greg Maxwell

## Free Market Competition

BitMEX [wrote a great article](https://blog.bitmex.com/bitcoin-cores-competition/?ref=blog.lopp.net) about the ecosystem of Bitcoin implementations. There are over a dozen different Bitcoin compatible implementations, and even more “competing network” implementations. This is the freedom of open source — anyone who is dissatisfied with the efforts of the Bitcoin Core project is free to start their own project. They can do so from scratch or they can fork the Core software.

At time of writing, 96% of reachable Bitcoin nodes are running some version of Bitcoin Core. Why is this the case? How can Bitcoin Core have near-monopoly status over the network of nodes if the effort required to switch to another software implementation is minimal? After all, many other implementations provide RPC APIs that are compatible with, or at least highly similar to Bitcoin Core.

I believe that this is a result of Bitcoin Core being a focal point for development. It has orders of magnitude more developer time and talent backing it, which means that the code produced by the Bitcoin Core project tends to be the most performant, robust, and secure. Node operators don’t want to run the second best software when it comes to managing money. Also, given that this is consensus software and the Bitcoin protocol does not — and arguably can not — have a formal specification because no one has the authority to write one, it’s somewhat safer to use the focal point implementation because you’re more likely to be bug-for-bug compatible with most of the rest of the network. In this sense, the code of the development focal point is the closest thing to a specification that exists.

## Who Are the Core Developers?

People who are unfamiliar with the [Bitcoin Core development process](https://github.com/bitcoin/bitcoin/blob/master/CONTRIBUTING.md?ref=blog.lopp.net) may look at the project from the outside and consider Core to be a monolithic entity. This is far from the case! There are frequent disagreements between Core contributors and even [the most](https://github.com/bitcoin/bitcoin/pulls?utf8=%E2%9C%93&q=is%3Aclosed+is%3Aunmerged+is%3Apr+author%3Alaanwj&ref=blog.lopp.net) [prolific contributors](https://github.com/bitcoin/bitcoin/pulls?utf8=%E2%9C%93&q=is%3Aclosed+is%3Aunmerged+is%3Apr+author%3Asipa+&ref=blog.lopp.net) have written plenty of code that has never been merged into the project. If you read the guidelines for contributing you may note that they are fairly loose — the process could be best described as “[rough consensus](https://tools.ietf.org/html/rfc7282?ref=blog.lopp.net).”

> Maintainers will take into consideration if a patch is in line with the general principles of the project; meets the minimum standards for inclusion; and will judge the general consensus of contributors.

Who are the Bitcoin Core maintainers? They are contributors who have built up sufficient social capital within the project by making quality contributions over a period of time. When the existing group of maintainers believes that it would be prudent to extend the role to a contributor who has exhibited competence, reliability, and motivation in a certain area, they can grant commit access to that person’s GitHub account. The lead maintainer role is for someone who has oversight over all aspects of the project and is responsible for coordinating releases. It has been voluntarily passed along over the years:

  * Satoshi Nakamoto: 1/3/09 - [2/23/11](https://sourceforge.net/p/bitcoin/mailman/message/27102906/?ref=blog.lopp.net)
  * [Gavin Andresen](https://medium.com/u/7032003d8001?ref=blog.lopp.net): [2/23/11](https://sourceforge.net/p/bitcoin/mailman/message/27102906/?ref=blog.lopp.net) \- [4/7/14](https://bitcoinfoundation.org/bitcoin-core-maintainer-wladimir-van-der-laan/?ref=blog.lopp.net)
  * [Wladimir](https://medium.com/u/5a1694f832c6?ref=blog.lopp.net) van der Laan: [4/7/14](https://bitcoinfoundation.org/bitcoin-core-maintainer-wladimir-van-der-laan/?ref=blog.lopp.net) — present


Acting as a Bitcoin Core maintainer is often referred to as janitorial work because maintainers don’t actually have the power to make decisions that run contrary to the consensus of contributors or of the users. However, the role can be quite taxing due to the extra attention from the ecosystem at large. For example, Gregory Maxwell gave up his maintainer role in 2017 [for personal reasons](https://www.reddit.com/r/Bitcoin/comments/3x7mrr/gmaxwell_unullc_no_longer_a_bitcoin_committer_on/cy29vkx/?ref=blog.lopp.net), likely due to the public pressure he experienced during the scaling debate. [Wladimir wrote a thoughtful post](https://laanwj.github.io/2016/05/06/hostility-scams-and-moving-forward.html?ref=blog.lopp.net) about the stress of being a Core maintainer and why it was appropriate to remove Gavin’s commit access, which upset a lot of people.

Similarly, when [Jeff Garzik](https://medium.com/u/765aa39f1042?ref=blog.lopp.net) was removed from the GitHub organization, he and others were upset about it, but he [had not contributed to Core in two years](https://www.reddit.com/r/Bitcoin/comments/6uec40/jeff_garzik_has_been_removed_from_the_bitcoin/?ref=blog.lopp.net). Leaving his GitHub account with write access to the repository was providing no benefit to the project — it was only creating a security risk and violated the principle of least privilege to which Wladimir referred in his post.

Others may look at Core and believe it to be a technocracy or ivory tower that makes it difficult for new entrants to join. But if you speak to contributors, you’ll find that’s not the case. While only [a dozen people](https://bitcointalk.org/index.php?topic=1774750.0&ref=blog.lopp.net) have had commit access over the years, hundreds of developers have made contributions. I myself have made a few small contributions; while I don’t consider myself a “Core developer” I _technically_ am one. No one can stop you from contributing!

> In 2011, as a high school student who didn't understand what a pointer was, the [@bitcoincoreorg](https://twitter.com/bitcoincoreorg?ref_src=twsrc%5Etfw&ref=blog.lopp.net) developer community (especially people like Greg Maxwell, [@pwuille](https://twitter.com/pwuille?ref_src=twsrc%5Etfw&ref=blog.lopp.net), etc) worked with me to make my shitty patches worth merging and made it a great environment to learn in.
> 
> — Matt Corallo (@TheBlueMatt) [November 18, 2018](https://twitter.com/TheBlueMatt/status/1064292104346771458?ref_src=twsrc%5Etfw&ref=blog.lopp.net)

> In 2016, [@TheBlueMatt](https://twitter.com/TheBlueMatt?ref_src=twsrc%5Etfw&ref=blog.lopp.net) organised a residency at [@ChaincodeLabs](https://twitter.com/ChaincodeLabs?ref_src=twsrc%5Etfw&ref=blog.lopp.net). I'd been reading everything about Bitcoin I could lay my hands on but hadn't dared submit a PR. Matt, Alex and Suhas were extraordinarily generous with their time in teaching us about Bitcoin and how to contribute.
> 
> — John Newbery (@jfnewbery) [November 18, 2018](https://twitter.com/jfnewbery/status/1064301049534664707?ref_src=twsrc%5Etfw&ref=blog.lopp.net)

> I started making small commits to [@bitcoincoreo

[... truncated at 20,000 characters ...]
