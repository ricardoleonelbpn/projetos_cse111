try:
        print(20*"-" + " Pesquisa de Satisfação " + 20*"-")
        print()
        nota = int(input("De 1 a 5, qual nota você daria para nosso atendimento? "))
        

        if nota == 5:
            print("Obrigado! Ficamos felizes que você teve uma ótima experiência.")
            input("\nGostaria de deixar seu feedback? ")
            print("Obrigado pelo seu feedback!")
        elif nota == 4:
            print("Obrigado! Ficamos felizes que você teve uma boa experiência.")
            input("\nGostaria de deixar seu feedback? ")
            print("Obrigado pelo seu feedback!")
        elif nota == 3:
            print("Agradecemos sua avaliação. Vamos trabalhar para melhorar e atigir nota 5.")
            input("\nGostaria de deixar sua sugestão? ")
            print("Obrigado pelo seu feedback!")
        elif nota == 2:
            print("Agradecemos sua avaliação. Vamos trabalhar para melhorar e atigir nota 5.")
            input("\nGostaria de deixar sua sugestão? ")
            print("Obrigado pelo seu feedback!")
        elif nota == 1:
            print("Agradecemos sua avaliação. Vamos trabalhar para melhorar e atigir nota 5.")
            input("\nGostaria de deixar sua sugestão? ")
            print("Obrigado pelo seu feedback!")
    #except 
