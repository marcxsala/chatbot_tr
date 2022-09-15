import random
from datetime import date

R_Hora = today = date.today()
print("Data actual:", today)
R_EATING = "I don't like eating cause I'm a bot!"
R_Futbol = "M'agrada molt, i soc culé"


def unknwon():
    return ["Rephrase that",
            "...",
            "Ok",
            "What does that mean?"][random.randrange(4)]
