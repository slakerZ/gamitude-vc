class engine:
    # todo add dict with command + template
    candidate_labels = ["select project", "select folder", "select timer"]
    hypothesis_template_project = "project {}"
    hypothesis_template_folder = "folder {}"
    hypothesis_template_timer = "timer {}"

    def __init__(self, sentence: str, classifier):
        self.sentence = sentence
        self.classifier = classifier

    def get_command(self):
        score = self.classifier(self.sentence, self.candidate_labels)
        mapped = dict(zip(score["labels"], score["scores"]))
        command = max(mapped, key=mapped.get)
        return command

    def get_entity(self, entities, command):
        hypothesis_template, entities = self.get_correct_entities(entities, command)
        names_list = [x["name"] for x in entities]
        score = self.classifier(
            self.sentence, names_list, hypothesis_template=hypothesis_template
        )
        mapped = dict(zip(score["labels"], score["scores"]))
        entity_name = max(mapped, key=mapped.get)
        f = next((x for x in entities if x["name"] == entity_name), ["error"])
        return f

    def get_correct_entities(self, entities, command):
        if command == self.candidate_labels[0]:
            return self.hypothesis_template_project, entities["projects"]
        elif command == self.candidate_labels[1]:
            return self.hypothesis_template_folder, entities["folders"]
        elif command == self.candidate_labels[2]:
            return self.hypothesis_template_timer, entities["timers"]
