# FICLRec

This is our Pytorch implementation for the paper: "**FICLRec: Frequency Enhanced Intent Contrastive Learning for Sequential Recommendation**".

## Environment  Requirement

* Pytorch>=1.11.0
* Python>=3.7  

## Usage

Please run the following command to install all the requirements:  

```python
pip install -r requirements.txt
```

## Evaluate Model

We provide the trained models on Beauty, Sports_and_Outdoors, Toys_and_Games and ML-1M datasets in `./src/output/<Data_name>`folder. You can directly evaluate the trained models on test set by running:

```
python main.py --data_name <Data_name> --model_idx 0 --p <p> --do_eval
```

On Beauty:

```python
python main.py --data_name Beauty --model_idx 0 --p 13 --do_eval
```

```
{'Epoch': 0, 'HIT@5': '0.0724', 'NDCG@5': '0.0516', 'HIT@10': '0.1007', 'NDCG@10': '0.0606', 'HIT@20': '0.1390', 'NDCG@20': '0.0703'}
```

On Sports_and_Outdoors:

```python
python main.py --data_name Sports_and_Outdoors --model_idx 0 --p 7 --do_eval
```

```
{'Epoch': 0, 'HIT@5': '0.0438', 'NDCG@5': '0.0300', 'HIT@10': '0.0623', 'NDCG@10': '0.0359', 'HIT@20': '0.0885', 'NDCG@20': '0.0425'}
```

On Toys_and_Games:

```python
python main.py --data_name Toys_and_Games --model_idx 0 --p 7 --do_eval 
```

```
{'Epoch': 0, 'HIT@5': '0.0820', 'NDCG@5': '0.0591', 'HIT@10': '0.1092', 'NDCG@10': '0.0679', 'HIT@20': '0.1471', 'NDCG@20': '0.0774'}
```


On Yelp:

```python
python main.py --data_name Yelp --model_idx 0 --p 13 --do_eval 
```

```
{'Epoch': 0, 'HIT@5': '0.0319', 'NDCG@5': '0.0201', 'HIT@10': '0.0521', 'NDCG@10': '0.0266', 'HIT@20': '0.0826', 'NDCG@20': '0.0342'}
```


On LastFM:

```python
python main.py --data_name LastFM --model_idx 0 --p 5 --do_eval
```

```
{'Epoch': 0, 'HIT@5': '0.0569', 'NDCG@5': '0.0413', 'HIT@10': '0.0853', 'NDCG@10': '0.0503', 'HIT@20': '0.1211', 'NDCG@20': '0.0594'}
```


## Train Model

Please train the model using the Python script `main.py`.

You can run the following command to train the model on Beauty datasets:

```
python main.py --data_name Beauty --rec_weight 1. --alpha 0.1 --beta 0.1 --f_neg --intent_num 1024 --hidden_dropout_prob 0.5 --attention_probs_dropout_prob 0.5 --p 13
```
or

You can use the training scripts in the `./src/scrips` folder to train the model 
```angular2html
bash beauty.sh
bash sports.sh
bash toys.sh
bash Yelp.sh
bash LastFM.sh
```
## Acknowledgment

- Transformer and training pipeline are implemented based on [ICSRec](https://github.com/qinhsiu/icsrec) and [BSARec](https://github.com/yehjin-shin/BSARec). Thanks them for providing efficient implementation.



