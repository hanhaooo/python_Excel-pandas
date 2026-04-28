#对比表格中某一列的数据，筛出重复值与非重复值
import pandas as pd

#对表格中某一列数据(code01)进行查重，并将该表格拆分成重复数据表格及非重复数据表格
def sheet_clear_dup(code,sheet):
    try:
        if sheet[code].duplicated().any():                          #当存在重复值时进行执行
            sheet_mask = sheet[code].duplicated(keep = False)   #所有重复行标记为True
            sheet_dup = sheet[sheet_mask].copy()                #筛选出重复行
            sheet_clear = sheet[~sheet_mask].copy()             #筛选出非重复行
            print("已完成数据分离,验证sheet_clear是否有重复值：",sheet_clear.duplicated().any())
            return sheet_dup,sheet_clear
        else:
             print(f"该sheet的'{code}'列无重复数据")
             return pd.DataFrame(),sheet.copy()
    except Exception as e:
        print(f'发生意外错误，请重新检查文件:{e}')
        return None,None
    
    
            

         

