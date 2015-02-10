# #aufschrei revisited

## Analysing #aufschrei with Python

### Requirements

* Python 3.0 or higher with all neccessary packages installed (...)
* MongoDB (or enabled port-forwarding to an existing MongoDB instance)

### Set-up

* Either:
  * import the tweets to your local MongoDB instance using `tweets2db.py`
  * OR: open an ssh port-forwarding connection
```
ssh -L 27017:localhost:27017 username@X.X.X.X
```
* start the iPython notebook by running
    `ipython3 notebook`
