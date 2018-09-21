import pandas as pd
from openpyxl import load_workbook


"""
padas dataframe创建新的excel
"""
def dataFrame2sheet(dataframe,excelWriter,sheet_name):

   # DataFrame转换成excel中的sheet表
   dataframe.to_excel(excel_writer=excelWriter, sheet_name=sheet_name,index=None)

   excelWriter.save()
   excelWriter.close()

"""
excel中新增sheet表
"""
def excelAddSheet(dataframe, excelWriter, sheet_name):

   book = load_workbook(excelWriter.path)
   excelWriter.book = book
   dataframe.to_excel(excel_writer=excelWriter,sheet_name=sheet_name,index=None)
   excelWriter.close()

# 将一个手机号下的所有sn都统计出来，并存到一个新的sheet中
def excelAddPhoneSn(df, phone):
    # 筛选df中的内容，'13970004878'
    df_moblie = df.loc[df['mobile (franchisee)']== phone]

    #创建ExcelWriter 对象
    excelWriter=pd.ExcelWriter('/Users/lgy/Desktop/'+'加盟商sn.xlsx',engine='openpyxl')

    # 在一个excel中新增一个sheet
    excelAddSheet(df_moblie,excelWriter,sheet_name=str(phone))

    print("存入成功")


if __name__ == '__main__':

    # 把from列和to列都转换为str类型
    # converters={'from':str,'to':str}

    # 确认excel文件的路径
    excel_file_path = '/Users/lgy/Desktop/'+'加盟商sn原始数据.xlsx'

    # 读取excel文件，并存入df
    df = pd.DataFrame(pd.read_excel(excel_file_path))

    # 将一个手机号下的所有sn都存入新的sheet中
    excelAddPhoneSn(df,13970004878)




    """其他一些常用的功能"""

    # 查看df中某一个'列'的所有内容(字典)
    df_phone = df[['mobile (franchisee)','加盟商']]

    # 罗列df中某一个'列'的所有选项
    pmList = df[['mobile (franchisee)']].values.T.tolist()[:][0]

    # 排除重复的直
    pmList_no_repeat = list(set(pmList))

    # 筛选df中的内容，'13970004878'
    df_13970004878 = df.loc[df['mobile (franchisee)']==13970004878]

    # 多重筛选条件
    # df_13970004878 = df.loc[df['加盟商'] == "徐徐"].loc[df['mobile'] == 13970004878]

    # 创建一个新的excel
    # dataFrame2sheet(df_13970004878,excelWriter,sheet_name='13970004878')



