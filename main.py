from pymapper import Mapper

mapper = Mapper({
    'dest_1': {
        'dest_2': '$source_1.source_2'
    },
    'dest_2': '$source_1.source_3.source_4'
})

result = mapper.map([
    {
        'source_1': {
            'source_2': [1, 2, 3],
            'source_3': {
                'source_4': 5
            }
        }
    },
    {
        'source_1': {
            'source_2': [4, 5, 6],
            'source_3': {
                'source_4': 7
            }
        }
    }
])
# re
print(result)
