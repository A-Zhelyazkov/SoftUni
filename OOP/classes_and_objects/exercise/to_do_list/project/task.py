class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if self.name == new_name:
            return "Name cannot be the same."

        self.name = new_name
        return self.name

    def change_due_date(self, new_date):
        if self.due_date == new_date:
            return "Date cannot be the same."

        self.due_date = new_date
        return self.due_date

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, n, new_comment):
        if not 0 <= n < len(self.comments):
            return "Cannot find comment."

        self.comments[n] = new_comment
        return f"{', '.join([str(i) for i in self.comments])}"

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
