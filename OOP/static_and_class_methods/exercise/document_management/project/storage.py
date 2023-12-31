class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = [c for c in self.categories if category_id == c.id][0]
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = [t for t in self.topics if topic_id == t.id][0]
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = [d for d in self.documents if document_id == d.id][0]
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = [c for c in self.categories if category_id == c.id][0]
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = [t for t in self.topics if topic_id == t.id][0]
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [d for d in self.documents if document_id == d.id][0]
        self.documents.remove(document)

    def get_document(self, document_id):
        document = [d for d in self.documents if document_id == d.id][0]
        return document

    def __repr__(self):
        result = ""
        for d in self.documents:
            result += f"{d}\n"

        return result