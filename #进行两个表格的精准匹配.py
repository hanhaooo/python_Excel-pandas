#进行两个表格的精准匹配
import pandas as pd

#创建独立的函数，处理两个excel的数据匹配工作，输出匹配上的文件和未匹配上的数据
def match_tables(table_left,table_right,code)
    try:
        match_data = table_left.merge(table_right,on = code,how = 'left',indicator = True)
        m_table_left = table_left[match_data['_merge'] == 'left_only'].copy()
        m_table_right = table_right[match_data['_merge'] == 'right_only'].copy()
        um_mark = match_data[]
        