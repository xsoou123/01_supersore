# ==========================================================
# Superstore Data Visualization
# Author: Hongyang Song
# ==========================================================

import os
import warnings
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from config import IMAGE_DIR, create_mysql_engine

warnings.filterwarnings("ignore")

# ==========================================================
# Matplotlib 全局设置
# ==========================================================

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.size"] = 11

# ==========================================================
# Tableau 商务配色
# ==========================================================

COLORS = {
    "blue": "#4E79A7",
    "orange": "#F28E2B",
    "green": "#59A14F",
    "red": "#E15759",
    "purple": "#B07AA1",
    "cyan": "#76B7B2",
    "yellow": "#EDC948",
    "gray": "#BAB0AC"
}

# ==========================================================
# 图片保存路径
# ==========================================================

IMAGE_PATH = IMAGE_DIR

os.makedirs(IMAGE_PATH, exist_ok=True)

# ==========================================================
# MySQL连接
# ==========================================================

engine = create_mysql_engine()

print("=" * 60)
print("读取MySQL数据...")
print("=" * 60)

df = pd.read_sql("SELECT * FROM orders", engine)

print("数据规模：", df.shape)

# ==========================================================
# 日期转换
# ==========================================================

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce",
    format="mixed"
)

# ==========================================================
# Y轴格式化
# ==========================================================

def money(x, pos):
    if x >= 1000000:
        return f"${x/1000000:.1f}M"
    elif x >= 1000:
        return f"${x/1000:.0f}K"
    return f"${x:.0f}"

# ==========================================================
# 月销售趋势
# ==========================================================

monthly = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
      .sum()
)

monthly.index = monthly.index.astype(str)

fig, ax = plt.subplots(figsize=(13,6))

ax.plot(
    monthly.index,
    monthly.values,
    color=COLORS["blue"],
    linewidth=3,
    marker="o",
    markersize=7
)

# 去除顶部右侧边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 网格
ax.grid(
    linestyle="--",
    alpha=0.3
)

# 标题
ax.set_title(
    "Monthly Sales Trend",
    fontsize=18,
    fontweight="bold",
    pad=15
)

ax.set_xlabel("Month")
ax.set_ylabel("Sales")

# 数值格式
ax.yaxis.set_major_formatter(
    FuncFormatter(money)
)

plt.xticks(rotation=45)

# 添加最后一个点的数据标签
ax.annotate(
    f"${monthly.iloc[-1]/1000:.1f}K",
    xy=(len(monthly)-1, monthly.iloc[-1]),
    xytext=(-15,10),
    textcoords="offset points",
    fontsize=10,
    color=COLORS["blue"]
)

plt.tight_layout()

# PNG
plt.savefig(
    os.path.join(IMAGE_PATH, "monthly_sales.png"),
    dpi=400,
    bbox_inches="tight"
)

# SVG
plt.savefig(
    os.path.join(IMAGE_PATH, "monthly_sales.svg"),
    bbox_inches="tight"
)

plt.close()

print("√ monthly_sales 完成")

# ==========================================================
# Sales by Category（Tableau风格）
# ==========================================================

category = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(9,6))

bars = ax.bar(
    category.index,
    category.values,
    color=[
        COLORS["blue"],
        COLORS["green"],
        COLORS["orange"]
    ],
    width=0.55
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.grid(axis="y", linestyle="--", alpha=0.25)

ax.set_title(
    "Sales by Category",
    fontsize=18,
    fontweight="bold",
    pad=15
)

ax.set_ylabel("Sales")

ax.yaxis.set_major_formatter(
    FuncFormatter(money)
)

# 数值标签
for bar in bars:

    value = bar.get_height()

    ax.text(
        bar.get_x()+bar.get_width()/2,
        value+10000,
        f"${value/1000:.0f}K",
        ha="center",
        fontsize=11,
        fontweight="bold"
    )

plt.tight_layout()

plt.savefig(
    os.path.join(IMAGE_PATH,"category_sales.png"),
    dpi=400,
    bbox_inches="tight"
)

plt.savefig(
    os.path.join(IMAGE_PATH,"category_sales.svg"),
    bbox_inches="tight"
)

plt.close()

print("√ category_sales 完成")


# ==========================================================
# Sales by Region（商务配色）
# ==========================================================

region = (
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(9,6))

bars = ax.bar(
    region.index,
    region.values,
    color=[
        COLORS["blue"],
        COLORS["cyan"],
        COLORS["green"],
        COLORS["orange"]
    ],
    width=0.55
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.grid(axis="y", linestyle="--", alpha=.25)

ax.set_title(
    "Sales by Region",
    fontsize=18,
    fontweight="bold",
    pad=15
)

ax.set_ylabel("Sales")

ax.yaxis.set_major_formatter(
    FuncFormatter(money)
)

for bar in bars:

    value = bar.get_height()

    ax.text(
        bar.get_x()+bar.get_width()/2,
        value+10000,
        f"${value/1000:.0f}K",
        ha="center",
        fontsize=10,
        fontweight="bold"
    )

plt.tight_layout()

plt.savefig(
    os.path.join(IMAGE_PATH,"region_sales.png"),
    dpi=400,
    bbox_inches="tight"
)

plt.savefig(
    os.path.join(IMAGE_PATH,"region_sales.svg"),
    bbox_inches="tight"
)

plt.close()

print("√ region_sales 完成")


# ==========================================================
# Sales by Segment（Power BI甜甜圈图）
# ==========================================================

segment = (
    df.groupby("Segment")["Sales"]
      .sum()
)

colors = [
    COLORS["blue"],
    COLORS["orange"],
    COLORS["green"]
]

fig, ax = plt.subplots(figsize=(8,8))

wedges, texts, autotexts = ax.pie(
    segment.values,
    labels=segment.index,
    colors=colors,
    startangle=90,
    autopct="%1.1f%%",
    pctdistance=0.78,
    wedgeprops=dict(
        width=0.42,
        edgecolor="white"
    )
)

# 中间白色圆（甜甜圈效果）
centre_circle = plt.Circle(
    (0,0),
    0.58,
    fc="white"
)

fig.gca().add_artist(centre_circle)

plt.title(
    "Sales by Customer Segment",
    fontsize=18,
    fontweight="bold",
    pad=20
)

for txt in autotexts:
    txt.set_fontsize(11)
    txt.set_weight("bold")

plt.tight_layout()

plt.savefig(
    os.path.join(IMAGE_PATH,"segment_sales.png"),
    dpi=400,
    bbox_inches="tight"
)

plt.savefig(
    os.path.join(IMAGE_PATH,"segment_sales.svg"),
    bbox_inches="tight"
)

plt.close()

print("√ segment_sales 完成")

# ==========================================================
# Top10 Products（Professional）
# ==========================================================

top10 = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
      .sort_values()
)

fig, ax = plt.subplots(figsize=(12,7))

bars = ax.barh(
    top10.index,
    top10.values,
    color=COLORS["blue"]
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.grid(axis="x", linestyle="--", alpha=0.3)

ax.set_title(
    "Top 10 Products by Sales",
    fontsize=18,
    fontweight="bold",
    pad=15
)

ax.set_xlabel("Sales")

ax.xaxis.set_major_formatter(
    FuncFormatter(money)
)

for bar in bars:

    value = bar.get_width()

    ax.text(
        value + 1000,
        bar.get_y() + bar.get_height()/2,
        f"${value/1000:.1f}K",
        va="center",
        fontsize=10,
        fontweight="bold"
    )

plt.tight_layout()

plt.savefig(
    os.path.join(IMAGE_PATH,"top10_products.png"),
    dpi=400,
    bbox_inches="tight"
)

plt.savefig(
    os.path.join(IMAGE_PATH,"top10_products.svg"),
    bbox_inches="tight"
)

plt.close()

print("√ top10_products 完成")


# ==========================================================
# Sales Distribution
# ==========================================================

mean_sales = df["Sales"].mean()
median_sales = df["Sales"].median()

fig, ax = plt.subplots(figsize=(10,6))

ax.hist(
    df["Sales"],
    bins=40,
    color=COLORS["cyan"],
    edgecolor="white",
    alpha=0.85
)

ax.axvline(
    mean_sales,
    color=COLORS["red"],
    linewidth=2,
    linestyle="--",
    label=f"Mean: {mean_sales:.2f}"
)

ax.axvline(
    median_sales,
    color=COLORS["orange"],
    linewidth=2,
    linestyle="-.",
    label=f"Median: {median_sales:.2f}"
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.grid(alpha=0.25)

ax.legend()

ax.set_title(
    "Sales Distribution",
    fontsize=18,
    fontweight="bold",
    pad=15
)

ax.set_xlabel("Sales")

ax.set_ylabel("Frequency")

plt.tight_layout()

plt.savefig(
    os.path.join(IMAGE_PATH,"sales_distribution.png"),
    dpi=400,
    bbox_inches="tight"
)

plt.savefig(
    os.path.join(IMAGE_PATH,"sales_distribution.svg"),
    bbox_inches="tight"
)

plt.close()

print("√ sales_distribution 完成")


# ==========================================================
# Summary Report
# ==========================================================

summary = pd.DataFrame({

    "Metric":[
        "Total Sales",
        "Average Sales",
        "Median Sales",
        "Max Sales",
        "Min Sales",
        "Order Count",
        "Customer Count"
    ],

    "Value":[
        round(df["Sales"].sum(),2),
        round(mean_sales,2),
        round(median_sales,2),
        round(df["Sales"].max(),2),
        round(df["Sales"].min(),2),
        df["Order ID"].nunique(),
        df["Customer ID"].nunique()
    ]

})

summary.to_csv(
    os.path.join(IMAGE_PATH,"summary.csv"),
    index=False,
    encoding="utf-8-sig"
)

print("√ summary.csv 完成")


# ==========================================================
# Finish
# ==========================================================

print("\n" + "="*65)
print("🎉 Professional Visualization Finished")
print("="*65)

print(f"图片保存位置：{IMAGE_PATH}")

print("""

生成文件：

✓ monthly_sales.png
✓ monthly_sales.svg

✓ category_sales.png
✓ category_sales.svg

✓ region_sales.png
✓ region_sales.svg

✓ segment_sales.png
✓ segment_sales.svg

✓ top10_products.png
✓ top10_products.svg

✓ sales_distribution.png
✓ sales_distribution.svg

✓ summary.csv

共生成 13 个文件
""")
