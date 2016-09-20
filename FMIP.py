import datetime, requests, time, base64, urllib2, json

def FMIP(username, password):
    i = 0
    while True:
        i +=1
        url = 'https://p04-fmipmobile.icloud.com/fmipservice/device/%s/initClient' % username
        headers = {
            'Accept': '*/*', #we need this header for ulib2
            'Authorization': 'Basic %s' % base64.b64encode("%s:%s" % (username, password)),
            'Content-Type': 'application/json; charset=utf-8',
            'X-Apple-Find-API-Ver': '3.0',
            'X-Apple-AuthScheme': 'Forever',
            'User-Agent': 'FindMyiPhone/500 CFNetwork/758.4.3 Darwin/15.5.0',
        }
        request = urllib2.Request(url, None, headers)
        request.get_method = lambda: "POST"
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            if e.code != 200 or e.code != 401:
                return "HTTP Error: %s" % e.code
            if e.code == 401:
                return "Auth Error"
            else:
                raise HTTPError
        z = json.loads(response.read())
        if i == 2: 
            break
        print "Sent \033[92mlocation\033[0m beacon to \033[91m[%s]\033[0m devices" % len(z["content"])
        print "Awaiting response from iCloud..."
        #okay, FMD request has been sent, now lets wait a bit for iCloud to get results, and then do again, and then break
        time.sleep(5)
    returnString = ""
    returnString += "\033[94m(%s %s | %s)\033[0m -> \033[92mFound %s Devices\033[0m\n-------\n" % (z["userInfo"]["firstName"], z["userInfo"]["lastName"], username, len(z["content"]))
    i = 1
    for y in z["content"]:
        try:
            returnString += "Device [%s]\n" % i
            i += 1
            returnString += "Model: %s\n" % y["deviceDisplayName"]
            returnString += "Name: %s\n" % y["name"]
            timeStamp = y["location"]["timeStamp"] / 1000
            timeNow = time.time()
            timeDelta = timeNow - timeStamp #time difference in seconds
            minutes, seconds = divmod(timeDelta, 60) #great function, saves annoying maths
            hours, minutes = divmod(minutes, 60)
            timeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime("%A, %B %d at %I:%M:%S")
            if hours > 0:
                timeStamp = "%s (%sh %sm %ss ago)" % (timeStamp, str(hours).split(".")[0], str(minutes).split(".")[0], str(seconds).split(".")[0])
            else:
                timeStamp = "%s (%sm %ss ago)" % (timeStamp, str(minutes).split(".")[0], str(seconds).split(".")[0])
            returnString += "Latitude, Longitude: <%s;%s>\n" % (y["location"]["latitude"], y["location"]["longitude"])
            returnString += "Battery: %s & %s\n" % (y["batteryLevel"], y["batteryStatus"])
            returnString += "\033[92mLocated at: %s\033[0m\n" % timeStamp
            returnString += "-------\n"
        except TypeError,e :
            returnString += "\033[92mCould not get GPS lock!\033[0m\n"
    return returnString

username = raw_input("Apple ID: ")
password = raw_input("Password: ")
print FMIP(username, password),
