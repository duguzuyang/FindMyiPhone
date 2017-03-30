# FindMyiPhone
Locates all devices associated with an iCloud account. No user notification, pretty, pure python, quick, fast, accurate. Works for any account, including ones with 2SV/2FA. This program will also work with a FMIP token that is extracted from the FindMyiPhone App on the iPhone, and can also play a sound on the located device(s).

# Usage 

***python FMIP.py***

```
INPUT: Apple ID 

INPUT: Password
```
```
OUTPUT:
Successfully authenticated

Sent location beacon to [3] devices
Awaiting response from iCloud...
Reprocessing iCloud response...

Awaiting response from iCloud...
(John Doe | 1234567[DSID]) -> Found 3 Devices
```
```
Device [1]

Model: MacBook Pro 13"
Name: John's MacBook Pro

Latitude, Longitude: <22.000000000;-22.000000000>
Street Address: 123 Mill Road, NY, NY 10001, USA

Battery: 88% & Charging

Located at: Monday, September 19 at 11:51:44 (0m 5s ago)
```
```
Device [2]

Model: iPhone 5s
Name: John's iPhone

Latitude, Longitude: <22.000000000;-22.000000000>
Street Address: 123 Mill Road, NY, NY 10001, USA

Battery: 88% & Charging

Located at: Monday, September 19 at 11:51:45 (0m 4s ago)

```
```
Device [3]

Model: MacBook Pro 15"
Name: John's MacBook Pro

Latitude, Longitude: <22.000000000;-22.000000000>
Street Address: 123 Mill Road, NY, NY 10001, USA

Battery: 88% & Charging

Located at: Monday, September 19 at 11:51:44 (0m 5s ago)
```

```
Would you like to play a sound? (Y/n): y
-------
Device [1] - [John's MacBook Pro | MacBook Pro 13"]
Device [2] - [John's iPhone | iPhone 5s]
Device [3] - [John's MacBook Pro | MacBook Pro 15"]
-------
Which above device should you like to play a sound for?
WARNING, this will send the iCloud user an email.

Enter a device number [1-3]: 2
Enter a message to be displayed: Greetings

Successfully played sound on [John's iPhone | iPhone 5s]
```
