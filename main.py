class store:
  def _init_(self, name, items, price, quantity):
    self.name = "StockX"
  def __init__ (self)
    self.items = ["Seafoam Retro Jordan 1" , "Wmns Dunk Low 'Sunrise Pulse'"," Chuck 70 High 'Obsidian'"]
    self.price = [271.50, 110, 75]
    self.quantity = [150, 52, 160 ]
    self.mycart()

  def welcome(self):
    print("Welcome to" +self.name+"\n"+self.tagline)
    working = True
    while working:
      self.mycart.totalitems()
      action = input("\ns=shop\nv=view cart\nr=remove item from cart\nc=checkout\nx=exit\nWhat do you want to do?")
      if action == "s":
        self.shopping()
      elif action == "v":
        self.mycart.viewing()
      elif action == "r":
        self.restock()
      elif action == "c":
        print("checkout")
      elif action == "x":
        print("exit")
        working = False
      else:
        print("I am sorry, I do not understand, please try again.")
    self.closestore()

  def shopping(self):
    self.listitems()
    index,amount = self.findit()
    self.mycart.additem(self.items[index],amount,self.prices[index])
    print("added"+str(amount)+""+self.items[index])
    self.amounts[index]-=amoumt
    if self.amounts[index] ==0:
      del self.items[index]
      del self.prices[index]
      del self.amounts[index]

  def restock(self):
    self.mycart.viewing()

    
