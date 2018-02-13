import seq2seq

LEARNERS = {c.__name__: c for c in [
    seq2seq.SimpleSeq2SeqLearner,
]}


def new(classname):
    return LEARNERS[classname]()
