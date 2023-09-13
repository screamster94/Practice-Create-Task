engine_list = ["Stirling Single", "Flying Scotsman", "Mallard", "Ivat Class D1" , "Ivat Class C1", "Ivatt Class C2"]

new_engine = input("What engine would you like to add to the list?")

def rank_engine(new_engine, engine_list):

    for i in range(len(engine_list)):

        rank = input("Do you like A)" + new_engine + " more or B)" + engine_list[i] + "more? A/B")

        if rank == "A":
            engine_list.insert(i, new_engine)
            return engine_list

        elif rank =="B":
           continue

    engine_list.append(new_engine)
    return engine_list

print("Your new ranking of engines is", rank_engine(new_engine, engine_list))