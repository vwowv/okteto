#coding:utf-8
import yaml
import random

def up_yml(ip_server):
        content = open('/home/runner/work/okteto/okteto/google-mirror.yml', 'r', encoding="utf-8")
        file_data = content.read()
        content.close()
        all_data = yaml.load_all(file_data)
        file = open('/home/runner/work/okteto/okteto/google-mirror.yml', 'w', encoding='utf-8')

        for data in all_data:
            num = random.randint(100, 10000);
            file.write("---\n")
            data['metadata']['labels']['testc'] = 'host{}'.format(num)
            yaml.dump(data, file)
            print(data)
        file.close()

if __name__ == '__main__':
    up_yml(ip_server='0.0.0.0')
