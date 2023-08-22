import math


class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def __repr__(self):
    heading = self.category.center(30, "*")
    funds = ""
    for acc in self.ledger:
      funds += "{:<23} {:<.2f}\n".format(acc["description"][:23], float(str(acc["amount"])[:7]))
    total_statement = heading + "\n" + funds+"Total: "+ str(Category.get_balance(self))
    return total_statement

  def deposit(self, amount, description=""):
    acc = {"amount": amount, "description": description}
    self.ledger.append(acc)

  def check_funds(self, amount):
    check = amount <= Category.get_balance(self)
    if check:
      return True
    return False

  def withdraw(self, amount, description=""):
    status = Category.check_funds(self, amount)
    if status:
      acc = {"amount": -amount, "description": description}
      self.ledger.append(acc)
    return status

  def transfer(self, amount, transfer_category):
    status = Category.check_funds(self, amount)
    if status:
      acc = {
        "amount": -amount,
        "description": f"Transfer to {transfer_category.category}"
      }
      self.ledger.append(acc)
      new_acc = {
        "amount": amount,
        "description": f"Transfer from {self.category}"
      }
      transfer_category.ledger.append(new_acc)
    return status

  def get_balance(self):
    total_balance = 0
    for acc in self.ledger:
      total_balance += acc["amount"]
    return total_balance

def round_to_nearest_tenth(number):
  rounded_number = round(number / 10) * 10
  return int(rounded_number)
  
def get_percentage_spent(categories):
    total_spent_dict=dict()
    total = 0 
    for category in categories:
      total_spent_categorywise=0
      for acc in category.ledger:
        amount=acc["amount"]
        if amount<0:
          total_spent_categorywise+=math.fabs(amount)
        total+=total_spent_categorywise
        total_spent_dict[category.category]=total_spent_categorywise
    for key,value in total_spent_dict.items():
        total_spent_dict[key]=round_to_nearest_tenth((value/total)*100)
    return total_spent_dict

def create_spend_chart(categories):
  chart_string="Percentage spent by category\n"
  total_spent_dict = get_percentage_spent(categories)
  chart_dict={}
  for percentage_num in range(100,-10,-10):
    chart_dict[percentage_num]=list() 
    for value in total_spent_dict.values():
       if percentage_num<=value:
         chart_dict[percentage_num].append("o")
       else:
         chart_dict[percentage_num].append(" ")
  for key,value in chart_dict.items():
    chart_string+="{:>3}| {:<7}  \n".format(key,"  ".join(value).strip('[]'))
  chart_string+="    "+"-"*10
  category_dict={}
  count=0
  category_names=[category.category for category in categories]
  max_length = len(sorted(category_names,key=len,reverse=True)[0])
  while True:
    category_dict[count]=list()
    for category in category_names:
      if count<len(category):
        category_dict[count].append(category[count])
      else:
        category_dict[count].append(" ")
    count+=1
    if count>max_length:
      break
  count=0
  for value in category_dict.values():
    if count<=max_length-1:
      chart_string+="\n     {}  ".format("  ".join(value).strip('[]'))  
      count+=1
  return chart_string
  