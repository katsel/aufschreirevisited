# #aufschrei revisited

## Analysing #aufschrei with Python

### Requirements

* Python 3.0 or higher with all neccessary packages installed (python3-tk, ...)
* MongoDB (or enabled port-forwarding to an existing MongoDB instance)

### Set-up

* Either:
  * import the tweets to your local MongoDB instance using `tweets2db.py`
  * OR: open a an ssh port-forwarding connection in a separate command line window
```
ssh -L 27017:localhost:27017 username@server
```
* start the iPython notebook by running
    `ipython3 notebook`

* save the notebook when done and stop the notebook server
* close the ssh connection by typing `exit`
