import requests

response = requests.get('https://www.manuscriptlink.com/society/khc/conference/whc/proceedings2')

body = response.text
lines = body.split("\n")
with open("links.txt", "w") as f:
    for line in lines:
        if "<a href" in line:
            tokens = line.split("'")
            if "pdf-paper" in tokens:
                f.write(tokens[3]+"\n")
