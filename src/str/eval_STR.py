

def word_acc(all_pred, all_gt):
    cor = 0
    for pred, gt in zip(all_pred, all_gt):
        gt = gt.upper()
        pred = pred.upper()

        for c in gt:
            if c not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
                gt = gt.replace(c, '')
        for c in pred:
            if c not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
                pred = pred.replace(c, '')

        if gt == pred:
            cor += 1

    return round(cor*100 / len(all_gt), 2)


def main():
    all_pred, all_gt = [], [] # list of str
    # load the gt and pred in the same order

    print('WAICS: ', word_acc(all_pred, all_gt))



if __name__ == '__main__':
    main()