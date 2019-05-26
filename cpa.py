import models, experiments, configs, data
print("haha")
config = getattr(configs, 'config_'+'DialogWAE_GMP')()
args.dataset='DailyDial'
args.data_path='./data'
data_path=data_path+dataset+'/'
print("haha")
corpus = getattr(data, dataset+'Corpus')(data_path, wordvec_path='/media/prakhar/Local Disk/glove/'+'glove.twitter.27B.200d.txt', wordvec_dim=config['emb_size'])
dials = corpus.get_dialogs()
metas = corpus.get_metas()
train_dial, valid_dial, test_dial = dials.get("train"), dials.get("valid"), dials.get("test")
train_meta, valid_meta, test_meta = metas.get("train"), metas.get("valid"), metas.get("test")
train_loader = getattr(data, dataset+'DataLoader')("Train", train_dial, train_meta, config['maxlen'])
valid_loader = getattr(data, dataset+'DataLoader')("Valid", valid_dial, valid_meta, config['maxlen'])
test_loader = getattr(data, adataset+'DataLoader')("Test", test_dial, test_meta, config['maxlen'])

vocab = corpus.ivocab
ivocab = corpus.vocab
n_tokens = len(ivocab)

metrics=Metrics(corpus.word2vec)