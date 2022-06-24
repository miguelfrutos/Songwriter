#pip install gpt_2_simple
import gpt_2_simple as gpt2
import configparser

# Download the small version of GPT2
gpt2.download_gpt2(model_name='124M')

# Prepare the train_set
file_name = 'train_dataset.txt'

# Finetune the model
sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              dataset=file_name,
              model_name='124M',
              steps=20,
              restore_from='fresh',
              run_name='run1',
              print_every=10,
              sample_every=20,
              )

# Envionment Variables with ConfigParser to include the starting point
cfg = configparser.ConfigParser()
cfg.read('user.ini')
input_lyrics=cfg.get('INPUTS','input_lyrics')

# run_test with some parameters
gpt2.generate(sess,
              length=250,
              temperature=0.7,
              prefix=input_lyrics,
              nsamples=5,
              top_k=40)
