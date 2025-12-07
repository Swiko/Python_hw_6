import json

purchases = {}
with open('purchase_log.txt', 'r', encoding='utf-8') as purchase_file:
    for line in purchase_file:
        data = json.loads(line.strip())
        purchases[data['user_id']] = data['category']

with open('visit_log__1_.csv', 'r', encoding='utf-8') as visit_file, \
     open('funnel.csv', 'w', encoding='utf-8', newline='') as funnel_file:

    funnel_file.write('user_id,source,category\n')

    for line in visit_file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(',')
        if len(parts) < 2:
            continue

        user_id = parts[0]
        source = parts[1]

        category = purchases.get(user_id)
        if category:
            funnel_file.write(f'{user_id},{source},{category}\n')
