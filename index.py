from appliances import DishWasher
from appliances import Refrigerator
from appliances import CanOpener
from appliances import CoffeeMaker
from appliances import Stove
from appliances import Dryer
from appliances import Washer

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

open_canner = CanOpener("black")
open_canner.open_can()