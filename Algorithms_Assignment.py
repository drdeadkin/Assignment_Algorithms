
def split_into_arrays(id_id, name, price, category):
    r = open("product_data.txt", "r")
    for line in r:
        parts = line.strip().split(",")
        id_id.append(parts[0])
        name.append(parts[1])
        price.append(parts[2])
        category.append(parts[3])
    id_id = [l.strip() for l in id_id]
    name = [i.strip() for i in name]
    price = [n.strip() for n in price]
    category = [z.strip() for z in category]
    return id_id, name, price, category


def insert(id_id, name, price, category):
    insert1 = input("Enter Id, Name, Price, and Category seperated by a comma: ")
    append1 = insert1.strip().split(",")
    id_id.append(append1[0])
    name.append(append1[1])
    price.append(append1[2])
    category.append(append1[3])


def update(id_id, name, price, category):
    modify1 = input("Enter Product ID to Modify: ")
    if modify1 in id_id:
        Index1 = id_id.index(modify1)
        modify2 = input("Enter if you want to edit Name(n), price(p) or Category(c): ").lower()
        if modify2 == "n":
                modify3 = input("Enter New modification: ")
                name[Index1] = modify3
        if modify2 == "p":
                modify4 = input("Enter New modification: ")
                price[Index1] = modify4
        if modify2 == "c":
                modify5 = input("Enter New modification: ")
                category[Index1] = modify5
    else:
        print("Product ID not found.")


def delete(id_id, name, price, category):
    modify1 = input("Enter Product ID to Delete: ")
    if modify1 in id_id:
        Index1 = id_id.index(modify1)
        id_id.pop(Index1)
        name.pop(Index1)
        price.pop(Index1)
        category.pop(Index1)
    else:
        print("Product ID not found.")


def search(id_id, name, price, category):
    modify1 = input("Enter ID, name, price or category: ")
    if modify1 in id_id:
        Index1 = id_id.index(modify1)
        print(id_id[Index1], name[Index1], price[Index1], category[Index1])
    elif modify1 in name:
        Index2 = name.index(modify1)
        print(id_id[Index2], name[Index2], price[Index2], category[Index2])
    elif modify1 in price:
        Index3 = price.index(modify1)
        print(id_id[Index3], name[Index3], price[Index3], category[Index3])
    else:
        print("Id, Name, Price or Category not found")

def bubble_sort(id_id, name, price, category):
    n = len(price)
    for i in range(n):
        for j in range(0, n - i - 1):
            if price[j] > price[j + 1]:
                price[j], price[j + 1] = price[j + 1], price[j]
                id_id[j], id_id[j + 1] = id_id[j + 1], id_id[j]
                name[j], name[j + 1] = name[j + 1], name[j]
                category[j], category[j + 1] = category[j + 1], category[j]

def main():
   id_1 = []
   name1 = []
   price = []
   category = []
   id_1, name1, price, category = split_into_arrays(id_1, name1, price, category)
   break1 = str
   while break1 != "exit":
       break1 = input("Do you want to bubble sort(b), Search(s), Delete(d), update(u), Insert(i), print(p) or exit: ").lower()
       if break1 == "b":
           bubble_sort(id_1, name1, price, category)
       elif break1 == "s":
           search(id_1, name1, price, category)
       elif break1 == "d":
           delete(id_1, name1, price, category)
       elif break1 == "u":
           update(id_1, name1, price, category)
       elif break1 == "i":
           insert(id_1, name1, price, category)
       elif break1 == "p":
           print("Product IDS: ", id_1)
           print("Product Names: ", name1)
           print("Prices:", price)
           print("Categorys:", category)


if __name__ == '__main__':
    main()
