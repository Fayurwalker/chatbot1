import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_ACCESS = "you can get access to other departments by contacting the customer care on 1800-123-123"
R_HELP_TYPE = 'What type of help are you looking for?'
R_TROUBLESHOOT = 'What type of request would you like to raise?'




def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
