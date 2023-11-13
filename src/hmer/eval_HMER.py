import edit_distance as ed
import re


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
        distance = delete + replace + insert
        return distance

    def __call__(self, pred_list, label_list):
        distance = self.cal_distance(pred_list, label_list)

        return distance


def acc(li_gt, li_pred, dist=0):
    cal_metric = edit_metric()
    cor = 0
    for gt, pred in zip(li_gt, li_pred):
        pred = split_token(pred)
        gt = gt.split(' ')
        edis = cal_metric(pred, gt)
        if edis <= dist:
            cor += 1

    return cor / len(li_gt)


def split_token(pred):
    li = [r'\\leftrightarrow', r'\\rightarrow', r'\\varepsilon', r'\\mathrm', 
    r'\\propto', r'\\mathbb', r'\\lambda', r'\\times', r'\\ldots', r'\\right', 
    r'\\infty', r'\\angle', r'\\frac', r'\\sqrt', r'\\left', r'\\text', r'\\beta',
    r'\\quad', r'\\circ', r'\\cdot', r'\\sum', r'\\lim', r'\\int', 
    r'\\leq', r'\\log', r'\\tan', r'\\sin', r'\\cos', r'\\geq', 
    r'\\rho', r'\\neq', r'\\div', r'\\to', r'\\pi']

    tokens = re.findall(r"|".join(li) + r"|\S", pred)

    return tokens


def main():
    all_pred, all_gt = [], [] # list of str
    # load the gt and pred in the same order

    print('exp_rate0', acc(all_gt, all_pred, dist=0))
    print('exp_rate1', acc(all_gt, all_pred, dist=1))
    print('exp_rate2', acc(all_gt, all_pred, dist=2))
    print('exp_rate3', acc(all_gt, all_pred, dist=3))

if __name__ == '__main__':
    main()