import requests
from bs4 import BeautifulSoup as bs

pagesToUpload = input("How many pages do you want to upload?: ")


def uploadPages(pagesToUpload):
    global page
    page = 1
    noteBooksList = []
    while page <= int(pagesToUpload):
        r = requests.get("https://nout.am/am/notebook.html?p=" + str(page))
        html = bs(r.content, "html.parser")

        noteBooks = html.select(".products > .product-item")
        if len(noteBooks):
            for el in noteBooks:
                # noteBooksList = str(num)
                title = el.select(".product-item-details > strong > .product-item-link")
                noteBooksList.append(title[0].text[1:-1])
            page += 1
        else:
            break
    return noteBooksList


uploaded_pages = uploadPages(pagesToUpload)
for i, j in enumerate(uploaded_pages):
    print(f"{i + 1}. {j}")

getNum = input("Write the number of notebook you liked to know price: ")


def getPrice(n):
    global page
    k = 1
    priceList = []

    while k <= int(pagesToUpload):
        r = requests.get("https://nout.am/am/notebook.html?p=" + str(k))
        html = bs(r.content, "html.parser")

        noteBooks = html.select(".products > .product-item")
        if len(noteBooks):
            for el in noteBooks:
                # noteBooksList = str(num)
                price = el.select(".price")
                priceList.append(price[0].text[0:-4])
            k += 1
        else:
            break

    return priceList[n]


print("You chose: " + uploadPages(pagesToUpload)[int(getNum) - 1])

print("Price: " + getPrice(int(getNum) - 1) + " AMD")
