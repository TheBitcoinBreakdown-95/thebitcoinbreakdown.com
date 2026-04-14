# Consolidated Failure Report -- btc-index Phase 3 + 3B

**Generated:** 2026-04-12
**Bitcoin Notes scraped failures:** 171
**Medium URLs (never attempted):** 31
**Total unique Medium (deduped WBIGAF + BN):** 36

## Summary

| Category | Count | Recovery Path |
|----------|-------|---------------|
| FTP/Gopher archives | 29 | Skip -- historical, not web-accessible |
| Dead web servers | 25 | Wayback Machine |
| Page gone (404/410) | 33 | Wayback Machine |
| WAF/403 blocked | 52 | Wayback -> Apify (last resort) |
| Timeout | 7 | Retry with longer timeout |
| Deleted tweets | 11 | Unrecoverable |
| Malformed URL | 1 | Skip |
| Other errors | 13 | Case-by-case |
| Medium (Apify queue) | 36 | Apify (paid, last resort) |

---

## 1. Truly Dead -- Skip (41 URLs)

No automated recovery possible.

### FTP/Gopher Archives (29)

Historical cypherpunk-era file servers. Not web-accessible, Wayback cannot archive FTP.

- `https://ftp.atnf.csiro.au`
- `https://ftp.atnf.csiro.au:/pub/people/rgooch'`
- `https://ftp.c2.org`
- `https://ftp.cpsr.org`
- `https://ftp.cs.uow.edu.au`
- `https://ftp.csn.net`
- `https://ftp.csn.org:/mpj/I_will_not_export/crypto_`
- `https://ftp.csua.berkeley.edu`
- `https://ftp.darmstadt.gmd.de`
- `https://ftp.demon.co.uk:/pub/pgp`
- `https://ftp.dhp.com`
- `https://ftp.dsi.unimi.it:/pub/security/crypt/code/schneier`
- `https://ftp.dsi.unimi.it:/pub/security/crypt/PGP`
- `https://ftp.eff.org`
- `https://ftp.informatik.uni`
- `https://ftp.informatik.uni-hamburg.de`
- `https://ftp.informatik.uni-hamburg.de:/pub/virus/crypt/disk`
- `https://ftp.informatik.uni-hamburg.de:/pub/virus/crypt/pgp/shells`
- `https://ftp.netcom.com`
- `https://ftp.netsys.com`
- `https://ftp.ox.ac.uk`
- `https://ftp.soda.csua.edu`
- `https://ftp.std.com:/pub/cme`
- `https://ftp.sumex-aim.stanford.edu/info-mac/nwt/utils/n-crypt`
- `https://ftp.wimsey.bc.ca`
- `https://ftp.wimsey.bc.ca:/pub/crypto`
- `https://ftp.win.tue.nl`
- `https://gopher://chaos.bsu.edu`
- `https://gopher://gopher.eff.org/11/Publications/Bruce_Sterling`

### Deleted Tweets (11)

Both fxtwitter API and Patchright browser failed. Accounts deleted or suspended.

- `https://twitter.com/bitcoin200t/status/1539602114082590720`
- `https://twitter.com/danieleripoll/status/1723425597794443668`
- `https://twitter.com/dergigi/status/1636677865944100864`
- `https://twitter.com/pwuille/status/1259990906997858304`
- `https://twitter.com/reardencode/status/1788074956225651060`
- `https://twitter.com/wef/status/808328302213689344?lang=en`
- `https://x.com/arkade_os/status/2013249214013440084`
- `https://x.com/bitman_pow/status/1724729512024216038`
- `https://x.com/Bryan8094215482/status/1810006201650077957`
- `https://x.com/rewkang/status/1970782770805813392`
- `https://x.com/spirit_satoshi/status/1772274850159030646`

### Malformed URLs (1)

- `https://javascript:window.print\(\`

## 2. Wayback Machine Candidates (58 URLs)

Try `https://web.archive.org/web/{url}` before any paid service.

### Dead Web Servers (25)

Connection refused -- server is down or domain expired. Content may exist in Wayback.

| Domain | URL |
|--------|-----|
| acns.nwu.edu | `https://acns.nwu.edu/surfpunk` |
| awesomelightningnetwork.com | `https://awesomelightningnetwork.com/` |
| bitcoin | `https://bitcoin` |
| cl.cam.ac.uk | `https://cl.cam.ac.uk/users/iwj10` |
| cpsr.org | `https://cpsr.org/cpsr/states/california/cal_gov_info_FAQ.html` |
| cpsr.org | `https://cpsr.org/home` |
| cspsprotocol.com | `https://cspsprotocol.com/p2p-network` |
| digicash.support.nl | `https://digicash.support.nl/` |
| dlc.link | `https://dlc.link/solutions` |
| draco.centerline.com:8080 | `https://draco.centerline.com:8080/~franl/pgp/pgp-` |
| econtalk.org | `https://econtalk.org/nathaniel-popper-on-bitcoin-and-digital-gold` |
| exitcondition.alrubinger.com | `https://exitcondition.alrubinger.com/2022/01/06/an-open-approach-to-financial-freedom` |
| iquest.com | `https://iquest.com/~fairgate/privacy/index.html` |
| justice.gov | `https://justice.gov/usao-nj/pr/somerset-county-man-charged-attempts-provide-material-support-hamas-making-false` |
| lndhub.io~~ | `https://lndhub.io~~` |
| martigny.ai.mit.edu | `https://martigny.ai.mit.edu/~bal/pks-commands.html` |
| netmarket.com | `https://netmarket.com/` |
| news.earn.com | `https://news.earn.com/quantifying-decentralization-e39db233c28e` |
| offlinebitcoins.com | `https://offlinebitcoins.com/` |
| programmingbitcoin.com | `https://programmingbitcoin.com/understanding-segwit-block-size` |
| rgb-faq.com | `https://rgb-faq.com/` |
| rschp2.anu.edu.au:8080 | `https://rschp2.anu.edu.au:8080/crypt.html` |
| theprogressivebitcoiner.com | `https://theprogressivebitcoiner.com/` |
| truthcoin.info | `https://truthcoin.info/blog/protocol-upgrade-terminology` |
| win.tue.nl | `https://win.tue.nl/win/math/dw/index.html` |

### 404 / Page Gone (33)

Active domains but specific page removed. High Wayback recovery probability.

| Domain | URL |
|--------|-----|
| ark-protocol.com | `https://ark-protocol.com/j` |
| arkdev.info | `https://arkdev.info/blog/liquidity-requirements` |
| bitcoinfoundation.org | `https://bitcoinfoundation.org/bitcoin/core-development-update-5` |
| bitrexe.com | `https://bitrexe.com/about` |
| btclexicon.com | `https://btclexicon.com/bitcoin-client` |
| btctools.org | `https://btctools.org/opcodes-list` |
| coindesk.com | `https://coindesk.com/consensus-magazine/2023/10/30/what-will-wall-streets-bitcoin-narrative-be` |
| cointelegraph.com | `https://cointelegraph.com/innovation-circle/understanding-crypto-custody-what-different-solutions-entail-for-investors-and-businesses` |
| cointelegraph.com | `https://cointelegraph.com/learn/bitcoin-etfs-a-beginners-guide-to-exchange-traded-funds` |
| cointelegraph.com | `https://cointelegraph.com/learn/who-is-satoshi-nakamoto-the-creator-of-bitcoin` |
| cointelegraph.com | `https://cointelegraph.com/lightning-network-101/what-is-lightning-network-and-how-it-works` |
| eff.org | `https://eff.org/pub/Publications/Bruce_Sterling/cfp_` |
| en.bitcoin.it | `https://en.bitcoin.it/wiki/Covenants_support\` |
| fedimint.org | `https://fedimint.org/docs/FAQs/WhyCommunityCustody` |
| fedimint.org | `https://fedimint.org/docs/intro` |
| finance.yahoo.com | `https://finance.yahoo.com/news/paying-taco-bell-dogecoin-may-113720323.html` |
| gamestation.net | `https://gamestation.net/d16-hexidice.html` |
| grayscale.com | `https://grayscale.com/crypto-products/grayscale-bitcoin-trust` |
| heliolending.com | `https://heliolending.com/2021/09/10/can-crypto-loans-help-pay-off-student-loans` |
| horizen.io | `https://horizen.io/academy/zendoo` |
| learn.saylor.org | `https://learn.saylor.org/course/PRDV151` |
| lightco.in | `https://lightco.in/2024/02/13/bitstake` |
| microsoft.com | `https://microsoft.com/en-us/research/publication/byzantine-generals-problem/_` |
| microstrategy.com | `https://microstrategy.com/en/bitcoin/documents/stone-ridge-2020-shareholder-letter` |
| mycryptopedia.com | `https://mycryptopedia.com/drivechain-explained` |
| nakamoto.com | `https://nakamoto.com/bitcoin-becomes-the-flag-of-technology` |
| nakamoto.com | `https://nakamoto.com/what-are-the-key-properties-of-bitcoin` |
| openmarket.com | `https://openmarket.com/info/cryptography/applied_crypt` |
| protos.com | `https://protos.com/what-is-miniscript/====` |
| sequentia.io | `https://sequentia.io/academy` |
| tftc.io | `https://tftc.io/issue-754` |
| unchained.com | `https://unchained.com/blog/bitcoin-inscriptions-ordinals==` |
| whitehouse.gov | `https://whitehouse.gov/briefing-room/statements-releases/2022/02/26/joint-statement-on-further-restrictive-economic-measures` |

## 3. WAF/403 Blocked (52 URLs)

Sites are live but blocking scrapers. Try Wayback first, then Apify as last resort.

| Domain | URL |
|--------|-----|
| americanliterature.com | `https://americanliterature.com/history/franklin-d-roosevelt/legislative/executive-order-6102` |
| americanthinker.com | `https://americanthinker.com/blog/2021/10/ready_for_the_government_to_control_how_you_spend_your_money.html` |
| ark-invest.com | `https://ark-invest.com/big-ideas-2023/bitcoin` |
| atlanticcouncil.org | `https://atlanticcouncil.org/blogs/econographics/strengthening-ties-china-and-the-gcc` |
| beincrypto.com | `https://beincrypto.com/crypto-adoption-higher-minorities-lgbtq-america` |
| bitcoin.stackexchange.com | `https://bitcoin.stackexchange.com/questions/106783/will-a-hard-fork-be-required-to-change-timestamp-fields` |
| bitcoin.stackexchange.com | `https://bitcoin.stackexchange.com/questions/29554/explanation-of-what-an-op-return-transaction-looks-like` |
| bitcoin.stackexchange.com | `https://bitcoin.stackexchange.com/questions/408/does-hoarding-really-hurt-bitcoin` |
| bitcoin.stackexchange.com | `https://bitcoin.stackexchange.com/questions/79182/january-19th-2038-rip-unix-timestamps` |
| bitcoin.stackexchange.com | `https://bitcoin.stackexchange.com/users/403/theymos` |
| bitcoinrollups.org | `https://bitcoinrollups.org/` |
| bitrefill.com | `https://bitrefill.com/` |
| blockchain.info | `https://blockchain.info/` |
| blog.chain.link | `https://blog.chain.link/dlc-link-chainlink-grant-bitcoin-discreet-log-contracts` |
| blog.trezor.io | `https://blog.trezor.io/how-bitcoin-boomed-in-2021-a64cccca6f71` |
| bloom.bg | `https://bloom.bg/dg-ws-core-bcom-m1` |
| cmegroup.com | `https://cmegroup.com/education/featured-reports/an-in-depth-look-at-the-economics-of-bitcoin.html` |
| coinsutra.com | `https://coinsutra.com/paid-blockchain-cryptocurrency-online-courses-certifications` |
| cs.berkeley.edu | `https://cs.berkeley.edu/~raph/remailer-list.html` |
| cygnus.com | `https://cygnus.com/~gnu/export.html` |
| dcjournal.com | `https://dcjournal.com/the-end-of-the-money-middlemen` |
| fintel.io | `https://fintel.io/fg/us/gbtc/CommonSharesOutstanding` |
| foundation.xyz | `https://foundation.xyz/2023/02/making-sense-of-stealth-addresses` |
| gate.io | `https://gate.io/learn/articles/13-lines-of-code-help-bitcoin-implement-smart-contracts-understand-the-op-cat-soft-fork/1681` |
| group30.org | `https://group30.org/publications/detail/4950` |
| hrf.org | `https://hrf.org/latest/cisa-research-paper` |
| hrw.org | `https://hrw.org/news/2017/12/12/chinas-chilling-social-credit-blacklist` |
| inleo.io | `https://inleo.io/@edicted/rune-lending-followup` |
| login.xyz | `https://login.xyz` |
| mantis.co.uk | `https://mantis.co.uk/~mathew` |
| mantis.co.uk | `https://mantis.co.uk/pgp/pgp.html` |
| markets.createsend1.com | `https://markets.createsend1.com/t/d-l-ahidlut-tutjgdjty-d` |
| markets.createsend1.com | `https://markets.createsend1.com/t/d-l-ahidlut-tutjgdjty-i` |
| markets.createsend1.com | `https://markets.createsend1.com/t/d-l-ahidlut-tutjgdjty-v` |
| nitv.net | `https://nitv.net/~mech/Romana/stego.html` |
| njump.me | `https://njump.me/nevent1qvzqqqqqqypzqgvra9r4sjqapufyl0vnc4kv4fz70e29em4c655y37vz206f0wt4qywhwumn8ghj7mn0wd68ytnzd96xxmmfdejhytnnda3kjctv9uq32amnwvaz7tmwdaehgu3wdau8gu3wv3jhvtcqyp0x6urd9zf37nl6p6r6ycvnphrx24gel0jgl5f0ck5dgmg9uhw4q4mkjnz` |
| papers.ssrn.com | `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3141240` |
| politico.com | `https://politico.com/news/2022/01/16/bitcoin-crashes-the-midterms-527126` |
| pubsonline.informs.org | `https://pubsonline.informs.org/doi/abs/10.1287/mnsc.2023.4885` |
| qz.com | `https://qz.com/1642441/extradition-law-why-hong-kong-protesters-didnt-use-own-metro-cards` |
| qz.com | `https://qz.com/africa/1922466/how-bitcoin-powered-nigerias-endsars-protests` |
| rfc-editor.org | `https://rfc-editor.org/ien/ien2.txt` |
| sec.gov | `https://sec.gov/Archives/edgar/data/1588489/000119312524003901/d144925ds3a.htm` |
| sec.gov | `https://sec.gov/news/press-release/2023-139` |
| seekingalpha.com | `https://seekingalpha.com/symbol/BTC-USD` |
| seekingalpha.com | `https://seekingalpha.com/symbol/ETH-USD` |
| theafricareport.com | `https://theafricareport.com/131083/african-countries-are-adopting-crypto-faster-than-their-global-counterparts` |
| thesaifhouse.wpcomstaging.com | `https://thesaifhouse.wpcomstaging.com/2017/05/19/economics-of-bitcoin-as-a-settlement-network` |
| thoughtco.com | `https://thoughtco.com/postal-service-losses-by-year-3321043` |
| udemy.com | `https://udemy.com/course/bitcoin-certification` |
| upload.wikimedia.org | `https://upload.wikimedia.org/wikipedia/commons/8/87/IBM_card_storage.NARA.jpg**` |
| weforum.org | `https://weforum.org/great-reset` |

## 4. Timeout / Retry (7 URLs)

Could succeed with longer timeout, different network, or retry.

- `https://dtcc.com/clearing-services/ficc-gov` (Timeout)
- `https://dtcc.com/~/media/Files/Downloads/WhitePapers/FICC-Central-Clearing-WP-Treasury-Market` (Timeout)
- `https://investopedia.com/articles/forex-currencies/091416/what-would-it-take-us-dollar-collapse.asp` (Browser timeout)
- `https://investopedia.com/terms/r/reservecurrency.asp` (Browser timeout)
- `https://quadralay.com/www/Crypt/Crypt.html` (Timeout)
- `https://roygbiv.money/` (Timeout)
- `https://sptfy.com/9oFO` (Timeout)

## 5. Other Errors (13 URLs)

- `https://archive.is/xNuVR` -- HTTP 429 (rate limited)
- `https://coinsloth.com/product/study-bitcoin` -- HTTP 500 (server error)
- `https://developer.tbd.website/projects/ssi` -- HTTP 500 (server error)
- `https://founders.archives.gov/documents/Washington/99-01-02-08500` -- HTTP 202
- `https://fred.stlouisfed.org/series/G160371A027NBEA` -- ReadError: [WinError 10054] An existing connection was forcibly closed by the remote host
- `https://fred.stlouisfed.org/series/MVMTD027MNFRBDAL` -- ReadError: [WinError 10054] An existing connection was forcibly closed by the remote host
- `https://github.com/bip420/bip420` -- No README found
- `https://github.com/bitcoin/bips` -- No README found
- `https://github.com/grondilu/bitcoin-bash-tools` -- No README found
- `https://github.com/LibertyFarmer/hamstr` -- No README found
- `https://microsoft.com/en-us/research/publication/reaching__agreement-presence-faults` -- InvalidURL: Invalid non-printable ASCII character in URL, '\x02' at position 59.
- `https://miningsyndicate.com/blogs/news/the-story-of-satoshi-nakamoto-bitcoin-s-founder` -- HTTP 402
- `https://usnews.com/news/world-report/articles/2021-09-07/china-weighing-occupation-of-former-us-air-base-at-bagram-sources` -- ReadError: [WinError 10054] An existing connection was forcibly closed by the remote host

## 6. Medium URLs -- Apify Queue (36 unique)

All Medium articles fail due to Cloudflare Turnstile CAPTCHA. Apify is the only
recovery path. Wait until all free methods are exhausted on other categories first.

| # | URL | WBIGAF Refs | BN Sources |
|----|-----|-------------|------------|
| 1 | `https://allenfarrington.medium.com/bitcoin-is-halal-4a8f0560c3d0` | 8.8 | BTC\Bitcoin as a religion.md |
| 2 | `https://allenfarrington.medium.com/bitcoin-is-venice-8414dda4207` | -- | BTC\Read again.md |
| 3 | `https://allenfarrington.medium.com/bitcoin-is-venice-8414dda42070` | -- | BTC\BTC library.md |
| 4 | `https://allenfarrington.medium.com/trust-me-bro-fb5a25964634` | -- | BTC\Black Rock ETF.md |
| 5 | `https://breedlove22.medium.com/masters-and-slaves-of-money-255ecc93404f` | -- | BTC\BTC library.md |
| 6 | `https://breedlove22.medium.com/the-number-zero-and-bitcoin-4c193336db5b` | 5.16, 8.10 | -- |
| 7 | `https://burakkeceli.medium.com/introducing-ark-6f87ae45e272` | -- | BTC\ARK – Layer 2.md |
| 8 | `https://danhedl.medium.com/bitcoins-distribution-was-fair-e2ef7bbbc892` | 4.3, 5.18 | -- |
| 9 | `https://danhedl.medium.com/planting-bitcoin-sound-money-72e80e40ff62` | 5.13 | -- |
| 10 | `https://jimmysong.medium.com/debunking-the-empty-block-attack-10513858b3f8` | -- | BTC\BTC library.md |
| 11 | `https://medium.com/@Bitlayer/bitvm-and-its-optimization-considerations-007da599d8ac` | -- | BTC\Scriptless Scripts BitVM.md |
| 12 | `https://medium.com/@Marketsbylili/how-to-secretly-travel-with-bitcoin-using-steganography-6e99a7ca9ad9` | -- | BTC\Steganography.md |
| 13 | `https://medium.com/@MiguelCuneta_21450/its-too-late-nothing-can-stop-the-bitcoin-protocol-738047bb5201` | 4.5, 5.4 | BTC\Bitcoin the internet of value.md, BTC\BTC library.md |
| 14 | `https://medium.com/@aantonop/why-dumb-networks-are-better-f0b94c271b76` | -- | BTC\Bitcoin the internet of value.md, BTC\BTC library.md |
| 15 | `https://medium.com/@nic__carter/a-most-peaceful-revolution-8b63b64c203e` | -- | BTC\A revolution.md |
| 16 | `https://medium.com/@nic__carter/bitcoin-at-12-f6fce39cb9bb` | 4.1, 9.6 | BTC\BTC library.md |
| 17 | `https://medium.com/@nic__carter/its-the-settlement-assurances-stupid-5dcd1c3f4e41` | -- | BTC\BTC library.md |
| 18 | `https://medium.com/@nic__carter/setting-the-record-straight-b4e1b415e7d9` | -- | BTC\Maxi.md |
| 19 | `https://medium.com/@ottosch/how-bip47-works-ee641cc14bf3` | -- | BTC\PayNyms.md |
| 20 | `https://medium.com/blockstream/cat-and-schnorr-tricks-i-faf1b59bd298` | -- | BTC\The Great Script Restoration (GSR).md |
| 21 | `https://medium.com/breez-technology/the-breez-open-lsp-model-scaling-lightning-by-sharing-roi-with-3rd-party-lsps-e2ef6e31562e` | -- | Lightning ⚡️\Breez SDK.md |
| 22 | `https://medium.com/coinmonks/origin-of-money-e04e756578e7` | -- | BTC\Origins of Money.md |
| 23 | `https://medium.com/digitalassetresearch/schnorr-signatures-the-inevitability-of-privacy-in-bitcoin-b2f45a1f7287` | -- | BTC\Taproot 22.0.md |
| 24 | `https://medium.com/hackernoon/bitcoin-miners-beware-invalid-blocks-need-not-apply-51c293ee278b` | -- | BTC\BTC library.md |
| 25 | `https://medium.com/interdax/the-symbolic-link-between-the-bitcoin-white-paper-and-halloween-2a967d273ca4` | -- | BTC\BTC library.md |
| 26 | `https://medium.com/mycrypto/the-future-of-ethereum-doesnt-have-wallets-232fcee708bf` | -- | BTC\BTC library.md |
| 27 | `https://medium.com/the-bitcoin-times/the-greatest-game-b787ac3242b2` | -- | BTC\BTC library.md |
| 28 | `https://notgrubles.medium.com/one-does-not-simply-censor-bitcoin-89dc4a32ba2b` | 5.2 | BTC\BTC library.md, BTC\Censorship resistance.md, Memes\Photosmemes.md |
| 29 | `https://paulbars.medium.com/magic-internet-money-how-a-reddit-ad-made-bitcoin-hit-1000-and-inspired-south-parks-art-b414ec7a5598` | -- | BTC\Rants.md |
| 30 | `https://pierre-rochard.medium.com/the-utility-of-saving-c56f7c170fc1` | 5.15 | -- |
| 31 | `https://rextar4444.medium.com/an-inquiry-into-john-nashs-proposal-for-ideal-money-f1551c46da31` | -- | BTC\John Nash Ideal Money.md |
| 32 | `https://shanakaanslemperera.medium.com/the-thermodynamic-monetary-transition-how-bitcoins-30-universal-laws-signal-humanity-s-shift-from-a23a3a3783ec` | 8.7 | -- |
| 33 | `https://tomerstrolight.medium.com/the-legendary-treasure-of-satoshi-nakamoto-c3621c5b2106` | 4.3, 4.5 | BTC\SATOSHI’S TREASURE.md |
| 34 | `https://tomerstrolight.medium.com/the-problem-with-ethereum-af9692f4af95` | -- | BTC\Ethereum.md |
| 35 | `https://vijayboyapati.medium.com/the-bullish-case-for-bitcoin-6ecc8bdecc1` | 4.5, 5.2, 5.3, 5.5, 5.15, 5.16 (via breedlove), 7.1 | BTC\Bitcoin as a religion.md, BTC\BTC library.md |
| 36 | `https://waterdripcapital.medium.com/driving-mass-adoption-of-crypto-how-the-rgb-protocol-is-illuminating-the-future-of-bitcoin-f45e60af8239` | -- | BTC\RGB.md |

---

## Recovery Plan

### Phase A: Wayback Machine (free)
- Target: 58 URLs (dead servers + 404 pages)
- Also try on WAF/403 URLs where the content existed before
- Use archive.org Wayback Machine API: `http://archive.org/wayback/available?url=TARGET`

### Phase B: Retry with Adjustments
- Target: 7 timeout URLs + 13 other errors
- Longer timeout (60s), different User-Agent, retry read errors

### Phase C: Check Notebook Context
- For remaining failures, check if the Bitcoin Note that linked the URL
  already contains the key content inline (quote, summary, argument)
- If so, the scrape is unnecessary -- the corpus already has the substance

### Phase D: Apify (paid, last resort)
- Target: 36 Medium URLs + any high-value WAF survivors
- Gate: user approval required per feedback_apify_last_resort.md
- Token in Ai Playground/.env

