class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# List of questions
questions = [
    # Football questions
    Question("Who won the FIFA World Cup in 2018?\n(a) Brazil\n(b) Germany\n(c) France\n", "c"),
    Question("Which player has won the most Ballon d'Or awards?\n(a) Cristiano Ronaldo\n(b) Lionel Messi\n(c) Neymar\n", "b"),
    Question("Which country has won the most UEFA European Championship titles?\n(a) Spain\n(b) Germany\n(c) Italy\n", "a"),
    
    # Software questions
    Question("Who created the Python programming language?\n(a) Guido van Rossum\n(b) Larry Page\n(c) Mark Zuckerberg\n", "a"),
    Question("Which company developed the Android operating system?\n(a) Apple\n(b) Google\n(c) Microsoft\n", "b"),
    Question("What does HTML stand for?\n(a) Hyper Text Markup Language\n(b) High Tech Multi Language\n(c) Home Tool Markup Language\n", "a"),
    
    # Music questions
    Question("Who is known as the 'King of Pop'?\n(a) Michael Jackson\n(b) Elvis Presley\n(c) Madonna\n", "a"),
    Question("Which band released the album 'Abbey Road'?\n(a) The Beatles\n(b) The Rolling Stones\n(c) Led Zeppelin\n", "a"),
    Question("Which artist has won the most Grammy Awards?\n(a) Beyoncé\n(b) Jay-Z\n(c) Taylor Swift\n", "a"),
    
    # Liverpool FC questions
    Question("Which player has the most appearances for Liverpool FC?\n(a) Steven Gerrard\n(b) Jamie Carragher\n(c) Ian Rush\n", "a"),
    Question("Who is Liverpool FC's all-time top goalscorer?\n(a) Mohamed Salah\n(b) Kenny Dalglish\n(c) Ian Rush\n", "c"),
    Question("Who is the current manager of Liverpool FC?\n(a) Jurgen Klopp\n(b) Pep Guardiola\n(c) Jose Mourinho\n", "a"),
    
    # Additional miscellaneous questions
    Question("What is the capital of Japan?\n(a) Tokyo\n(b) Beijing\n(c) Seoul\n", "a"),
    Question("Which planet is known as the 'Red Planet'?\n(a) Mars\n(b) Jupiter\n(c) Saturn\n", "a"),
    Question("Who wrote the play 'Romeo and Juliet'?\n(a) William Shakespeare\n(b) Charles Dickens\n(c) Jane Austen\n", "a"),
    Question("What is the chemical symbol for water?\n(a) Wo\n(b) Wa\n(c) H2O\n", "c"),
    Question("Which is the largest ocean on Earth?\n(a) Pacific Ocean\n(b) Atlantic Ocean\n(c) Indian Ocean\n", "a"),
    Question("Who painted the Mona Lisa?\n(a) Leonardo da Vinci\n(b) Vincent van Gogh\n(c) Pablo Picasso\n", "a"),
    # Add more questions as needed
]
