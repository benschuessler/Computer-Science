import random
ds = ["local", "roasted", "grilled", "garlic mashed", "oven dried", "spiced", "stewed", "assorted", "iced", "sliced", "braised", "free-range", "baby" "teriyaki glazed", "steamed"]
main = ["cauliflower", "tilapia fillet", "pork loin", "green beans", "basmati rice", "rainbox carrots", "fingerling potatoes", "three color squash", "potatoes", "eggplant", "drumstick", "short rib", "duck breast", "eye round of beef", "baguette"]
add = ["with fennel","gratin","bengali style", "with peas","pizza","with balsamico","with garlic and olive oil","with pigeon peas","with minted yogurt","soup","chutney","salad","with tropical fruit salad","with troptical fruit salsa","over sticky rice","au jus"]
prices = []
while True:
    mode = input("What would you like to do? 1: random combination of items, 2: pick specific meal, 3: exit")

    if mode == "3":
        break
    elif mode == "1":
        items=input("how many menu items would you like")
        y=0
        
        #check if items is an integer
        while y < int(items):
            print(random.choice(ds),random.choice(main),random.choice(add))
            y+=1
    elif mode == "2":
        items=input("how many meals would you like")

        for i in range(int(items)):
            d = input("Which descriptor would you like? ")
            m = input("Which main would you like? ")
            a = input("Which add on would you like? ")
            print(d + m + a)
    else:
        print("Invalid")


