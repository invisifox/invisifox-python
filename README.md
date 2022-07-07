# invisiFox Python API

Welcome to the invisiFox Python API!
[Node.js API](--NODE API LINK HERE--) | [Rest API](https://docs.invisifox.com/rest-api)

In order to use the invisiFox API you will need an API key. You can get your API key by creating an account and adding credit on [invisifox.com](https://invisifox.com).

## Installation

To install the Python API and get started you can simply pip install invisiFox into your project.

```sh
$ pip install invisiFox
```

## HCaptcha Solver

When making a request must pass a number of paramaters. Some key paramters are required and others are not. The list below details the available paramaters. Those marked optional are not required, all the others are required.


**token:** your invisifox api token

**siteKey:** the HCaptcha sitekey from the website you are using. This is usually found in HTTP requests or in the HCaptcha iFrame
**pageurl:** the url on which you find the HCaptcha. Usually the full url is not required, for example all the url parameters may not be necassary
**proxy:** the proxy address you want to use to solve the HCaptcha in format username:password@host:port or host:port
**rqdata (optional):** for enterprise HCaptcha websites, this value is usually found in HTTP requests.
**useragent (optional):** the useragent of the device you are using or emulating
**cookies (optional):** the browser cookies
**invisible (optional):** default set to false, set to true for invisible HCaptchas

Solving a HCaptcha usually takes 25 to 120 seconds depending on network traffic so please be patient. You will be automatically charged for each request from your balance at a rate of US$ 0.6 / 1000 Captcha Solutions.

```python
from invisiFox import invisiFox

bot = invisiFox()
bot.apiKey = 'YOUR API KEY'

solution = bot.solveHCaptcha('b2b02ab5-7dae-4d6f-830e-7b55634c888b','https://discord.com','http://username:password@host:port')
print(solution)
```

## Residential Proxy

In order to use invisiFox proxies you will need your proxy authentication username and password. You can get these two values by creating an account and adding credit on [invisifox.com](https://invisifox.com) proxies.

invisiFox proxies are designed to be dynamically generated and customizable on the go. The documentation below describes how to generate a proxies.

**Random Rotation**

Random rotation proxies are proxies that are randomized on each request. This is usefull for use cases where you are requesting a resource that is rate limited but does not maintain a session based on your IP address. For example this is useful for anonymous data scraping, but no ideal for a case where an account is logged in and must make successive requests from the same IP address. In the later case, Stick IPs are more suitable

**Sticky Proxies**

Sticky IP proxies are designed to be easy to dynamically generate, as well as to maintain a fixed IP session based on a string. In addition we use high level request databasing to reduce instances of IP reuse / collision. Simple put unlike other providers on the market we try to make sure the proxy we provide has not recently been used by you or someone else on the host / website you are accessing. Effectively we substantially increase success rates and reduce the change of being detected on highly sensitive application.

**Generating Proxies**

You can easily generate proxies using our API. You can pass none, any, or all of the following paramaters.

**country (optional):** the country where you want the proxy from. Defaults to random country.
**proxyType (optional):** the type of proxy between "random" and "sticky". Defaults to "random".
**protocol (optional):** the type of proxy between "http" and "https". Defaults to "http".
**count (optional):** the number of proxies to be returned in an array. Defaults to 1.

```python
from invisiFox import invisiFox

bot = invisiFox()
bot.proxyUsername = 'username'
bot.proxyPassword = 'password'

x = bot.makeProxy(country=bot.proxyCountriesList[1],proxyType='sticky',protocol='https',count=5)
print(x)
```

## Technical Difficulties

If you are experiencing techincal difficulties please contact [support@100fire.com](mailto:support@100fire.com). We will do our best to reply in a timely fashion.

