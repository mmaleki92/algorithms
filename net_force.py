def has_acceleration(force_x, force_y, force_neg_x, force_neg_y):
    # Calculate net force in x and y directions
    net_force_x = force_x - force_neg_x
    net_force_y = force_y - force_neg_y
    
    # Check if the net force is zero in both directions
    if net_force_x == 0 and net_force_y == 0:
        return False  # No acceleration
    return True  # Acceleration exists


# Example usage
forces = (10, 20, 10, 20)  # Forces in (x, y, -x, -y)
if has_acceleration(*forces):
    print("The body has acceleration.")
else:
    print("The body does not have acceleration.")




# 1 2 1 2
# No
# 12 15 11 15
# Yes