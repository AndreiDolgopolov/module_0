#!/usr/bin/env python
# coding: utf-8

# In[69]:


import numpy as np

def game_core_v3(number):
    #Function for getting a random number equal to a given one in a minimum number of attempts
    minimum_number = 1
    maximum_number = 101
    #try number one
    count = 1
    predict = minimum_number + (maximum_number - minimum_number)//2 #We take the first number from the middle of the range
    while number != predict:
        count+=1
        if number > predict:
            minimum_number = predict + 1 #Increment to exclude unsuitable low range number 
            predict = minimum_number + (maximum_number - minimum_number)//2
        elif number < predict: 
            maximum_number = predict #The upper limit is not included
            #Optional check for debug period
            if maximum_number <= minimum_number:
                print('@Выбранное число {}, загаданное {}, макс {}, мин {}'.format(predict, number, maximum_number, minimum_number))
                return(count)
            predict = minimum_number + (maximum_number - minimum_number)//2    
    return(count) # The task is completed, the number is guessed

def score_game(game_core):
    count_ls = []
    np.random.seed(1)  # we fix RANDOM SEED so that the experiment is reproducible
    random_array = np.random.randint(1,101, size=(1000)) #do 1000 reps to get the average
    for number in random_array:
        num_ug = game_core(number)
        count_ls.append(num_ug)
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# start program
result = score_game(game_core_v3)


# In[ ]:





# In[ ]:




