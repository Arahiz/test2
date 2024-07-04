def fill_values(values, tests):
    def fill_id_value(tests, _id, value):
        if fill_id_value.flag:
            return
        for elem in tests:
            if elem['id'] == _id:
                elem['value'] = value
                fill_id_value.flag = 1
                return
            elif 'values' in elem:
                fill_id_value(elem['values'], _id, value)
    for obj in values['values']:
        fill_id_value.flag = 0
        _id, value = obj['id'], obj['value']
        fill_id_value(tests['tests'], _id, value)


if __name__ == '__main__':
    import json
    import sys

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    with open(values_file) as v, open(tests_file) as t:
        values = json.load(v)
        tests = json.load(t)

    fill_values(values, tests)
    with open(report_file, 'w') as report:
        json.dump(tests, report, indent=4)
