
# # from gcms import GCMS
# # from object import Color
# # from exceptions import NoBinFoundException
# # import pdb
# # if __name__ == "__main__":

# #     gcms = GCMS()

# #     # Adding bins with varying capacities
# #     # Adding objects with specific sizes and colors
    
# #     gcms.add_object(2001, 20, Color.RED)  # Object 2001 (Size 20, RED)

# #     # Bin information based on the correct answer
# #     # bin_info returns the number of objects and the list of objects stored

# #     # Object information based on the correct answer
# #     # object_info returns the value of the bin where the object is stored
# #     print(gcms.object_info(2001))  # Expected: 1001
    
    
# # from gcms import GCMS
# # from object import Color
# # from exceptions import NoBinFoundException

# # def print_separator():
# #     print("\n" + "-"*80 + "\n")

# # if __name__ == "__main__":
# #     # Initialize GCMS
# #     gcms = GCMS()
    
# #     # Adding an initial set of bins with varying capacities
# #     initial_bin_data = [
# #         (1001, 50),
# #         (1002, 30),
# #         (1003, 40),
# #         (1004, 25),
# #         (1005, 35),
# #         (1006, 60),
# #         (1007, 45),
# #         (1008, 55),
# #         (1009, 20),
# #         (1010, 70)
# #     ]
    
# #     print("Adding Initial Bins:")
# #     for bin_id, capacity in initial_bin_data:
# #         gcms.add_bin(bin_id, capacity)
# #         print(f"Added Bin ID: {bin_id}, Capacity: {capacity}")
    
# #     print_separator()
    
# #     # Adding an initial set of objects with varying sizes and colors
# #     initial_object_data = [
# #         (2001, 20, Color.RED),
# #         (2002, 15, Color.YELLOW),
# #         (2003, 10, Color.BLUE),
# #         (2004, 25, Color.GREEN),
# #         (2005, 30, Color.RED),
# #         (2006, 5, Color.YELLOW),
# #         (2007, 8, Color.BLUE),
# #         (2008, 22, Color.GREEN),
# #         (2009, 35, Color.BLUE),
# #         (2010, 40, Color.RED),
# #         (2011, 12, Color.YELLOW),
# #         (2012, 18, Color.GREEN),
# #         (2013, 7, Color.BLUE),
# #         (2014, 28, Color.RED),
# #         (2015, 16, Color.YELLOW)
# #     ]
    
# #     print("Adding Initial Objects:")
# #     for obj_id, size, color in initial_object_data:
# #         try:
# #             gcms.add_object(obj_id, size, color)
# #             print(f"Added Object ID: {obj_id}, Size: {size}, Color: {color.name}")

# #         except NoBinFoundException:
# #             print(f"Failed to add Object ID: {obj_id}, Size: {size}, Color: {color.name} - No suitable bin found")
    
# #     print_separator()
    
# #     # Displaying bin information after initial additions
# #     print("Bin Information After Adding Initial Objects:")
# #     for bin_id, _ in initial_bin_data:
# #         try:
# #             remaining_capacity, objects_in_bin = gcms.bin_info(bin_id)
# #             print(f"Bin ID: {bin_id}, Remaining Capacity: {remaining_capacity}, Objects: {objects_in_bin}")
# #         except Exception as e:
# #             print(f"Error retrieving info for Bin ID: {bin_id} - {str(e)}")
    
# #     print_separator()
    
# #     # Displaying object information after initial additions
# #     print("Object Information After Adding Initial Objects:")
# #     for obj_id, _, _ in initial_object_data:
# #         try:
# #             assigned_bin = gcms.object_info(obj_id)
# #             print(f"Object ID: {obj_id} is assigned to Bin ID: {assigned_bin}")
# #         except Exception as e:
# #             print(f"Error retrieving info for Object ID: {obj_id} - {str(e)}")
    
# #     print_separator()
    
# #     # Adding additional bins after some objects have been placed
# #     additional_bin_data = [
# #         (1011, 65),
# #         (1012, 45),
# #         (1013, 55)
# #     ]
    
# #     print("Adding Additional Bins:")
# #     for bin_id, capacity in additional_bin_data:
# #         gcms.add_bin(bin_id, capacity)
# #         print(f"Added Bin ID: {bin_id}, Capacity: {capacity}")
    
# #     print_separator()
    
# #     # Adding additional objects after new bins have been added
# #     additional_object_data = [
# #         (2016, 25, Color.GREEN),
# #         (2017, 14, Color.YELLOW),
# #         (2018, 9, Color.BLUE),
# #         (2019, 50, Color.RED),
# #         (2020, 33, Color.YELLOW),
# #         (2021, 12, Color.GREEN),
# #         (2022, 7, Color.BLUE),
# #         (2023, 19, Color.RED),
# #         (2024, 28, Color.YELLOW),
# #         (2025, 11, Color.BLUE)
# #     ]
    
# #     print("Adding Additional Objects:")
# #     for obj_id, size, color in additional_object_data:
# #         try:
# #             gcms.add_object(obj_id, size, color)
# #             print(f"Added Object ID: {obj_id}, Size: {size}, Color: {color.name}")
# #         except NoBinFoundException:
# #             print(f"Failed to add Object ID: {obj_id}, Size: {size}, Color: {color.name} - No suitable bin found")
    
# #     print_separator()
    
# #     # Displaying bin information after adding additional objects
# #     print("Bin Information After Adding Additional Objects:")
# #     for bin_id, _ in initial_bin_data + additional_bin_data:
# #         try:
# #             remaining_capacity, objects_in_bin = gcms.bin_info(bin_id)
# #             print(f"Bin ID: {bin_id}, Remaining Capacity: {remaining_capacity}, Objects: {objects_in_bin}")
# #         except Exception as e:
# #             print(f"Error retrieving info for Bin ID: {bin_id} - {str(e)}")
    
# #     print_separator()
    
# #     # Displaying object information after adding additional objects
# #     print("Object Information After Adding Additional Objects:")
# #     for obj_id, _, _ in initial_object_data + additional_object_data:
# #         try:
# #             assigned_bin = gcms.object_info(obj_id)
# #             print(f"Object ID: {obj_id} is assigned to Bin ID: {assigned_bin}")
# #         except Exception as e:
# #             print(f"Object ID: {obj_id} has been deleted or does not exist - {str(e)}")
    
# #     print_separator()
    
# #     # Deleting some objects
# #     objects_to_delete = [2003, 2005, 2010, 2015, 2018, 2019] 
# #     print("Deleting Objects:")
# #     for obj_id in objects_to_delete:
# #         try:
# #             gcms.delete_object(obj_id)
# #             print(f"Deleted Object ID: {obj_id}")
# #         except Exception as e:
# #             print(f"Failed to delete Object ID: {obj_id} - {str(e)}")
    
# #     print_separator()
    
# #     # Displaying bin information after deletions
# #     print("Bin Information After Deleting Objects:")
# #     for bin_id, _ in initial_bin_data + additional_bin_data:
# #         try:
# #             remaining_capacity, objects_in_bin = gcms.bin_info(bin_id)
# #             print(f"Bin ID: {bin_id}, Remaining Capacity: {remaining_capacity}, Objects: {objects_in_bin}")
# #         except Exception as e:
# #             print(f"Error retrieving info for Bin ID: {bin_id} - {str(e)}")
    
# #     print_separator()

# #     # Displaying object information after deletions
# #     print("Object Information After Deleting Objects:")
# #     current_items = initial_object_data + additional_object_data

# #     current_items = [ elt for elt, _, _ in current_items] 
# #     current_items = [elt for elt in current_items if elt not in objects_to_delete]
# #     for obj_id in current_items:
# #         try:
# #             assigned_bin = gcms.object_info(obj_id)
# #             print(f"Object ID: {obj_id} is assigned to Bin ID: {assigned_bin}")
# #         except Exception as e:
# #             print(f"Object ID: {obj_id} has been deleted or does not exist - {str(e)}")
    
# #     print_separator()
    
# #     # Attempting to add an object that cannot fit into any bin
# #     print("Adding an Object That Cannot Fit into Any Bin:")
# #     try:
# #         gcms.add_object(2026, 100, Color.BLUE)
# #         print(f"Added Object ID: 2026, Size: 100, Color: BLUE")
# #     except NoBinFoundException:
# #         print("Failed to add Object ID: 2026, Size: 100, Color: BLUE - No suitable bin found")
    
# #     print_separator()
    
# #     # Final bin information
# #     print("Final Bin Information:")
# #     for bin_id, _ in initial_bin_data + additional_bin_data:
# #         try:
# #             remaining_capacity, objects_in_bin = gcms.bin_info(bin_id)
# #             print(f"Bin ID: {bin_id}, Remaining Capacity: {remaining_capacity}, Objects: {objects_in_bin}")
# #         except Exception as e:
# #             print(f"Error retrieving info for Bin ID: {bin_id} - {str(e)}")
    
# #     print_separator()
    
# #     print("All enhanced tests completed.")
# from gcms import GCMS
# from object import Color
# from exceptions import NoBinFoundException

# if __name__ == "__main__":
#     # Initialize GCMS
#     gcms = GCMS()

#     # Add 10 bins with different capacities
#     gcms.add_bin(1001, 10)
#     gcms.add_bin(1002, 15)
#     gcms.add_bin(1003, 12)
#     gcms.add_bin(1004, 20)
#     gcms.add_bin(1005, 8)
#     gcms.add_bin(1006, 18)
#     gcms.add_bin(1007, 25)
#     gcms.add_bin(1008, 30)
#     gcms.add_bin(1009, 22)
#     gcms.add_bin(1010, 35)

#     # Add 20 objects with varying sizes and colors
#     objects = [
#         (2001, 5, Color.BLUE), (2002, 6, Color.GREEN), (2003, 4, Color.RED),
#         (2004, 7, Color.YELLOW), (2005, 3, Color.BLUE), (2006, 9, Color.GREEN),
#         (2007, 12, Color.RED), (2008, 2, Color.YELLOW), (2009, 11, Color.BLUE),
#         (2010, 14, Color.GREEN), (2011, 6, Color.RED), (2012, 4, Color.YELLOW),
#         (2013, 8, Color.BLUE), (2014, 7, Color.GREEN), (2015, 3, Color.RED),
#         (2016, 2, Color.YELLOW), (2017, 13, Color.BLUE), (2018, 1, Color.GREEN),
#         (2019, 5, Color.RED), (2020, 10, Color.YELLOW)
#     ]

#     for obj_id, size, color in objects:
#         try:
#             gcms.add_object(obj_id, size, color)
#         except NoBinFoundException:
#             print(f"Object {obj_id} was not able to be added")

#     # Print information about the bins
#     for bin_id in range(1001, 1011):
#         print(gcms.bin_info(bin_id))

#     # Delete some objects
#     gcms.delete_object(2003)  # Object ID 2003
#     gcms.delete_object(2010)  # Object ID 2010
#     gcms.delete_object(2009)  # Object ID 2009

#     # Print bin information after deletions
#     print("\nAfter deleting objects:")
#     for bin_id in range(1001, 1011):
#         print(gcms.bin_info(bin_id))
# # from gcms import GCMS
# # from object import Color
# # from exceptions import NoBinFoundException
# # if __name__=="__main__":

# #     gcms = GCMS()
# #     gcms.add_bin(1001, 10)
# #     gcms.add_bin(1002, 10)
# #     gcms.add_bin(1003, 20)
# #     gcms.add_bin(1004, 20)
# #     gcms.add_bin(1005, 18)
# #     gcms.add_bin(1006, 18)
# #     gcms.add_bin(1007, 25)
# #     gcms.add_bin(1008, 25)
# #     gcms.add_bin(1009, 30)
# #     gcms.add_bin(1010, 30)
# #     #print(gcms.bincapacitytreeblue.inorder_traversaldata())
# #     #print(gcms.bincapacitytreeyellow.inorder_traversaldata())
# #     #print(gcms.bincapacitytreered.inorder_traversaldata())
# #     #print(gcms.bincapacitytreegreen.inorder_traversaldata())


# #     # Add 20 objects with varying sizes and colors
# #     objects = [
# #         (2001, 5, Color.BLUE), (2002, 6, Color.GREEN), (2003, 4, Color.RED),
# #         (2004, 7, Color.YELLOW), (2005, 3, Color.BLUE), (2006, 9, Color.GREEN),
# #         (2007, 12, Color.RED), (2008, 2, Color.YELLOW), (2009, 11, Color.BLUE),
# #         (2010, 14, Color.GREEN), (2011, 6, Color.RED), (2012, 4, Color.YELLOW),
# #         (2013, 8, Color.BLUE), (2014, 7, Color.GREEN), (2015, 3, Color.RED),
# #         (2016, 2, Color.YELLOW), (2017, 13, Color.BLUE), (2018, 1, Color.GREEN),
# #         (2019, 5, Color.RED), (2020, 10, Color.YELLOW)
# #         ]

# #     for obj_id, size, color in objects:
# #         try:
# #             gcms.add_object(obj_id, size, color)
# #         except NoBinFoundException:
# #             print(f"Object {obj_id} was not able to be added")

# #         # Print information about the bins
# #     for bin_id in range(1001, 1011):
# #         print(gcms.bin_info(bin_id))

# #         # Delete some objects
# #     gcms.delete_object(2003)  # Object ID 2003
# #     gcms.delete_object(2010)  # Object ID 2010
# #     gcms.delete_object(2009)  # Object ID 2009

# #         # Print bin information after deletions
# #     print("\nAfter deleting objects:")
# #     for bin_id in range(1001, 1011):
# #         print(gcms.bin_info(bin_id))
# # from gcms import GCMS
# # from object import Color
# # from exceptions import NoBinFoundException

# # if __name__ == "__main__":

# #     gcms = GCMS()

# #     # Step 1: Add some bins with capacities
# #     gcms.add_bin(1234, 10)
# #     gcms.add_bin(4321, 20)
# #     gcms.add_bin(1111, 15)

# #     # Step 2: Add an object
# #     try:
# #         gcms.add_object(1001, 6, Color.RED)  # Add object with size 6
# #         print("Object 1001 added with size 6.")
# #     except NoBinFoundException:
# #         print("Object 1001 could not be added.")

# #     # Step 3: Check bin info before deletion
# #     print("Before deletion:")
# #     print(gcms.bin_info(1234))
# #     print(gcms.bin_info(4321))
# #     print(gcms.bin_info(1111))

# #     # Step 4: Delete the object
# #     try:
# #         gcms.delete_object(1001)
# #         print("Object 1001 deleted.")
# #     except:
# #         print("Failed to delete object 1001.")

# #     # Step 5: Check bin info after deletion
# #     print("After deletion:")
# #     print(gcms.bin_info(1234))
# #     print(gcms.bin_info(4321))
# #     print(gcms.bin_info(1111))

# #     # Step 6: Re-add the same object but with a different size
# #     try:
# #         gcms.add_object(1001, 8, Color.RED)  # Add object with new size 8
# #         print("Object 1001 added again with size 8.")
# #     except NoBinFoundException:
# #         print("Object 1001 could not be re-added.")

# #     # Step 7: Check bin info after re-adding the object
# #     print("After re-adding:")
# #     print(gcms.bin_info(1234))
# #     print(gcms.bin_info(4321))
# #     print(gcms.bin_info(1111))
# # from gcms import GCMS
# # from object import Color
# # from exceptions import NoBinFoundException
# # import random

# # if __name__ == "__main__":

# #     # Set the seed for random number generation to ensure identical results on different machines
# #     random.seed(42)

# #     # Initialize GCMS instance
# #     gcms = GCMS()

# #     # Function to generate random color
# #     def get_random_color():
# #         return random.choice([Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW])

# #     # Add 200 bins with unique IDs and random sizes
# #     for i in range(1, 201):
# #         bin_id = 4000 + i  # Unique bin IDs starting from 4001 to 4200
# #         bin_size = random.randint(40, 100)  # Random bin size between 40 and 100
# #         gcms.add_bin(bin_id, bin_size)

# #     # Add 400 objects with unique IDs, random colors, and sizes
# #     for i in range(1, 401):
# #         object_id = 7000 + i  # Unique object IDs starting from 7001 to 7400
# #         object_size = random.randint(5, 50)  # Random object size between 5 and 50
# #         object_color = get_random_color()

# #         try:
# #             gcms.add_object(object_id, object_size, object_color)
# #             # Print object info
# #             print(f"Added Object: {gcms.object_info(object_id)}")
# #         except Exception as e:
# #             print(f"Error adding object {object_id}: {e}")

# #     # Set to keep track of deleted objects
# #     deleted_objects = set()

# #     # Delete 100 objects randomly
# #     for _ in range(100):
# #         while True:
# #             object_id = 7000 + random.randint(1, 400)  # Randomly choose an object to delete
# #             if object_id not in deleted_objects:
# #                 try:
# #                     gcms.delete_object(object_id)
# #                     deleted_objects.add(object_id)  # Mark object as deleted
# #                     print(f"Deleted Object: {object_id}")
# #                     break  # Exit the while loop if object deleted successfully
# #                 except Exception as e:
# #                     print(f"Error deleting object {object_id}: {e}")
# #                     break  # Break if error occurs (such as the object not being found)

# #     # Print bin info for all 200 bins at the end
# #     for i in range(1, 201):
# #         bin_id = 4000 + i
# #         try:
# #             print(f"Bin Info: {gcms.bin_info(bin_id)}")
# #         except NoBinFoundException as e:
# #             print(f"Error fetching info for bin {bin_id}: {e}")

# #     print("DONE")


from gcms import GCMS
from object import Color
from exceptions import NoBinFoundException
if __name__=="__main__":

    gcms = GCMS()
    gcms.add_bin(1001, 10)
    gcms.add_bin(1002, 10)
    gcms.add_bin(1003, 20)
    gcms.add_bin(1004, 20)
    gcms.add_bin(1005, 18)
    gcms.add_bin(1006, 18)
    gcms.add_bin(1007, 25)
    gcms.add_bin(1008, 25)
    gcms.add_bin(1009, 30)
    gcms.add_bin(1010, 30)
    #print(gcms.bincapacitytreeblue.inorder_traversaldata())
    #print(gcms.bincapacitytreeyellow.inorder_traversaldata())
    #print(gcms.bincapacitytreered.inorder_traversaldata())
    #print(gcms.bincapacitytreegreen.inorder_traversaldata())


    # Add 20 objects with varying sizes and colors
    objects = [
        (2001, 5, Color.BLUE), (2002, 6, Color.GREEN), (2003, 4, Color.RED),
        (2004, 7, Color.YELLOW), (2005, 3, Color.BLUE), (2006, 9, Color.GREEN),
        (2007, 12, Color.RED), (2008, 2, Color.YELLOW), (2009, 11, Color.BLUE),
        (2010, 14, Color.GREEN), (2011, 6, Color.RED), (2012, 4, Color.YELLOW),
        (2013, 8, Color.BLUE), (2014, 7, Color.GREEN), (2015, 3, Color.RED),
        (2016, 2, Color.YELLOW), (2017, 13, Color.BLUE), (2018, 1, Color.GREEN),
        (2019, 5, Color.RED), (2020, 10, Color.YELLOW)
        ]

    for obj_id, size, color in objects:
        try:
            gcms.add_object(obj_id, size, color)
        except NoBinFoundException:
            print(f"Object {obj_id} was not able to be added")

        # Print information about the bins
    for bin_id in range(1001, 1011):
        print(gcms.bin_info(bin_id))

        # Delete some objects
    gcms.delete_object(2003)  # Object ID 2003
    gcms.delete_object(2010)  # Object ID 2010
    gcms.delete_object(2009)  # Object ID 2009

        # Print bin information after deletions
    print("\nAfter deleting objects:")
    for bin_id in range(1001, 1011):
        print(gcms.bin_info(bin_id))