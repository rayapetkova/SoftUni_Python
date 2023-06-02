from project.topic import Topic
from project.category import Category
from project.document import Document


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

    def edit_category(self, category_id: int, new_name: str):
        for c_category in self.categories:
            if c_category.id == category_id:
                c_category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for c_topic in self.topics:
            if c_topic.id == topic_id:
                c_topic.topic = new_topic
                c_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        for c_document in self.documents:
            if c_document.id == document_id:
                c_document.file_name = new_file_name

    def delete_category(self, category_id):
        for c_category in self.categories:
            if c_category.id == category_id:
                self.categories.remove(c_category)

    def delete_topic(self, topic_id):
        for c_topic in self.topics:
            if c_topic.id == topic_id:
                self.topics.remove(c_topic)

    def delete_document(self, document_id):
        for c_document in self.documents:
            if c_document.id == document_id:
                self.documents.remove(c_document)

    def get_document(self, document_id):
        for c_document in self.documents:
            if c_document.id == document_id:
                return str(c_document)

    def __repr__(self):
        final = []

        for c_document in self.documents:
            final.append(str(c_document))

        return '\n'.join(final)


