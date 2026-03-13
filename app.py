import streamlit as st

st.markdown("""
<meta name="google-site-verification" content="<meta name="google-site-verification" content="oYTxFSyfzgxw2P0sGBcZhBwL2qPtvbi57JgbdlVrQMA" />" />
""", unsafe_allow_html=True)

import streamlit as st
import matplotlib.pyplot as plt
import io

st.title("📊 資料作成アプリ（10種類グラフ）")

rows = st.number_input("項目数", 1, 50, 3)

labels = []
values = []

for i in range(rows):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(f"項目{i+1}", key=f"name{i}")

    with col2:
        value = st.number_input(f"値{i+1}", key=f"value{i}")

    labels.append(name)
    values.append(value)

graph_type = st.selectbox(
    "グラフ種類",
    [
        "棒グラフ",
        "横棒グラフ",
        "折れ線グラフ",
        "円グラフ",
        "散布図",
        "面グラフ",
        "ヒストグラム",
        "箱ひげ図",
        "ステップグラフ",
        "ドットグラフ"
    ]
)

fig = None

if st.button("グラフ作成"):

    fig, ax = plt.subplots()

    if graph_type == "棒グラフ":
        ax.bar(labels, values)

    elif graph_type == "横棒グラフ":
        ax.barh(labels, values)

    elif graph_type == "折れ線グラフ":
        ax.plot(labels, values)

    elif graph_type == "円グラフ":
        ax.pie(values, labels=labels, autopct='%1.1f%%')

    elif graph_type == "散布図":
        ax.scatter(range(len(values)), values)

    elif graph_type == "面グラフ":
        ax.fill_between(range(len(values)), values)

    elif graph_type == "ヒストグラム":
        ax.hist(values)

    elif graph_type == "箱ひげ図":
        ax.boxplot(values)

    elif graph_type == "ステップグラフ":
        ax.step(range(len(values)), values)

    elif graph_type == "ドットグラフ":
        ax.plot(range(len(values)), values, 'o')

    plt.xticks(rotation=45)

    st.pyplot(fig)

if fig:

    file_type = st.selectbox(
        "保存形式",
        ["PNG", "JPG", "PDF", "SVG"]
    )

    buf = io.BytesIO()

    if file_type == "PNG":
        fig.savefig(buf, format="png")

    elif file_type == "JPG":
        fig.savefig(buf, format="jpg")

    elif file_type == "PDF":
        fig.savefig(buf, format="pdf")

    elif file_type == "SVG":
        fig.savefig(buf, format="svg")

    st.download_button(
        "ダウンロード",
        buf.getvalue(),
        file_name=f"graph.{file_type.lower()}",
        mime="application/octet-stream"
    )
