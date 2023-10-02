class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill, mana):
        if skill in self.skills:
            return "Skill already added"

        self.skills[skill] = mana
        return f"Skill {skill} added to the collection of the player {self.name}"

    def player_info(self):
        result = f"Name: {self.name}\n" + \
                 f"Guild: {self.guild}\n" + \
                 f"HP: {self.hp}\n" + \
                 f"MP: {self.mp}"

        for skill, mana in self.skills.items():
            result += f"\n==={skill} - {mana}"

        return result

