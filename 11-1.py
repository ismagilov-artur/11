word = """С дичью дело, мы полагаем, закончено. Глава предприятия Хадсон, по сведениям, рассказал о мухобойках все. 
    Фазаньих курочек берегитесь """.split()

spisok = [word[i] for i in range(2, len(word), 3)]
print(' '.join(spisok))
