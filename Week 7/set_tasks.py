##Task 1

# def observed():
#     observations = {"car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
#     return observations
#
# def run_task1():
#     print(observed())
#
# run_task1()

##Task 2

# def observed_items():
#     observations = []
#     for i in range(7):
#         obs = input("please enter an observation: ")
#         observations.append(obs)
#     return observations
#
#
# def run_task2():
#     print("counting observations...")
#     observations = observed_items()
#     obs_count = set()
#     for observation in observations:
#         count = observation, observations.count(observation)
#         obs_count.add(count)
#     print(obs_count)
#
# if __name__ == '__main__':
#     run_task2()
#

## Task 2

def observed_items():
    observations = []
    for i in range(5):
        obs = input("please enter an observation")
        observations.append(obs)
    return observations

def remove_observations(x):
    count = input("do you want to remove any observations?")
    truefalse = True
    if count == "yes":
        while truefalse:
            remove_item = input("what observation do you wish to remove")
            x.remove(remove_item)
            print("Done!")
            re_do = input("do you want to remove any more observations?")
            if re_do == "yes":
                truefalse = True
            else:
                truefalse = False
                return x
    else:
        return x

def run_task3():
    observations = observed_items()
    remove_observations(observations)
    print(observations)

if __name__ == '__main__':
    run_task3()









