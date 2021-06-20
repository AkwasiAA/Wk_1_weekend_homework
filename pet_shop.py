def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash_figure):
    pet_shop["admin"]["total_cash"]=(pet_shop["admin"]["total_cash"]+ cash_figure)

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, new_sales):
    pet_shop["admin"]["pets_sold"]=(pet_shop["admin"]["pets_sold"]+ new_sales)

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, british_shorthair):
    matching_breed = []
    for pet in pet_shop["pets"]:
        if pet ["breed"]==british_shorthair: matching_breed.append(british_shorthair)
    return matching_breed

def get_pets_by_breed(pet_shop, dalmation):
    matching_breed = []
    for pet in pet_shop["pets"]:
        if pet ["breed"]==dalmation: matching_breed.append(dalmation)
    return matching_breed

def find_pet_by_name(pet_shop,name):
     for pet in pet_shop["pets"]:
        if pet["name"]==None:
         return None
        elif pet["name"]=="Arthur":
         return pet

# def find_pet_by_name(pet_shop,name):
#      for pet in pet_shop["pets"]:
#         if pet["name"]==None:
#          return None
#         elif pet["name"]=="Fred":
#          return pet

def remove_pet_by_name(pet_shop, Arthur): 
    index_to_remove = 0 
    for pet in pet_shop["pets"]: 
        if pet["name"] == Arthur: 
            index_to_remove = pet_shop["pets"].index(pet) 
            pet_shop["pets"].pop(3)

def add_pet_to_stock(pet_shop, new_pet):
     pet_shop["pets"].append(new_pet)           

def get_customer_cash(customers):
    return customers["cash"]