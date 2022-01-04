from kivy.app import App
from kivy.lang import Builder


class DynamicLabels(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = [["Bob Brown", "0414144411"], ["Cat Cyan", "0441411211"], ["Oren Ochre", "0432123456"]]

    def build(self):
        self.title = "Dynamic labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.handle_show()
        return self.root

    def handle_show(self):
        # for i in range(len(self.name_to_phone)):
        self.root.ids.output_label.text = "{} number is {}".format(self.name_to_phone[0][0], self.name_to_phone[0][1])
        self.root.ids.output_label_2.text = "{} number is {}".format(self.name_to_phone[1][0], self.name_to_phone[1][1])
        self.root.ids.output_label_3.text = "{} number is {}".format(self.name_to_phone[2][0], self.name_to_phone[2][1])


DynamicLabels().run()
