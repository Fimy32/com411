#Nested IF demo
book_type = input("What cover type does the book have (soft or hard)?")

if book_type == "soft":
    yes_no = input("Is the book perfect bound (yes or no)?")
    if (yes_no == "yes"):
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
if book_type == "hard":
    print("Books with hard covers can be more expensive!")