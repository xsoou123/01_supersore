import pandas as pd

from config import DATA_DIR, create_mysql_engine

OUTPUT_PATH = DATA_DIR / "clean_superstore.csv"

# ==========================================
# 连接数据库
# ==========================================

def connect_mysql():
    engine = create_mysql_engine()
    print("=" * 60)
    print("MySQL连接成功")
    print("=" * 60)
    return engine


# ==========================================
# 读取数据
# ==========================================

def load_data(engine):
    df = pd.read_sql("SELECT * FROM orders", engine)

    print("\n========== 数据读取成功 ==========")
    print(f"数据规模：{df.shape[0]} 行 × {df.shape[1]} 列")

    return df


# ==========================================
# 数据概览
# ==========================================

def data_overview(df):

    print("\n========== 前5行 ==========")
    print(df.head())

    print("\n========== 数据类型 ==========")
    print(df.info())

    print("\n========== 描述统计 ==========")
    print(df.describe(include="all"))

    print("\n========== 缺失值 ==========")
    print(df.isnull().sum())

    print("\n========== 重复值 ==========")
    print(df.duplicated().sum())


# ==========================================
# 数据清洗
# ==========================================

def clean_data(df):

    df.columns = df.columns.str.strip()

    print("\n数据清洗完成（未删除任何数据）")

    return df


# ==========================================
# 销售分析
# ==========================================

def sales_analysis(df):

    print("\n========== 销售分析 ==========")

    print(f"总销售额：{df['Sales'].sum():,.2f}")
    print(f"平均销售额：{df['Sales'].mean():,.2f}")
    print(f"最大销售额：{df['Sales'].max():,.2f}")
    print(f"最小销售额：{df['Sales'].min():,.2f}")
    print(f"中位数：{df['Sales'].median():,.2f}")
    print(f"标准差：{df['Sales'].std():,.2f}")


# ==========================================
# 品类分析
# ==========================================

def category_analysis(df):

    print("\n========== 品类销售 ==========")

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print(category_sales)

    print(f"\n销售额最高品类：{category_sales.idxmax()}")

    return category_sales


# ==========================================
# 区域分析
# ==========================================

def region_analysis(df):

    print("\n========== 区域销售 ==========")

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print(region_sales)

    print(f"\n销售额最高区域：{region_sales.idxmax()}")

    return region_sales


# ==========================================
# 客户类型分析
# ==========================================

def segment_analysis(df):

    print("\n========== 客户类型 ==========")

    segment_sales = (
        df.groupby("Segment")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print(segment_sales)

    return segment_sales


# ==========================================
# Top10商品
# ==========================================

def top_products(df):

    print("\n========== Top10商品 ==========")

    top10 = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print(top10)

    return top10


# ==========================================
# 保存数据
# ==========================================

def export_data(df):

    df.to_csv(
        OUTPUT_PATH,
        index=False,
        encoding="utf-8-sig"
    )

    print("\n清洗后的数据已保存：")
    print(OUTPUT_PATH)


# ==========================================
# 主程序
# ==========================================

def main():

    engine = connect_mysql()

    df = load_data(engine)

    data_overview(df)

    df = clean_data(df)

    category_sales = category_analysis(df)

    region_sales = region_analysis(df)

    segment_sales = segment_analysis(df)

    top10 = top_products(df)

    sales_analysis(df)

    export_data(df)

    print("\n" + "=" * 60)
    print("EDA 第一阶段完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
