import os

inp = str(raw_input("Do you want to delete this program? "))

if inp.lower() == "yes" or inp.lower() == "y":
    if os.path.exists("main.py"):
        print("cya <o/")
        os.remove("main.py")
    else:
        print("doesn't exist.")
else:
    print("oh. ok. guess i live another day.")

