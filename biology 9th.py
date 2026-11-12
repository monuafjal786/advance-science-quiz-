
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp

Window.clearcolor = (0.08, 0.10, 0.16, 1)

questions = {
    
    "Biology": [
        ("Living organisms ki basic unit kya hai?",
         ["Tissue", "Cell", "Organ", "Organ system"], 1),

        ("Cell ki khoj kisne ki thi?",
         ["Robert Hooke", "Darwin", "Mendel", "Pasteur"], 0),

        ("Cell ka powerhouse kise kehte hain?",
         ["Nucleus", "Mitochondria", "Ribosome", "Golgi body"], 1),

        ("Plant cell ki cell wall kiski bani hoti hai?",
         ["Protein", "Cellulose", "Fat", "Starch"], 1),

        ("Cell ka control centre kya hai?",
         ["Vacuole", "Nucleus", "Cytoplasm", "Ribosome"], 1),

        ("Photosynthesis kis organelle mein hota hai?",
         ["Mitochondria", "Chloroplast", "Nucleus", "Golgi body"], 1),

        ("Protein synthesis ka kaam kaun karta hai?",
         ["Ribosome", "Lysosome", "Vacuole", "Nucleus"], 0),

        ("Cell membrane ka nature kaisa hota hai?",
         ["Fully permeable", "Selectively permeable",
          "Impermeable", "Rigid"], 1),

        ("Plant cell mein bada vacuole kis kaam aata hai?",
         ["Storage", "Respiration", "Movement", "Digestion"], 0),

        ("Prokaryotic cell mein kya absent hota hai?",
         ["Cell membrane", "Cytoplasm",
          "True nucleus", "Ribosome"], 2),

        ("Plant mein water transport kaun karta hai?",
         ["Phloem", "Xylem", "Epidermis", "Cortex"], 1),

        ("Plant mein food transport kaun karta hai?",
         ["Xylem", "Phloem", "Root hair", "Stomata"], 1),

        ("Blood kis type ka tissue hai?",
         ["Muscular", "Nervous", "Connective", "Epithelial"], 2),

        ("Muscle contraction mein kaun se proteins help karte hain?",
         ["Actin aur Myosin", "Keratin aur Collagen",
          "Insulin aur Glucagon", "DNA aur RNA"], 0),

        ("Nervous tissue ki structural unit kya hai?",
         ["Neuron", "Nephron", "Alveoli", "Osteocyte"], 0),

        ("Plant ki outer protective tissue kya hai?",
         ["Xylem", "Epidermis", "Phloem", "Cambium"], 1),

        ("Stomata ka main function kya hai?",
         ["Food storage", "Gas exchange",
          "Water absorption", "Seed formation"], 1),

        ("Bone kis type ka tissue hai?",
         ["Muscular", "Connective", "Nervous", "Epithelial"], 1),

        ("Voluntary muscles ka example kya hai?",
         ["Heart muscle", "Biceps muscle",
          "Stomach muscle", "Intestinal muscle"], 1),

        ("Meristematic tissue ka main function kya hai?",
         ["Photosynthesis", "Growth",
          "Food storage", "Transport"], 1),

        ("Classification ka main purpose kya hai?",
         ["Organisms ko group karna", "Food banana",
          "Respiration karna", "Movement karna"], 0),

        ("Binomial nomenclature kisne diya?",
         ["Darwin", "Linnaeus", "Mendel", "Whittaker"], 1),

        ("Five kingdom classification kisne diya?",
         ["R. H. Whittaker", "Linnaeus",
          "Aristotle", "Haeckel"], 0),

        ("Fungi ki cell wall kiski bani hoti hai?",
         ["Cellulose", "Chitin", "Protein", "Lipid"], 1),

        ("Bacteria kis kingdom mein aate hain?",
         ["Protista", "Monera", "Fungi", "Plantae"], 1),

        ("Mushroom kis kingdom ka member hai?",
         ["Animalia", "Plantae", "Fungi", "Monera"], 2),

        ("Fish kis group ke animals hain?",
         ["Amphibia", "Pisces", "Reptilia", "Mammalia"], 1),

        ("Earthworm kis phylum ka member hai?",
         ["Annelida", "Arthropoda", "Mollusca", "Porifera"], 0),

        ("Cockroach kis phylum mein aata hai?",
         ["Annelida", "Arthropoda", "Mollusca", "Cnidaria"], 1),

        ("Frog kis class ka animal hai?",
         ["Pisces", "Amphibia", "Reptilia", "Aves"], 1),

        ("Life ki basic requirement kya hai?",
         ["Food", "Plastic", "Metal", "Smoke"], 0),

        ("Cellular respiration ka main purpose kya hai?",
         ["Energy release karna", "Water banana",
          "Growth rokna", "Food store karna"], 0),

        ("Aerobic respiration ke liye kya zaroori hai?",
         ["Nitrogen", "Oxygen", "Carbon dioxide", "Hydrogen"], 1),

        ("Human lungs mein gas exchange kahan hota hai?",
         ["Trachea", "Alveoli", "Bronchi", "Nose"], 1),

        ("Human heart mein kitne chambers hote hain?",
         ["Two", "Three", "Four", "Five"], 2),

        ("Blood mein oxygen transport kaun karta hai?",
         ["WBC", "RBC", "Platelets", "Plasma only"], 1),

        ("Plants mein food banane ki process kya hai?",
         ["Respiration", "Photosynthesis",
          "Transpiration", "Excretion"], 1),

        ("Photosynthesis ke liye kaunsi gas chahiye?",
         ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], 1),

        ("Transpiration mainly kis part se hota hai?",
         ["Root", "Stomata", "Flower", "Seed"], 1),

        ("Human body ka largest organ kaun sa hai?",
         ["Heart", "Liver", "Skin", "Kidney"], 2),

        ("Kidney ki functional unit kya hai?",
         ["Neuron", "Nephron", "Alveolus", "Villus"], 1),

        ("Communicable disease ka example kya hai?",
         ["Diabetes", "Tuberculosis", "Cancer", "Scurvy"], 1),

        ("Malaria kis organism se hota hai?",
         ["Plasmodium", "Amoeba", "Bacteria", "Virus"], 0),

        ("Malaria ka carrier kaun hai?",
         ["Housefly", "Female Anopheles mosquito",
          "Cockroach", "Honeybee"], 1),

        ("Antibiotics mainly kis ke against kaam karte hain?",
         ["Bacteria", "All viruses", "Dust", "All insects"], 0),

        ("Vaccine ka main purpose kya hai?",
         ["Immunity develop karna", "Hunger badhana",
          "Digestion rokna", "Sleep badhana"], 0),

        ("Ecosystem mein producers kaun hote hain?",
         ["Green plants", "Carnivores", "Fungi only", "Humans only"], 0),

        ("Food chain mein energy ka main source kya hai?",
         ["Moon", "Sun", "Soil", "Wind"], 1),

        ("Ozone layer humein kis radiation se bachati hai?",
         ["Infrared", "Ultraviolet", "Radio waves", "Sound waves"], 1),

        ("Biodegradable waste ka example kya hai?",
         ["Plastic bottle", "Vegetable peels",
          "Glass", "Aluminium can"], 1)
    ],


    "Physics": [
        ("Force ki SI unit kya hai?",
         ["Joule", "Newton", "Watt", "Pascal"], 1),
        ("Speed ka formula kya hai?",
         ["Distance × Time", "Distance / Time",
          "Time / Distance", "Mass / Volume"], 1),
        ("Light ki speed sabse adhik kis me hoti hai?",
         ["Water", "Glass", "Vacuum", "Air"], 2),
        ("Electric current ki SI unit kya hai?",
         ["Volt", "Ampere", "Ohm", "Watt"], 1),
        ("Work ki SI unit kya hai?",
         ["Newton", "Joule", "Ampere", "Meter"], 1)
    ],

    "Chemistry": [
        ("Water ka chemical formula kya hai?",
         ["CO2", "H2O", "O2", "NaCl"], 1),
        ("Gold ka symbol kya hai?",
         ["Ag", "Go", "Au", "Gd"], 2),
        ("Atom ke nucleus me kya hota hai?",
         ["Electron", "Proton aur Neutron",
          "Sirf Electron", "Molecule"], 1),
        ("Common salt ka formula kya hai?",
         ["NaCl", "HCl", "KCl", "CaCO3"], 0),
        ("Oxygen ka atomic number kya hai?",
         ["6", "7", "8", "9"], 2)
    ]
}


class QuizApp(App):

    def build(self):
        self.main = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        self.student_name = ""
        self.roll = ""
        self.student_class = ""
        self.subject = ""

        self.score = 0
        self.q_index = 0
        self.time_left = 30
        self.timer = None
        self.selected = False

        self.show_registration()
        return self.main

    # Text label with automatic wrapping
    def make_label(self, text, size=20):
        lbl = Label(
            text=text,
            font_size=dp(size),
            color=(1, 1, 1, 1),
            halign="center",
            valign="middle",
            size_hint_y=None
        )

        def update_width(instance, width):
            instance.text_size = (width - dp(20), None)

        def update_height(instance, texture_size):
            instance.height = texture_size[1] + dp(20)

        lbl.bind(width=update_width)
        lbl.bind(texture_size=update_height)

        return lbl

    def make_button(self, text, callback):
        btn = Button(
            text=text,
            font_size=dp(18),
            size_hint_y=None,
            height=dp(50),
            background_normal="",
            background_color=(0.12, 0.42, 0.75, 1)
        )

        btn.bind(on_press=callback)
        return btn

    # Student registration
    def show_registration(self):
        self.main.clear_widgets()

        self.main.add_widget(
            self.make_label("ADVANCE SCIENCE CENTRE", 23)
        )

        self.main.add_widget(
            self.make_label("ONLINE QUIZ SYSTEM", 20)
        )

        self.name_input = TextInput(
            hint_text="Student Name",
            multiline=False,
            size_hint_y=None,
            height=dp(50),
            font_size=dp(18)
        )
        self.main.add_widget(self.name_input)

        self.roll_input = TextInput(
            hint_text="Roll Number",
            multiline=False,
            size_hint_y=None,
            height=dp(50),
            font_size=dp(18)
        )
        self.main.add_widget(self.roll_input)

        self.class_input = TextInput(
            hint_text="Class (9, 10, 11, 12)",
            multiline=False,
            size_hint_y=None,
            height=dp(50),
            font_size=dp(18)
        )
        self.main.add_widget(self.class_input)

        self.main.add_widget(
            self.make_button("Continue", self.validate_student)
        )

    def validate_student(self, instance):
        name = self.name_input.text.strip()
        roll = self.roll_input.text.strip()
        student_class = self.class_input.text.strip()

        if not name or not roll:
            self.show_message("Name aur Roll Number bhariye")
            return

        if student_class not in ["9", "10", "11", "12"]:
            self.show_message("Class 9, 10, 11 ya 12 likhiye")
            return

        self.student_name = name
        self.roll = roll
        self.student_class = student_class

        self.show_subjects()

    def show_message(self, message):
        self.main.clear_widgets()

        self.main.add_widget(self.make_label(message))

        self.main.add_widget(
            self.make_button(
                "Back",
                lambda x: self.show_registration()
            )
        )

    # Subject selection
    def show_subjects(self):
        self.main.clear_widgets()

        self.main.add_widget(
            self.make_label("Welcome " + self.student_name, 22)
        )

        self.main.add_widget(
            self.make_label("Select Your Subject", 20)
        )

        for subject in questions:
            self.main.add_widget(
                self.make_button(
                    subject,
                    lambda x, s=subject: self.start_quiz(s)
                )
            )

    # Start quiz
    def start_quiz(self, subject):
        self.subject = subject
        self.score = 0
        self.q_index = 0

        self.show_question()

    # Display question
    def show_question(self):
        if self.timer:
            self.timer.cancel()
            self.timer = None

        self.main.clear_widgets()
        self.selected = False
        self.time_left = 30

        self.main.add_widget(
            self.make_label(
                self.subject + " | Question " +
                str(self.q_index + 1),
                20
            )
        )

        self.timer_label = self.make_label("Time: 30 sec", 18)
        self.main.add_widget(self.timer_label)

        q = questions[self.subject][self.q_index]

        # Long question automatically wraps
        self.question_label = self.make_label(q[0], 20)
        self.main.add_widget(self.question_label)

        for i, option in enumerate(q[1]):
            btn = self.make_button(
                option,
                lambda x, n=i: self.check_answer(n)
            )
            self.main.add_widget(btn)

        self.timer = Clock.schedule_interval(
            self.update_timer, 1
        )

    # Timer
    def update_timer(self, dt):
        self.time_left -= 1

        self.timer_label.text = (
            "Time: " + str(self.time_left) + " sec"
        )

        if self.time_left <= 0:
            self.timer.cancel()
            self.timer = None
            self.next_question()

    # Check answer
    def check_answer(self, selected_option):
        if self.selected:
            return

        self.selected = True

        correct = questions[self.subject][self.q_index][2]

        if selected_option == correct:
            self.score += 1
            self.timer_label.text = "Correct Answer!"
        else:
            self.timer_label.text = "Wrong Answer!"

        if self.timer:
            self.timer.cancel()
            self.timer = None

        Clock.schedule_once(
            lambda dt: self.next_question(), 1
        )

    # Next question
    def next_question(self):
        if self.timer:
            self.timer.cancel()
            self.timer = None

        self.q_index += 1

        if self.q_index < len(questions[self.subject]):
            self.show_question()
        else:
            self.show_result()

    # Final result
    def show_result(self):
        self.main.clear_widgets()

        total = len(questions[self.subject])

        self.main.add_widget(
            self.make_label("QUIZ COMPLETED", 25)
        )

        self.main.add_widget(
            self.make_label("Name: " + self.student_name)
        )

        self.main.add_widget(
            self.make_label("Roll No: " + self.roll)
        )

        self.main.add_widget(
            self.make_label("Class: " + self.student_class)
        )

        self.main.add_widget(
            self.make_label("Subject: " + self.subject)
        )

        self.main.add_widget(
            self.make_label(
                "Your Score: " + str(self.score) +
                " / " + str(total),
                25
            )
        )

        percentage = (self.score / total) * 100

        self.main.add_widget(
            self.make_label(
                "Percentage: " + str(round(percentage, 2)) + "%"
            )
        )

        self.main.add_widget(
            self.make_button("Try Again", self.show_subjects)
        )

        self.main.add_widget(
            self.make_button(
                "New Student",
                self.show_registration
            )
        )


if __name__ == "__main__":
    QuizApp().run()
