import pandas as pd
import chardet

from config import DATA_DIR, create_mysql_engine

# ==========================================
# 配置
# ==========================================

CSV_PATH = DATA_DIR / "train.csv"

# ==========================================
# 自动检测编码
# ==========================================

with open(CSV_PATH, "rb") as f:
    result = chardet.detect(f.read())

encoding = result["encoding"]

print("=" * 60)
print("CSV编码：", encoding)
print("=" * 60)

# ==========================================
# 读取CSV
# 不做任何日期转换
# 不删除任何数据
# ==========================================

df = pd.read_csv(
    CSV_PATH,
    encoding=encoding,
    low_memory=False
)

print("\n========== CSV读取成功 ==========")
print("数据规模：", df.shape)

print("\n字段：")
print(df.columns.tolist())

print("\n前5行：")
print(df.head())

# 去掉字段前后空格

df.columns = df.columns.str.strip()

# ==========================================
# 查看缺失值
# ==========================================

print("\n========== 缺失值 ==========")
print(df.isnull().sum())

# ==========================================
# 创建MySQL连接
# ==========================================

engine = create_mysql_engine()

print("\nMySQL连接成功！")

# ==========================================
# 导入数据库
# replace表示覆盖旧表
# ==========================================

print("\n开始导入MySQL，请稍等...")

df.to_sql(
    name="orders",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=1000,
    method="multi"
)

print("\n========== 导入完成 ==========")

# ==========================================
# 验证导入结果
# ==========================================

count = pd.read_sql(
    "SELECT COUNT(*) AS total FROM orders",
    engine
)

print("\n数据库数据量：")
print(count)

print("\n数据库前5条：")

print(
    pd.read_sql(
        "SELECT * FROM orders LIMIT 5",
        engine
    )
)

print("\n==============================")
print("CSV行数：", len(df))
print("数据库行数：", count.iloc[0, 0])

if len(df) == count.iloc[0, 0]:
    print("\n★★★★★ 数据导入成功（100%一致）★★★★★")
else:
    print("\n★★★★★ 数据导入失败，请检查！★★★★★")

print("==============================")
