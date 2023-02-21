import os
import json

def get_purchase_log():
    purchase_log = {}
    with open('./purchase_log.txt', 'r', encoding='utf-8') as purchase_fh:
        for line in purchase_fh:
            line = line.strip()

            dict = json.loads(line)
            purchase_log[dict['user_id']] = dict['category']

    return purchase_log

def main():
    purchase_log = get_purchase_log()

    if os.path.isfile('./funnel.csv'):
        os.remove('./funnel.csv')
    funnel_fh = open('./funnel.csv', 'w', encoding='utf-8')
    funnel_fh.writelines('user_id,source,category\n')

    with open('./visit_log.csv', 'r', encoding='utf-8') as f:
        f.readline()

        for line in f:
            line = line.strip()
            string_parts = line.split(",")
            user_id = string_parts[0]
            source = string_parts[1]

            if user_id in purchase_log:
                funnel_fh.writelines([f'{user_id},{source},{purchase_log[user_id]}\n'])
            else:
                continue

        funnel_fh.close()

if __name__ == '__main__':
    main()
