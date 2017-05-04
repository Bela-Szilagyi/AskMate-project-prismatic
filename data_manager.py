import base64
import time
import datetime

# read file into a @table
#
# @file_name: string
# @table: list of lists of strings
def get_table_from_file(file_name, indices):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(",") for element in lines]
    table = base64_decoder(table, indices)
    table = get_timeform_from_stamp(table)
    return table


# write a @table into a file
#
# @file_name: string
# @table: list of lists of strings
def write_table_to_file(file_name, table, indices):
    table = base64_coder(table, indices)
    with open(file_name, "w") as file:
        for record in table:
            row = ','.join(record)
            file.write(row + "\n")


def base64_decoder(table, indices):
    for row in table:
        for i in indices:
            row[i] = str(base64.b64decode(row[i]).decode("utf-8"))
    return table


def base64_coder(table, indices):
    for row in table:
        for i in indices:
            row[i] = base64.b64encode(bytes(row[i],"utf-8")).decode("utf-8")  # str(base64.encodebytes(bytearray(row[i].encode()))) 
    return table


def table_sort(table, sort_key_number, rev_boolean):
    table = sorted(table, key=lambda table: table[sort_key_number], reverse=rev_boolean)
    return table


def get_time_stamp():
    # print(str(int(time.time()))) 
    return str(int(time.time()))


def get_timeform_from_stamp(table):
    for row in table:
        row[1] = datetime.datetime.fromtimestamp(int(row[1])).strftime('%Y-%m-%d %H:%M:%S')
    return table


def get_timeform_to_stamp(table):
    for row in table:
        row[1] = str(int(datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S').strftime("%s")))
    return table


def add_item_to_table(table, request):
    max_id = 0
    if len(table) > 0:
        max_id = max(int(i[0]) for i in table)
    table.append([str(max_id+1),
                 get_time_stamp(),
                 '0',
                 '0',
                 request['new_question_title'],
                 request['new_question_message'],
                 ''])
    return table


def add_item_to_answer_table(table, request):
    max_id = 0
    if len(table) > 0:
        max_id = max(int(i[0]) for i in table)
    table.append([str(max_id+1),
                 get_time_stamp(),
                 '0',
                 request['question_id'],
                 request['new_answer_message'],
                 ''])
    return table


