#Set

cars={"BMW","Audi","Tata","Ford"}
#sets are unordered collection of items
#sets' items are immutable but we can add or remove items
#sets do not allow duplicate values

complex_set={1, "Hello", 3.14, True, None}
#Set can contain different data types

#Accessing elements in a set---------------------------------------
for car in cars:
    print(car) #Print each element in the set
print(cars) #Print the entire set
#----------------------------------------------------------------------


#----------------------------------------------------------------------

#Set operations-----------------------------------------------------
print(len(cars)) #Length of the set

num1={1,2,3}
num2={3,4,5}
cars.update(num1,num2) #Adding multiple elements to the set
#cars |= num1 | num2   Alternative way to add multiple elements using union operator

cars.add("Mercedes") #Adding an element to the set


cars.remove("Tata") #Removing an element from the set (raises error if not found)
cars.discard("Hyundai") #Removing an element that may not exist (no error if not found)
cars.pop() #Removes and returns an random element from the set
cars.clear() #Clears the set but keeps the set itself
del cars #Deleting the set completely

more_cars={"Honda","Hyundai","Ford"}
all_cars=cars.union(more_cars) #Union of two sets
# all_cars=cars | more_cars  Alternative way to do union using | operator

common_cars=cars.intersection(more_cars) #Intersection of two sets
# common_cars=cars & more_cars  Alternative way to do intersection using & operator

cars.intersection_update(more_cars) #changed original set
#Update cars set to keep only common elements with more_cars

diff_cars=cars.difference(more_cars) #Difference of two sets
# diff_cars=cars - more_cars  Alternative way to do difference using - operator
#also there is a difference_update() method to change original set

symmetric_diff=cars.symmetric_difference(more_cars) #Symmetric difference of two sets
# symmetric_diff=cars ^ more_cars  Alternative way
#also there is a symmetric_difference_update() method to change original set

copies=cars.copy() #Create a copy


#----------------------------------------------------------------------

