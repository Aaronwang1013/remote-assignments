def avg(data):
    product = data["products"]
    sum = 0
    for i in range(len(product)):
        sum += product[i]["price"]
    return round(sum / len(product), 3)

# your code here


print(avg({
    "products": [
        {
            "name": "Product 1",
            "price": 100},
        {
            "name": "Product 2",
            "price": 700},
        {
            "name": "Porduct 3",
            "price": 300}
    ]})
)
