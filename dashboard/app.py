import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Analyse des ventes et de la satisfaction client – E-commerce mode",
    layout="wide"
)

sns.set_theme(style="whitegrid")

TEXT_COLOR = "#2E2E2E"
DIVIDER_COLOR = "#EDE6DB"


PINK_DARK = "#D96C8A"
PINK_LIGHT = "#F2A7C2"

GREEN_DARK = "#6BAE9E"
GREEN_LIGHT = "#A8D5BA"


st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #2E2E2E;
    margin-bottom: 5px;
    text-align: center;
}

.sub-title {
    font-size: 20px;
    color: #6BAE9E;
    margin-bottom: 30px;
    text-align: center;
}

.divider {
    height: 2px;
    background-color: #EDE6DB;
    margin: 40px 0;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="main-title">
    Analyse des ventes et de la satisfaction client
</div>
<div class="sub-title">
    E-commerce de mode – comportements d’achat et recommandations
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


@st.cache_data
def load_data():
    return (
        pd.read_csv("data/sales_by_category.csv"),
        pd.read_csv("data/sales_by_age_group.csv"),
        pd.read_csv("data/avg_rating_by_age_group.csv"),
        pd.read_csv("data/recommendation_rate_by_category.csv")
    )

sales_category, sales_age, avg_rating, reco_rate = load_data()



_, icon_left, title_col, icon_right, _ = st.columns([1, 1, 4, 1, 1])

with icon_left:
    st.image("assets/icon-shopping.png", width=55)

with title_col:
    st.markdown(
        "<h2 style='text-align:center; color:#2E2E2E;'>Analyse des ventes</h2>",
        unsafe_allow_html=True
    )

with icon_right:
    st.image("assets/icon-shopping.png", width=55)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")


with col1:
    top_categories = sales_category.sort_values("sales", ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(7, 6))
    sns.barplot(
        data=top_categories,
        x="sales",
        y="category",
        color=PINK_DARK,
        ax=ax
    )

    ax.set_xlabel("Nombre de ventes", fontsize=11)
    ax.set_ylabel("Catégorie de produit", fontsize=11)

    ax.set_axisbelow(True)
    ax.grid(True, axis="x", linestyle="--", alpha=0.4)

    for bar in ax.patches:
        bar.set_height(0.8)

    plt.tight_layout()
    st.pyplot(fig)

    st.markdown(
        "<p style='text-align:center; font-weight:600;'>Ventes par catégorie de produits (Top 10)</p>",
        unsafe_allow_html=True
    )


with col2:
    fig, ax = plt.subplots(figsize=(7, 6))
    sns.barplot(
        data=sales_age,
        x="age_group",
        y="sales",
        color=PINK_LIGHT,
        ax=ax
    )

    ax.set_xlabel("Tranche d’âge", fontsize=11)
    ax.set_ylabel("Nombre de ventes", fontsize=11)

    ax.set_axisbelow(True)
    ax.grid(True, axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()
    st.pyplot(fig)

    st.markdown(
        "<p style='text-align:center; font-weight:600;'>Ventes par tranche d’âge</p>",
        unsafe_allow_html=True
    )


st.markdown('<div class="divider"></div>', unsafe_allow_html=True)



_, icon_left, title_col, icon_right, _ = st.columns([1, 1, 4, 1, 1])

with icon_left:
    st.image("assets/icon-shopping.png", width=55)

with title_col:
    st.markdown(
        "<h2 style='text-align:center; color:#2E2E2E;'>Satisfaction client</h2>",
        unsafe_allow_html=True
    )

with icon_right:
    st.image("assets/icon-shopping.png", width=55)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

col3, col4 = st.columns(2, gap="large")


with col3:
    fig, ax = plt.subplots(figsize=(7, 6))
    sns.lineplot(
        data=avg_rating,
        x="age_group",
        y="avg_rating",
        marker="o",
        linewidth=3,
        color=GREEN_DARK,
        ax=ax
    )

    ax.set_xlabel("Tranche d’âge", fontsize=11)
    ax.set_ylabel("Note moyenne de satisfaction", fontsize=11)
    ax.set_ylim(0, 5)

    ax.set_axisbelow(True)
    ax.grid(True, axis="both", linestyle="--", alpha=0.4)

    plt.tight_layout()
    st.pyplot(fig)

    st.markdown(
        "<p style='text-align:center; font-weight:600;'>Satisfaction moyenne par tranche d’âge</p>",
        unsafe_allow_html=True
    )


with col4:
    reco_sorted = reco_rate.sort_values("recommendation_rate", ascending=False)

    colors = sns.light_palette(
        GREEN_DARK,
        n_colors=len(reco_sorted),
        reverse=True
    )

    fig, ax = plt.subplots(figsize=(7, 6))
    sns.barplot(
        data=reco_sorted,
        x="recommendation_rate",
        y="category",
        palette=colors,
        ax=ax
    )

    ax.set_xlabel("Taux de recommandation", fontsize=11)
    ax.set_ylabel("Catégorie de produit", fontsize=11)
    ax.set_xlim(0, 1)

    ax.set_axisbelow(True)
    ax.grid(True, axis="x", linestyle="--", alpha=0.4)

    plt.tight_layout()
    st.pyplot(fig)

    st.markdown(
        "<p style='text-align:center; font-weight:600;'>Taux de recommandation par catégorie</p>",
        unsafe_allow_html=True
    )
