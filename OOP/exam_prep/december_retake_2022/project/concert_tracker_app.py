from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer,
    }

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type, name, age):
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")

        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")

        musician = self.VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre, audience, ticket_price, expenses, place):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name, band_name):
        band = [b for b in self.bands if b.name == band_name]
        musician = [m for m in self.musicians if m.name == musician_name]

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        curr_band = band[0]
        curr_band.members.append(musician[0])

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name, band_name):
        band = [b for b in self.bands if b.name == band_name]

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        curr_band = band[0]
        musician = [m for m in curr_band.members if m.name == musician_name]
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        curr_band.members.remove(musician[0])
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place, band_name):
        concert = [c for c in self.concerts if c.place == concert_place][0]
        band = [b for b in self.bands if b.name == band_name][0]
        current_musicians = set()

        for member in band.members:
            if isinstance(member, Drummer):
                current_musicians.add("Drummer")
            if isinstance(member, Guitarist):
                current_musicians.add("Guitarist")
            if isinstance(member, Singer):
                current_musicians.add("Singer")

        if len(current_musicians) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert_genre = concert.genre

        if "Rock" == concert_genre:
            for member in band.members:
                if isinstance(member, Singer):
                    if "sing high pitch notes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

                if isinstance(member, Drummer):
                    if "play the drums with drumsticks" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

                if isinstance(member, Guitarist):
                    if "play rock" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        if "Metal" == concert_genre:
            for member in band.members:
                if isinstance(member, Singer):
                    if "sing low pitch notes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

                if isinstance(member, Drummer):
                    if "play the drums with drumsticks" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

                if isinstance(member, Guitarist):
                    if "play metal" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        if "Jazz" == concert_genre:
            for member in band.members:
                if isinstance(member, Singer):
                    if "sing low pitch notes" in member.skills and "sing high pitch notes" in member.skills:
                        pass
                    else:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

                if isinstance(member, Drummer):
                    if "play the drums with drum brushes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

                if isinstance(member, Guitarist):
                    if "play jazz" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

