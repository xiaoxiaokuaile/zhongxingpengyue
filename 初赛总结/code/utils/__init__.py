class AverageMeter(object):
    """Computes and stores the average and current value"""
    def __init__(self):
        self.val = 0
        self.reset()

    def reset(self):
        self.avg = 0
        self.sum = 0
        self.count = 0

    def add(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count