#进行两个表格的精准匹配
import pandas as pd

#创建独立的函数，处理两个excel的数据匹配工作，输出匹配上的文件和未匹配上的数据
def match_tables(table_left,table_right,code):
    try:
        if code not in table_left.columns or code not in table_right.columns:
            raise KeyError(f"列'{code}'不存在于其中任何一个表")
        match_data = table_left.merge(table_right,on = code,how = 'outer',indicator = True)
        m_table = match_data[match_data['_merge'] == "both"].copy()
        um_table_left = match_data[match_data['_merge'] == "left_only"].copy()
        um_table_right = match_data[match_data['_merge'] == "right_only"].copy()
        return m_table,um_table_left,um_table_right
    except Exception as e:
        print(f'出现错误:{e}')
        return None,None,None
    
file1 = pd.read_excel(r"c:\Users\hanfu\Desktop\practice\数据源\班级人员.xlsx")
file2 = pd.read_excel(r"c:\Users\hanfu\Desktop\practice\数据源\班级人员匹配.xlsx")
code = '学号'
m_file,um01,um02 = match_tables(file1,file2,code)
print(m_file,"\n")
print(um01)

