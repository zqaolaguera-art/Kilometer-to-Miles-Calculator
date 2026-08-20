# Assign variables and distance in kilometers from user
distance_km1 = float(input("Enter distance in kilometers: "))
miles = 0.621371

# Convert distance from kilometers to miles
distance_miles1 = distance_km1 * miles

print(f"Distance in miles: {distance_miles1}")

# Ask the user if they want to retry another distance
retry = input("Do you want to convert another distance? (yes/no): ")

if retry == "yes":
    # Ask for 2nd distance in kilometers
    distance_km2 = float(input("Enter distance in kilometers: "))  
    
    # Convert 2nd distance from kilometers to miles 
    distance_miles2 = distance_km2 * miles

    print(f"Distance in miles: {distance_miles2}")

else:
    print("Program ended.")