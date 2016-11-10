import json,urllib
data = urllib.urlopen("http://www.shopicruit.myshopify.com/products.json").read()
d = json.loads(data)
print (type(d["products"])) #list
print(d["products"])

for i in range(len(d["products"])):
    if d["products"][i]["product_type"] == "Clock" or d["products"][i]["product_type"] == "Watches":
        print(d["products"][i]["price"])

#Getting shit done requires solid time management, so you've decided you need to stock up on clocks and watches. You head to your favourite Shopify store 'Shopicruit', which sells all kinds of wacky products. Write a program that calculates how much it will cost you to buy all the clocks and watches in the store.

#Attach your answer (in dollars), as well as your program (any language) below. You can find the endpoint for Shopicruit's products at: shopicruit.myshopify.com/products.json?page=1 (Keep in mind there are multiple pages of results).
