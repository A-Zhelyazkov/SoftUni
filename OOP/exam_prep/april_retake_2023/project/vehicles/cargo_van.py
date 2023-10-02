from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    def __init__(self, brand, model, license_plate_number):
        super().__init__(brand, model, license_plate_number, 180)

    def drive(self, mileage):
        percentage = (mileage / self.max_mileage) * 100
        rounded = int(percentage-0.5)+1
        self.battery_level -= (rounded + 5)