#Task 1: Code Correction You are provided with a Python script that is supposed to help in event planning, 
# but it has errors. Identify and fix them.
# Task 2 further enhance your code  asking for additional things like "audio system"
#or "projector" based on number of attendees 
# Task 3 ask if want "vegetarian" food recommend "Veggie Delight Caterers" otherwise
# recommend "Gorumet Meals Caterer"



attendees = input("Enter number of attendees: ")
venue = "large hall" if attendees > 100 else "conference room"
print(venue)