# print("Hello World")

counties_dict = {'Araphoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
# print(counties_dict)

voting_data = {1: {'county': 'El Paso', 
    'registered_voters': 461149}, 2:{
    'county': 'Jefferson',
    'registered_voters': 432438}, 3:{
    'county': 'Denver', 
    'registered_voters': 463353}, 4:{
    'county': 'Arapahoe',
    'registered_voters': 422829}}
print(voting_data[1].values())

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == "Denver":
    #print(counties[1])

#if counties[3] != "Jefferson":
    #print(counties[2])

# if "El Paso" in counties:
    # print ("El Paso is in the list of counties.")
# else:
    # print("El Paso is not in the list of counties.")

# if "Arapahoe" in counties and "El Paso" not in counties:
    # print("Only Arapahoe is in the list of counties.")
# else: 
    # print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# for county in counties:
    # print(county)

# for county in counties_dict.keys():
    # print(county)

# for voters in counties_dict.values():
    # print(voters)

for county,voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county,voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")