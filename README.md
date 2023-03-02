![](https://img.shields.io/github/issues/cyclothymia/Socials-Email-Checker)
![](https://img.shields.io/github/stars/cyclothymia/Socials-Email-Checker)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# A Social Media Email Link Checker
A simple social media email checker that checks a bulk list of emails utilising proxies.

### Current supported social media
- Instagram
- Twitter

## Requirements & Setup
The required language is Python, and pip libraries currently necessary is just `requests`.

## How to use
1. Download `Socials-Email-Checker`
2. Run `pip install requests` in the terminal.
3. Add HTTPS proxies into "proxylist.txt". If you don't have proxies, run `python proxyscraper.py` to scrape for publicly available proxies that will be added to "proxylist.txt" upon completion.
4. Add emails to be checked to "emails.txt"
5. Run `python twitter.py` to check on twitter, and `python instagram.py` to check on instagram.
6. A prompt will come up asking for the filename. Enter the filename of the list. If you did step 4, type "emails.txt" and press enter.
7. If an email is linked on the checked social media, the email will be added to a list named after the social media.

## Recommendations
I recommend you purchase HTTPS proxies from a site you trust, that way the proxies used are reliable.
If you don't know anywhere you can purchase HTTPS proxies, you can from https://proxy.webshare.io for reliable and fast proxies.

## Future Plans
- Additional Social Medias
- Faster Checks

## Credits and Mentions
[Proxy handler](https://github.com/landoncrabtree/social-checker/blob/master/proxy.py)
