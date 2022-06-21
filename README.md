# invisifox-python
Python 3 package for easy integration with the API of invisifox captcha solving service.

## Installation
This package can be installed with Pip:

```pip install invisifox```


Sample code:

To create invisifox instance 

```python 
from invisifox import InvisiFox

invisifoxSolver = InvisiFox(apiKey='YOUR API KEY')
```

To get hcaptcha solution


```python 
solution = invisifoxSolver.solveHCaptcha(sitekey='4c672d35-12342-42b2-88c3-78380b012345',
                                                pageurl='https://domain',
                                                proxy='username:password@ipaddress:port'

```
