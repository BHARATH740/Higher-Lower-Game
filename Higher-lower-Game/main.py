from art import logo, vs
from game_data import data
import random


is_crt = True
final_score = 0
print(logo)
print("\n")
while is_crt:
    is_def = False
    if not is_def :
        A=data[random.randint(0,len(data))]
        B=data[random.randint(0,len(data))] 
    else :
        B=data[random.randint(0,len(data))] 
    while A==B:
        B=data[random.randint(0,len(data))]
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(vs)
    print("\n")
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    crt_ans = 'A' if A["follower_count"] > B["follower_count"] else 'B'
    print(crt_ans)
    ans = input(f"Who has more followers? Type 'A' or 'B': ")
    if crt_ans != ans:
        print(f"Sorry, that's wrong. Final score : {final_score}")
        is_crt = False
        break
    else :
        A = A if crt_ans == 'A' else B
        final_score +=1
        print(f"You're right! Current Score: {final_score}")
            
        
    


input()