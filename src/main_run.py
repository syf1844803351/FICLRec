import os

dataset = ["Sports_and_Outdoors_low","Sports_and_Outdoors_high","Sports_and_Outdoors_mid"]
#dataset = ["Beauty","Sports_and_Outdoors","Toys_and_Games","ml-1m","Yelp"]
c = [1024]
for d in c:
    os.system("python main.py --data_name Yelp --rec_weight 1. --alpha 0.1 --beta 0.1 --f_neg --intent_num 256 "
              "--hidden_dropout_prob 0.5 --attention_probs_dropout_prob 0.5 --weight_decay 1e-5 --p 13".format(
        d,
    ))

