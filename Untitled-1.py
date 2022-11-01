#%%
print("Hello world")



# %%

is_male = False
is_hairy = True

if is_male:
    print("You are a man")
if is_male and is_hairy:
    print("you're a hairy man")
if not(is_male) and (is_hairy):
    print("you're a hairy female, respectfully")
elif not(is_male) and not(is_hairy):
    print("you a female")
# %%

# %%


def max_num(num1, num2, num3):
    if num1 >= num2 & num1 >= num3:
        return num1
    elif num2 >=1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(-1,4,9))
# %%
num1 = float(input("Enter first nubmer: "))
op = (input("Enter operator: "))
num2 = (float(input("Enter second nubmer: ")))

if op == "+":
    print (num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid operator")

# %%

print("So That Was Your Calculator Experience")
