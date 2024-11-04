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

def observed_items():
    observations = []
    for i in range(7):
        obs = input("please enter an observation: ")
        observations.append(obs)
    return observations


def run_task2():
    print("counting observations...")
    observations = observed_items()
    obs_count = set()
    for observation in observations:
        count = observation, observations.count(observation)
        obs_count.add(count)
    print(obs_count)

if __name__ == '__main__':
    run_task2()


