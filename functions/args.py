def my_country(country = "Rwanda"):
  print(f"Hello from {country}")


    
# def greet(*names):
#     for name in names:
#     print("Hello {name}"):

def students_attributes(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

# A function named concatenate_args that takes any number of string arguments
#  in positional arguments format and concatenates them into a single string
def concatenate_args(*students):
    result = ""
    for student in students:
        result += student
    return result
# A function named concatenate_kwargs that takes any number of string arguments
#  in keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    return "".join(kwargs.values())
    result = concatenate_kwargs(arg1="Knitting", arg2="Crafts", arg3="pottery")
print(result)

