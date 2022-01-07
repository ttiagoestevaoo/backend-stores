
def test_read_main():

    with open('CNAB.txt') as file:
        for line in file.readlines():
            tipo  = line[0:1]
            created_at = line[1:9]
            value = line[9:19]
            cpf= line[19:30]
            card= line[30:42]
            time_at= line[42:48]
            owner= line[48:62]
            store= line[62:81]

    assert {} == {"msg": "Hello World"}
 