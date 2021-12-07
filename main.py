from urllib.request import urlopen
from bs4 import BeautifulSoup
from PIL import Image
import requests

url = requests.get(input("Enter url: "))

if url.status_code == 200:
    soup = BeautifulSoup(url.content, "lxml")

    title = "".join(list(map(lambda x: "_" if x in "\/," else x, (soup.find("span",
                    attrs={"class": "j-title-breadcrumb"}).text).strip()+".pdf")))
    imgs = soup.findAll("img", attrs={"class": "slide_image"})

    for i in range(len(imgs)):
        imgs[i] = Image.open(requests.get(
            imgs[i]["data-full"], stream=True).raw)

    imgs[0].save(title, save_all=True, append_images=imgs[1:])

    print("Your file has been saved successfully ✔️")
elif url.status_code == 404:
    print("Please enter a valid url")
else:
    print("Sorry , some error occured 😐")
