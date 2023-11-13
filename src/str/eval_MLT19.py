

def precision(pred_li, gt_li):
    cor, tol = 0, 0
    for gt, pred in zip(pred_li, gt_li):
        for i in pred:
            if i in gt:
                cor += 1
        tol += len(pred)

    return cor / tol * 100


def recall(pred_li, gt_li):
    cor, tol = 0, 0
    for gt, pred in zip(pred_li, gt_li):
        for i in gt:
            if i in pred:
                cor += 1
        tol += len(gt)
    return cor / tol * 100



def main():
    all_pred, all_gt = [], [] # list of str
    # load the gt and pred in the same order

    p = precision(all_pred, all_gt)
    r = recall(all_pred, all_gt)
    f1 = 2 * p * r / (p + r)
    f1 = round(f1, 2)
    print('Precision:', p, 'Recall:', r, 'F1score:', f1)


if __name__ == '__main__':
    main()