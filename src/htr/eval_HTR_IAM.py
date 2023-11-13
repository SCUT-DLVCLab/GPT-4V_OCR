import edit_distance as ed


class edit_metric():
    def __init__(self):
        pass

    def cal_distance(self, label_list, pre_list):
        y = ed.SequenceMatcher(a=label_list, b=pre_list)
        yy = y.get_opcodes()
        insert = 0
        delete = 0
        replace = 0
        for item in yy:
            if item[0] == 'insert':
                insert += item[-1] - item[-2]
            if item[0] == 'delete':
                delete += item[2] - item[1]
            if item[0] == 'replace':
                replace += item[-1] - item[-2]

        distance = insert + delete + replace
        return distance

    def __call__(self, pred_list, label_list, is_CER=False):
        if is_CER:
            pred_list = [i for i in pred_list]
            label_list = [i for i in label_list]
        else:
            pred_list = pred_list.split(' ')
            label_list = label_list.split(' ')
        distance = self.cal_distance(pred_list, label_list)

        return distance


def WER_CER(li_gt, li_pred, is_CER=False):
    cal_metric = edit_metric()
    all_distance, all_len = 0, 0
    for gt, pred in zip(li_gt, li_pred):
        all_distance += cal_metric(pred, gt, is_CER)
        if is_CER:
            all_len += len(pred)
        else:
            all_len += len(gt.split(' '))
    
    return round((all_distance / all_len)*100, 2)


def main():
    all_pred, all_gt = [], [] # list of str
    # load the gt and pred in the same order

    print('WER: ', WER_CER(all_gt, all_pred, is_CER=False) )
    print('CER: ', WER_CER(all_gt, all_pred, is_CER=True) )


if __name__ == '__main__':
    main()