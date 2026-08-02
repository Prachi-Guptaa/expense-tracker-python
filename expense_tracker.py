from expense import Expense
from datetime import datetime
from datetime import date
import calendar

today = date.today()

# Total days in current month
days_in_month = calendar.monthrange(today.year, today.month)[1]

remaining_days = (days_in_month - today.day)



today = datetime.now()
day = today.day


def main():

  print("expense tracker is running")
  budget=2000
  expense_file="expense.csv"
    
# get input
  expense=get_userExpense()
  print(expense)

# store it
  save_expenseToFile(expense,expense_file)
   
# read and summerize
  summerize_expense(expense_file,budget)


 
def save_expenseToFile(expense:Expense,expense_file):
  with open(expense_file,"a") as f:
      f.write(f"{expense.name},{expense.category},{expense.amount}\n")
   
def summerize_expense(expense_file,budget):
   expenses: list[Expense]=[]
   with open(expense_file,"r") as f:
     lines=f.readlines()
     for i,line in enumerate(lines): 
       stripped_line=line.strip()
       expense_name,expense_category,expense_amount =stripped_line.split(",")
       print(f"{i+1}- {expense_name}, {expense_category},{expense_amount}")
       line_expense=Expense(name=expense_name,category=expense_category,amount=float(expense_amount))
       
       expenses.append(line_expense)
     
     amount_by_category={}
     for expense in expenses:
       key=expense.category
       if key in amount_by_category:
         amount_by_category[key]+= expense.amount
       else:
         amount_by_category[key]= expense.amount


     print("Expense_by_category")
     for key,amount in amount_by_category.items():
       print(f"{key}: Rs.{amount:.2f}")

     total_spent=sum(x.amount for x in expenses)
     print(f"\nYou have spent- Rs.{total_spent:.2f} this month\n")

     remaining_budget=budget-total_spent
     print(f"Budget remaining - Rs.{remaining_budget:.2f} this month\n")
     daily_budget=remaining_budget/remaining_days
     print(f"Budget per day-Rs.{daily_budget}")

         


   
def get_userExpense():

 expense_name =input("Enter expense name: ")
 expense_amount =float(input("Enter expense amount: "))
 expense_categories =["Home","Food","Fun","Work","Miscellaneous"]
 while True:
    print("Select a category:")
    for i, category_name in enumerate(expense_categories):
     print(f"{i+1},{category_name}")
    value_range=f"(1-{len(expense_categories)})"
    selected_index=int(input(f"Enter a category number {value_range}: "))-1
    if selected_index in range(len(expense_categories)):
      selected_category=expense_categories[selected_index]
      new_expense=Expense(name=expense_name,category=selected_category,amount=expense_amount)
      return new_expense
    else:
      print("Invalid category, Please try again!")




  


if __name__=="__main__":
 main()

