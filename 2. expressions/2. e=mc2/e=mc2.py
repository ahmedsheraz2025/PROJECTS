
# Write a program that continually reads in mass from the 
# and then outputs the equivalent energy using Einstein's mass-energy equivalence formula


C = 299792458

def main():
    mass_in_kilo = float(input("Enter the mass: "))
    
    # Calcuation:
    energy : float = mass_in_kilo * (C ** 2)
    
    # Print output:
    print(f"Energy: {energy}")
    
    
      
if __name__ == '__main__':
    main()

