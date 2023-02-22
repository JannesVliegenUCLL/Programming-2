# Write your code here
from textwrap import dedent
def generate_git_script(id):
    string = f'''
    if [ ! -d {id} ]; then
        git clone https://github.com/{id}/project {id}
    else
        (cd {id}; git pull)
    fi
    '''
    print(string.strip())

generate_git_script(7)
