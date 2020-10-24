#coding:utf-8
import yaml
import random

def up_yml():
        content1 = open('baota.yml', 'r', encoding="utf-8")
        file_data1 = content1.read()
        content1.close()
        all_data = yaml.full_load_all(file_data1)
        file1 = open('baota.yml', 'w', encoding='utf-8')

        for data in all_data:
            num = random.randint(100, 10000);
            file1.write("---\n")
            data['metadata']['labels']['testc'] = 'host{}'.format(num)
            yaml.dump(data, file1)
            print('成功')
        file1.close()

if __name__ == '__main__':
    up_yml()
