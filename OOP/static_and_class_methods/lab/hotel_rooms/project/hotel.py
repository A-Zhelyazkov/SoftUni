class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        room.take_room(people)

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        room.free_room()

    def status(self):
        total_guests = sum([r.guests for r in self.rooms if r.is_taken])
        result = f"Hotel {self.name} has {total_guests} total guests\n" \
                 f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}\n" \
                 f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}"
        return result