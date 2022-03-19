from aws.dynamoDB.table import create_table

if __name__ == '__main__':
    table = {
        'Attributes' : [
            {
                'AttributeName': 'face-id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'person-id',
                'AttributeType': 'S'
            },
        ],
        'Name' : 'Faces',
        'KeySchema' : [
            {
                'AttributeName' : 'face-id',
                'KeyType' : 'HASH'
            },
            {
                'AttributeName': 'person-id',
                'KeyType': 'RANGE'
            },
        ],
        'ProvisionedThroughput' : {
            'ReadCapacityUnits' : 10,
            'WriteCapacityUnits' : 10
        }
    }
    create_table(table)