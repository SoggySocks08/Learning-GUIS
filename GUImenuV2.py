import os, time
clear = 'cls' if os.name == 'nt' else 'clear'
os.system(clear)
from tkinter import *

class App:
  # ===================
  # Constructor
  # ===================
  def __init__(self, root):
    self.root = root
    self.order=[]
    self.cust_Ords = {}
    self.menu_dict = {"chicken sandwich": 5,
            "spicy sandwich": 8,
            "fries": 5,
            "da bev": 4,
            "salad": 4,
            "shake":5}
           
    self.inventory_dict = {"chicken sandwich": 5,
             "spicy sandwich": 5,
             "fries": 5,
             "da bev": 5,
             "salad": 5,
             "shake": 5}
   
    self.restocks_dict = {"chicken sandwich": 0,
             "spicy sandwich": 0,
             "fries": 0,
             "da bev": 0,
             "salad": 0,
             "shake": 0}
    
    self.letterBank=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    self.setup_window()
    self.create_widgets()
  # ===================
  # Setup Methods
  # ===================
  def setup_window(self):
    self.root.title("Chick-Fil-A")
    self.root.geometry('750x750')
 
  def create_widgets(self):

    self.create_frames()

    self.create_frame1_buttons()
    self.create_frame1_labels()

    self.create_frame2_buttons()
    self.create_frame2_labels()
    self.create_frame2_entry()
   
    self.create_frame3_buttons()

    self.frame2.grid_remove()
    self.frame3.grid_remove()

  def create_frames(self):
    # frame1 for main order page
    self.frame1 = Frame(self.root)
    self.frame1.grid(row=0,column=0)

    # frame2 for name entry
    self.frame2 = Frame(self.root)
    self.frame2.grid(row=0,column=0)
   
    #frame3 for either continuing the order
    self.frame3 = Frame(self.root)
    self.frame2.grid(row=0,column=0)

 # First order screen
  
  def create_frame1_buttons(self):
    # dictionary contains all button objects corresponding to each menu item
    items = ["Chicken Sandwich", "Spicy Sandwich", "Fries", "Salad", "Da Bev","Shake"]
    # r = rows, c = columns. Used to place the buttons in the correct place on grid in for loop below
    r = 0
    c = 0
    # for loop creates all menu buttons automatically, 3 per column
    for item in items:
      btn = Button(self.frame1,
                   text=f"{item}: ${self.menu_dict[item.lower()]}",
                   width=20,
                   command=lambda item=item: self.add2Order(item))
      btn.grid(row=r,column=c, sticky=W)
      if r == 2:
        c +=1
        r=0
        continue
      r+=1

    # Submit button (seperate from menu item buttons)
    self.submit=Button(self.frame1,
                       text="Submit",
                       width=20,
                       height=2,
                       command=lambda: self.submitFunc()
    )
    self.submit.grid(row=4,column=0, pady=25, sticky=W)
 
  def create_frame1_labels(self):
    # display's order as user is building it
     self.order_text = '\n'.join(self.order)
     self.orderLbl = Label(self.frame1,
                     text=f"Order{self.order}")
     self.orderLbl.grid(row=6,column=0)

 # Name entry screen
  def create_frame2_buttons(self):
    #Enters the user's name for order
    cnfrm = Button(self.frame2,
                   text="Confirm",
                   width=15,
                   command=self.cnfrmFunc
    )
    cnfrm.grid(row=1,column=0, pady=10, sticky=W)

  def create_frame2_labels(self):
    label = Label(self.frame2,
                  text="Please Enter a name for the order:")
    label.grid(row=0,column=0)

  def create_frame2_entry(self):
    self.nameInput = Entry(self.frame2,
                      width=20,
                      bd=5,
                      relief=RAISED)
    self.nameInput.grid(row=0,column=2)
   
 # Order confirmation screen
  def create_frame3_buttons(self):
      b2Obtn = Button(self.frame3,
                      text="Place another order",
                      width=15,
                      command=self.b2O)
      b2Obtn.grid(row=0,column=0, sticky=W)

      endOrder = Button(self.frame3,
                        text="End Order",
                        width=15,
                        command=self.endOrder
                        )
      endOrder.grid(row=1,column=0, sticky=W)
   
 # ===================
 # Event Handling
 # ===================

  def submitFunc(self):
    self.frame1.grid_remove()
    self.frame2.grid()

  def add2Order(self, item):
    self.order.append(item)
    self.order_text='\n'.join(self.order)
    self.orderLbl.config(text=f"Order:\n{self.order_text}")

  def getName(self):
    name=self.nameInput.get()
    return(name)

  def cnfrmFunc(self):
    name = self.nameInput.get()
                
            
    self.cust_Ords[self.getName().capitalize()]=self.order
    self.order=[]

    self.frame2.grid_remove()
    self.nameInput.delete(0, END)
    self.orderLbl.config(text=f"Order: {self.order}")
    self.frame3.grid()

  def endOrder(self):
     self.root.destroy()
     print(self.cust_Ords)
     self.inv_func()
     self.display_totals()
     self.display_rev()
     
  def b2O(self):
      self.frame3.grid_remove()
      self.frame1.grid()
     
 # ===================
 # Logic
 # ===================

  def calc_totals(self):
    totals = {}
    for name, order in self.cust_Ords.items():
        cost = 0
        for item in order:
            cost += self.menu_dict[item.lower()]
        totals[name] = cost
    return(totals)
 
  def calc_rev(self):
      revenue = 0
      for name, total in self.calc_totals().items():
          revenue += total
      for item, restocks in self.restocks_dict.items():
          for i in range (restocks):
              revenue -= (self.menu_dict[item.lower()] - 3) * 5
      return(revenue)

  def inv_func(self):
      for name, order in self.cust_Ords.items():
          for item in order:
              if self.inventory_dict[item.lower()] > 0:
                  self.inventory_dict[item.lower()] -= 1
              else:
                  self.inventory_dict[item.lower()] = 4
                  self.restocks_dict[item.lower()] += 1
      print("\nInventory:")
      for item, count in self.inventory_dict.items():
          print(f"{item}: {count}")
      print("\nRestocks:")
      for item, restocks in self.restocks_dict.items():
          print(f"{item}: {restocks}")

  def display_ords(self):
      for name, order in self.cust_Ords.items():
          print(f"{name}'s order: {order}")

  def display_totals(self):
    print()
    for name, total in (self.calc_totals().items()):
        print(f"{name}'s total: ${total}")

  def display_rev(self):
    print(f"\nDaily revenue: ${self.calc_rev()}\n")

pos = Tk()
gui = App(pos)
pos.mainloop()
