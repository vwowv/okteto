#coding:utf-8
import yaml
import random

def change(files):
        content = open(files, 'r', encoding="utf-8")
        file_data = content.read()
        content.close()
        all_data = yaml.full_load_all(file_data)
        file = open(files, 'w', encoding='utf-8')   
        for data in all_data:
            num = random.randint(100, 10000);
            file.write("---\n")
            data['metadata']['labels']['testc'] = 'host{}'.format(num)
            yaml.dump(data, file)
            print('成功')      
        file.close()

if __name__ == '__main__':
    change('baota.yml') 