class Cart():
 

    
    def __init__(self,handles,ammount,items):
        self.handles = handles
        self.ammount = ammount
        self.items = items
        

    def showcart(self):
        print("The items in your cart")
        for item in self.items:
            print(item)

    def showAmmount(self):
        print(f'Your ammount of items in your cart is: {self.capacity}')
        
    
    def addToCart(self):
        products = input('What would you like to attach? ')
        self.items.append(products)
        
    
    def changeCartAmmount(self, ammount):
        self.ammount = ammount
        
    
    def increaseAmmount(self, changed_ammount = 20):
        if self.ammount == isinstance(self.ammount, str):
            print("Hopefully we can do this.")
        else:
            self.ammount += changed_ammount

safeway_bag = Cart(2,20,[])



def fun():
    while True:
        response = input('What do you want to do? attach/show/ or remove')
        
        if response.lower() == 'remove':
            safeway_bag.showCart()
        print('Thanks for shopping')
        
        if response.lower() == 'attach':
            safeway_bag.Cart()
            
        if response.lower() == 'show':
            safeway_bag.Cart()
        break    

fun()