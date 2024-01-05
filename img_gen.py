from os import system,listdir

cookie = "1iIUOVB-hUwj4v1nrdVhJfSEUX_BXtJWuHiFsKcrQ_19NxGGw4x5iAPn1CH0Rj2b4ZudUggWjO8RjcstN_a8cFx_H7-qN4FAZlucigtP9LhK6DVfMnzn_Co2yZHHhA9FxrQR8YWuQEhuUa7izeRJgmWnr8VszHDzaB1yFgo2SjbTfJiraZYET7KknAp3T3TaNGsk08h1UCFt2F6I_szBQJGO--iQPJPcqmLtcqXlwy2U"

def generate_image(prompt):
    system(f'python -m BingImageCreator --prompt "{prompt}" -U "{cookie}"')
    return listdir('output')