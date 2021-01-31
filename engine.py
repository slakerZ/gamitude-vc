from transformers import pipeline


class engine:
    # todo add dict with command + template
    candidate_labels = ["select project", "select folder", "select timer"]
    hypothesis_template_project = "project {}"
    hypothesis_template_folder = "folder {}"
    hypothesis_template_timer = "timer {}"

    def __init__(self, sentence: str):
        self.sentence = sentence
        self.classifier = pipeline("zero-shot-classification")

    def get_command(self):
        score = self.classifier(self.sentence, self.candidate_labels)
        mapped = dict(zip(score["labels"], score["scores"]))
        return max(mapped, key=mapped.get)

    def get_entity(self, entities, command):
        hypothesis_template, entities = self.get_correct_entities(entities, command)
        score = self.classifier(
            self.sentence, entities, hypothesis_template=hypothesis_template
        )
        mapped = dict(zip(score["labels"], score["scores"]))
        return max(mapped, key=mapped.get)

    def get_correct_entities(self, entities, command):
        if command is self.candidate_labels[0]:
            return self.hypothesis_template_project, entities["projects"]
        elif command is self.candidate_labels[1]:
            return self.hypothesis_template_folder, entities["folders"]
        elif command is self.candidate_labels[2]:
            return self.hypothesis_template_timer, entities["timers"]
