import requests, json
def dl(imgURL, imgname):
    global exists
    global retry
    paths = imgname
    try:
        print(imgURL)
        response = requests.get(imgURL)
        file = open(paths, "wb")
        file.write(response.content)
        file.close()
    except:
        print("Il y a eu une erreur !")
        global errors
        errors += 1

id = str(input("Track ID: "))

url = "https://api.spotify.com/v1/tracks/" + id
querystring = {"market":"FR"}
headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'authorization': "Bearer BQCk9c43oIUR53aL5oFExZ3OutnF_PZFYMt1f-szD77MqocR7AbklYQIpMQ4x_vt6A8HSsvrzWPLoE_4nwJeq4JMdi3728EN_ISPkM5vgmw1pyaugPZBmiT__3seyKX2xvlmiM12sM68NYyQPTpAcNGBfoo4A0I8nznX2BSW"
    }

Resp = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)

dl(Resp["album"]["images"][0]["url"], Resp["album"]["name"] + ".jpg")