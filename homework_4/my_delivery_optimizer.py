from delivery_ga import DeliveryOptimizer, DELIVERY_LOCATIONS, AVERAGE_SPEED, SERVICE_TIME
import numpy as np

class MyDeliveryOptimizer(DeliveryOptimizer):
    """Optimized implementation of the delivery route optimizer."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Chromosome length: Each location is assigned a priority
        self.chromosome_length = len(DELIVERY_LOCATIONS)
    
    def decode_chromosome(self, chromosome: np.ndarray) -> list:
        """
        Decode chromosome into a delivery route.
        
        Args:
            chromosome: Binary array representing the solution
            
        Returns:
            list: Delivery route (indices of locations in order)
        """
        # Sort locations by their assigned priority in the chromosome
        return np.argsort(chromosome) + 1  # Convert 0-based to 1-based indexing
    
    def calculate_fitness(self, chromosome: np.ndarray) -> float:
        """
        Calculate fitness as the inverse of the total travel distance.
        
        Args:
            chromosome: Binary array representing the solution
            
        Returns:
            float: Fitness value (higher is better)
        """
        route = self.decode_chromosome(chromosome)
        total_distance = 0
        current_pos = (0, 0)  # Start at depot
        
        # Calculate total distance including return to depot
        for location_idx in route:
            next_pos = DELIVERY_LOCATIONS[location_idx - 1]
            total_distance += np.linalg.norm(np.array(next_pos) - np.array(current_pos))
            current_pos = next_pos
        
        total_distance += np.linalg.norm(np.array(current_pos))  # Return to depot
        
        return 1000 / (total_distance + 1)  # Higher fitness for shorter distances
    
    def _calculate_arrival_times(self, route: list) -> list:
        """
        Calculate arrival times at each location.
        
        Args:
            route: List of location indices
            
        Returns:
            list: Arrival times at each location (in minutes)
        """
        current_time = 0
        current_pos = (0, 0)  # Start at depot
        arrival_times = []
        
        for location_idx in route:
            next_pos = DELIVERY_LOCATIONS[location_idx - 1]
            travel_time = (np.linalg.norm(np.array(next_pos) - np.array(current_pos)) / AVERAGE_SPEED) * 60
            current_time += travel_time + SERVICE_TIME
            arrival_times.append(current_time)
            current_pos = next_pos
        
        return arrival_times
