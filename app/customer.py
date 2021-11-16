import random
import time

class Customer:
    """
    Represents a group of persons running individual bike objects.
    """

    routes_by_city = {}
    _id = None
    bike = None
    route = None
    route_idx = 0

    def __init__(self, calculated_routes, id, bike):
        self.routes_by_city = calculated_routes
        self._id = id
        self.bike = bike

    def reset_bike(self, bike):
        speed = random.randint(5, 20)
        should_reverse = random.randint(0, 1)
        route_idx = random.randint(0, len(self.routes_by_city["umea"]) - 1)
        points = self.routes_by_city["umea"][route_idx][speed]
        if should_reverse == 1:
            points.reverse()
        bike.reset_route(points)
            
    def run(self):
        """
        Runs specified number of bikes with random route and
        speed for every bike.
        """
        speed = random.randint(5, 20)
        should_reverse = random.randint(0, 1)
        route_idx = random.randint(0, len(self.routes_by_city["umea"]) - 1)
        self.route = self.routes_by_city["umea"][route_idx][speed]
        if should_reverse == 1:
            self.route.reverse()

        self.bike.start()

        self.start_bike(self.bike)

    def start_bike(self, bike):
        """
        Starts all bikes and bulk updates their position according
        to respective route every second.
        """
        for location in self.route:
            bike.move_bike(location)
            time.sleep(10)
        #bike.check_in_parking_area(self.routes_by_city["parkings"])