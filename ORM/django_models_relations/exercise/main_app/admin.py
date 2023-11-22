from django.contrib import admin

from main_app.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "year", "owner", "car_details")

    @staticmethod
    def car_details(obj):
        try:
            owner_name = obj.owner.name
        except AttributeError:
            owner_name = "No owner"

        try:
            car_registration = obj.registration.registration_number
        except AttributeError:
            car_registration = "No registration number"

        return f"Owner: {owner_name}, Registration: {car_registration}"

    car_details.short_description = "Car Details"
