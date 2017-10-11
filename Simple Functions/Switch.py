# Say you had a list of numbers and you wanted to return the string equivalent. You could do this by building a dict:

def switch_it_up(number):
    number_converter={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
    return number_converter[number]
 
# or:

def switch_it_up(number):
  return {
    0:"Zero",
    1:"One",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"Five",
    6:"Six",
    7:"Seven",
    8:"Eight",
    9:"Nine"
 }[number]
 
 # or you can call .get on the dict:
 
 def switch_it_up(number):
    dict = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    0: "Zero"}
    
    return dict.get(number)
    
 # or in this case you can just use a list:
 
 def switch_it_up(n):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]
    
 # or:
 
 def switch_it_up(number):
    #your code here
    d = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return d[number].capitalize()
